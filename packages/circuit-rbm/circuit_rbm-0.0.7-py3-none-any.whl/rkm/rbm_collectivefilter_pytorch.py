import numpy as np
import sys
import random
import time
import matplotlib.pyplot as plt
import pickle
import os
import glob
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
import torch.nn.init as init


class RBM(object):
    ''' Class for generic Restricted Boltzmann Machine (RBM)

    Parameters
    ----------
    model_name : str
        Name of the model
    n_vis : int
        Number of visible units
    n_hin : int
        Number of hidden units
    k : int
        Number of Gibbs sampling steps
    minMax_W : tuple
        Tuple containing the minimum and maximum values for the weights
    energy_type : str
        Type of energy_type function to use. Options are 'hopfield' and 'linear_circuit_i' with i=1,2,3
    optimizer : str
        Type of optimizer to use. Options are 'Adam' and 'SGD'
    regularization : bool
        Whether to use regularization or not
    l1_factor : float
        L1 regularization factor
    l2_factor : float
        L2 regularization factor

    Attributes
    ----------
    name : str
        Name of the model
    W : array-like, shape (n_hin, n_vis)
        Weight matrix
    v_bias : array-like, shape (n_vis,)
        Visible bias vector
    h_bias : array-like, shape (n_hin,)
        Hidden bias vector
    k : int
        Number of Gibbs sampling steps
    min_W : float
        Minimum value for the weights
    max_W : float
        Maximum value for the weights
    energy_type : str
        Type of energy_type function to use. Options are 'hopfield' and 'linear_circuit_i' with i=1,2,3
    n_hidden : int
        Number of hidden units
    n_visible : int
        Number of visible units
    epoch : int
        Current epoch
    errors_free_energy : list
        List containing the free energy difference between data and model
    errors_loss : list
        List containing the loss between data and model
    regularization : bool
        Whether to use regularization or not
    l1 : float
        L1 regularization factor
    l2 : float
        L2 regularization factor
    optimizer : str
        Type of optimizer to use. Options are 'Adam' and 'SGD'
    lr : float
        Learning rate
    m_dW : float
        Adam's momentum for the weights
    m_dv : float
        Adam's momentum for the visible bias
    m_dh : float
        Adam's momentum for the hidden bias
    v_dW : float
        Adam's velocity for the weights
    v_dv : float
        Adam's velocity for the visible bias
    v_dh : float
        Adam's velocity for the hidden bias
    beta1 : float
        Adam's beta1 parameter
    beta2 : float
        Adam's beta2 parameter
    epsilon : float
        Adam's epsilon parameter
    '''
    def __init__(self,
                 model_name,
                 n_vis=784,
                 n_hin=50,
                 k=1,
                 lr=0.01,
                 max_epochs=200000,
                 minMax_W = (-100,100),
                 energy_type = 'hopfield',
                 optimizer ='Adam',
                 regularization = False,
                 l1_factor=1e-7,
                 l2_factor=1e-7,
                 ground_v = 1,
                 ground_h = 1,
                 batch_size=64,
                 train_algo='CD',
                 centering=False,
                 average_data = None,
                 sampling_model_beta = 1,
                 nrelu = False,
                 use_mask = False,
                 mytype = torch.double,
                 is_conditional = False,
                 ):

        self.name = model_name
        print('*** Initializing {}'.format(self.name))
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        # Set default dtype
        self.mytype = mytype
        torch.set_default_dtype(self.mytype)
        print('The model is working on the following device: {}'.format(self.device))        
        self.k = k
        self.max_epochs = max_epochs
        self.lr = lr
        self.min_W, self.max_W = torch.Tensor(minMax_W).to(self.device)
        self.energy_type = energy_type
        self.n_hidden = n_hin
        self.n_visible = n_vis
        self.model_beta = sampling_model_beta
        # Quantities to store
        self.epoch = 0
        self.regularization = regularization
        if self.regularization=='l1':
            self.l1=l1_factor
        elif self.regularization=='l2':
            self.l2=l2_factor
        self.optimizer = optimizer
        # If true, add conditional layer
        self.is_conditional = is_conditional
        # Initialize weights
        self.W = torch.randn((n_hin,n_vis,),dtype=self.mytype, device=self.device)
        if is_conditional:
            self.D = torch.randn((n_hin,n_vis,),dtype=self.mytype, device=self.device)
        self.v_bias = torch.zeros((n_vis,) ,dtype=self.mytype, device=self.device)
        self.h_bias = torch.randn((n_hin,) ,dtype=self.mytype, device=self.device)
        # Make weights contiguous
        self.W = self.W.contiguous()
        if is_conditional:
            self.D = self.D.contiguous()
        self.v_bias = self.v_bias.contiguous()
        self.h_bias = self.h_bias.contiguous()
        ## Initialize with normal distribution
        init.xavier_normal_(self.W)
        if is_conditional:
            init.xavier_normal_(self.D)
        init.normal_(self.v_bias)
        init.normal_(self.h_bias)
        if average_data is not None:
            # Initialize the visible bias from data frequency
            self.v_bias = torch.log(average_data/(1-average_data)+1e-5).to(self.device).to(self.mytype)
        if self.optimizer =='Adam':
            # Adam's momenta
            self.m_dW = 0*self.W
            self.m_dv = 0*self.v_bias
            self.m_dh = 0*self.h_bias
            self.v_dW = 0*self.W
            self.v_dv = 0*self.v_bias
            self.v_dh = 0*self.h_bias
            # Adam's parameters
            self.beta1  =0.9
            self.beta2  =0.999
            self.epsilon=1e-8
        if self.energy_type != 'hopfield':
            self.ground_v = ground_v
            self.ground_h = ground_h
            self._update_circuit_variables()
        self.train_algo = train_algo
        self.batch_size = batch_size
        if self.train_algo=='PCD':
            # Initialize the persistent chains
            self.persistent_chains = torch.where(torch.rand(self.batch_size, self.n_visible) > 0.5, 1.0, 0.0).to(self.device).to(self.mytype)
        self.centering = centering
        if self.centering:
            if average_data.shape[0]!=n_vis:
                print('Error: you need to provide the average of the data to center the gradient')
                sys.exit()
            # Initialize the offsets for the gradient centering
            self.ov = average_data.to(self.device)
            self.oh = self.h_bias*0 + 0.5
            self.batch_ov = self.v_bias*0
            self.batch_oh = self.h_bias*0
            # And the sliding factors
            self.slv = 0.01
            self.slh = 0.01
        else:
            self.ov=0
            self.oh=0
        # Epochs at which to store the model
        num_points = 50 
        self.t_to_save = sorted(list(set(np.round(np.logspace(np.log10(1), np.log10(self.max_epochs), num_points)).astype(int).tolist())))
        # *** If True I am using the NReLU
        self.nrelu=nrelu
        if self.nrelu:
            print('ERROR: NReLU not fully implemented')
            sys.exit()
        # use mask for recommendation systems
        self.use_mask = use_mask


    def pretrain(self, pretrained_model):
        # Check if you have model load points
        filename_list = glob.glob('model_states/{}_t*.pkl'.format(pretrained_model))
        if len(filename_list)>0:
            all_loadpoints = sorted([int(x.split('_t')[-1].split('.pkl')[0]) for x in filename_list])
            last_epoch = all_loadpoints[-1]
            print('** Using as pretraining model {} at epoch {}'.format(pretrained_model,last_epoch))
            with open('model_states/{}_t{}.pkl'.format(pretrained_model,last_epoch), "rb") as file:
                temp_model = pickle.load(file)
                # *** Import pretrained parameters
                self.W = temp_model.W.to(self.mytype)
                self.h_bias = temp_model.h_bias.to(self.mytype)
                self.v_bias = temp_model.v_bias.to(self.mytype)
                if self.is_conditional and temp_model.is_conditional:
                    self.D = temp_model.D.to(self.mytype)
        else:
            print('** No load points for {}'.format(pretrained_model))


    def v_to_h(self,v,beta=None):
        if beta is None:
            beta = self.model_beta
        return self.Bernoulli_v_to_h(v,beta)
    
    def h_to_v(self,h,beta=None):
        if beta is None:
            beta = self.model_beta
        return self.Bernoulli_h_to_v(h,beta)


    def Bernoulli_v_to_h(self,v,beta):
        p_h = self._prob_h_given_v(v, beta)
        sample_h = torch.bernoulli(p_h)
        return p_h,sample_h
    def Bernoulli_h_to_v(self,h,beta):
        p_v = self._prob_v_given_h(h, beta)
        sample_v = torch.bernoulli(p_v)
        return p_v,sample_v
        

    def _free_energy_hopfield(self, v, beta=None):
        if beta is None:
            beta = self.model_beta
        vbias_term = torch.mv(v, self.v_bias)*beta  
        wx_b = torch.mm(v, self.W.t()) + self.h_bias 
        hidden_term = torch.sum(torch.log(1 + torch.exp(wx_b * beta)), axis=1)
        return -hidden_term - vbias_term

    def _energy_hopfield(self, v, h):
        energy = -(torch.mm(v, self.W.t()) * h).sum(1)  - torch.mv(v, self.v_bias) - torch.mv(h, self.h_bias)
        return energy

    def _energy_linear_circuit_4(self, v, h):
        # ****** TO BE DONE! ******
        energy = -(torch.mm(v, self.W.t()) * h).sum(1)  - torch.mv(v, self.v_bias) - torch.mv(h, self.h_bias)
        return energy
    


    def forward(self, v, k, beta=None):
        if beta is None:
            beta = self.model_beta
        pre_h1,h1 = self.v_to_h(v, beta)
        h_ = h1
        for _ in range(k):
            pre_v_,v_ = self.h_to_v(h_, beta)
            #v_ *= self.mask
            pre_h_,h_ = self.v_to_h(v_, beta)
        return v_

    
    # Function to average the gradients, excluding the masked elements
    def maskedmean(self, x):
        mask_sum = (x!=0).to(torch.int).sum(dim=0)

        # Check if any element in mask_sum is zero
        if (mask_sum == 0).any():
            #print("Warning: Zero elements in mask_sum. Replacing with 1.")
            # Replace zero elements with 1 in mask_sum
            mask_sum = torch.where(mask_sum == 0, 1, mask_sum)
        
        return torch.div(x.sum(dim=0) , mask_sum)


    def train(self, train_data, test_data=[], print_error=False, print_test_error=False):
        '''
        Train the model using the given data and parameters
        '''
        while self.epoch < self.max_epochs:
            if self.energy_type !='hopfield':
                self.clip_weights()
                self.clip_bias()
                self._update_circuit_variables()
            else:
                self.W_t = self.W.t()
            if self.is_conditional:
                self.D_t = self.D.t()
            # **** Train loop    
            for _, v_data in enumerate(train_data):
                start_time = time.time()
                # Use mask (for conditional RBM)
                self.mask = (v_data!=0.5).to(self.mytype) 
                if self.train_algo=='PCD':
                    # Update the chain after every batch 
                    self.persistent_chains = self.forward(self.persistent_chains,self.k)
                    v_model = self.persistent_chains
                elif self.train_algo=='RDM':
                    # This algo uses random samples
                    # But since we want to train with the same exact protocol that we will use for generation,
                    ## we random sample from the hidden and not the visible
                    #h_rnd = torch.randint(high=2, size=(self.batch_size, self.n_hidden), device=self.device, dtype=self.mytype)
                    #_, v_model = self.h_to_v(h_rnd)
                    v_model = torch.randint(high=2, size=(self.batch_size, self.n_visible), device=self.device, dtype=self.mytype)
                    #v_model = torch.bernoulli(0.5*torch.ones(size=(self.batch_size, self.n_visible), device=self.device, dtype=self.mytype))
                    #### This version has problems
                    ###random_tensor = torch.rand(self.batch_size, self.n_visible, device=self.device, dtype=self.mytype)
                    ###v_model = self.forward(torch.where(random_tensor > 0.5, 1.0, 0.0), self.k)
                    v_model = self.forward(v_model, self.k)
                elif self.train_algo=='CD':
                    v_model = self.forward(v_data,self.k)

                # Apply model
                h_data = self.v_to_h(v_data)[0]
                h_model = self.v_to_h(v_model)[0]

                # Apply centering
                if self.centering:
                    self.batch_ov = v_data.mean(0)
                    self.batch_oh = h_data.mean(0)
                    # update with sliding
                    self.ov = (1-self.slv)*self.ov + self.slv*self.batch_ov
                    self.oh = (1-self.slh)*self.oh + self.slh*self.batch_oh
                
                # Compute gradients
                dEdW_data , dEdv_bias_data,  dEdh_bias_data , dEdD_data = self.derivatives(v_data,h_data)
                dEdW_model, dEdv_bias_model, dEdh_bias_model, dEdD_model = self.derivatives(v_model,h_model)
                

                # Average over batch
                dEdW_data       = self.maskedmean(dEdW_data)      
                dEdv_bias_data  = self.maskedmean(dEdv_bias_data) 
                dEdh_bias_data  = torch.mean(dEdh_bias_data, dim=0) 
                dEdW_model      = self.maskedmean(dEdW_model)     
                dEdv_bias_model = self.maskedmean(dEdv_bias_model)
                dEdh_bias_model = torch.mean(dEdh_bias_model, dim=0)
                if self.is_conditional:
                    dEdD_model = torch.mean(dEdD_model, dim=0)
                    dEdD_data  = torch.mean(dEdD_data , dim=0)

                
                # Update weights and biases
                if self.optimizer =='Adam':
                    self.Adam_update(self.epoch+1,
                                    dEdW_data, 
                                    dEdW_model, 
                                    dEdv_bias_data, 
                                    dEdv_bias_model, 
                                    dEdh_bias_data, 
                                    dEdh_bias_model)
                elif self.optimizer =='SGD':
                    self.SGD_update(dEdW_data,
                                    dEdW_model,
                                    dEdv_bias_data,
                                    dEdv_bias_model,
                                    dEdh_bias_data,
                                    dEdh_bias_model,
                                    dEdD_data,
                                    dEdD_model)
            
                if self.energy_type !='hopfield':
                    self.clip_weights()
                    self.clip_bias()
                    self._update_circuit_variables()
                else:
                    self.W_t = self.W.t()
                if self.is_conditional:
                    self.D_t = self.D.t()

                self.epoch += 1

                # Store the model state
                if self.epoch in self.t_to_save:
                    with open("model_states/{}_t{}.pkl".format(self.name,self.epoch), "wb") as file:
                        pickle.dump(self, file)

                if self.epoch % 100 ==0:
                    t = time.time()-start_time
                    if print_error:
                        v_model = self.forward(v_data, self.k)
                        v_model[v_data==0.5] = v_data[v_data==0.5]
                        rec_error_train = ((v_model - v_data)**2).mean(1).mean(0)
                        if not print_test_error:
                            print ("Epoch: %d , train-err %.5g , time: %f"%(self.epoch, rec_error_train, t))
                        else:
                            self.mask = (test_data!=0.5).to(self.mytype) 
                            t_model = self.forward(test_data, self.k)
                            t_model[test_data==0.5] = test_data[test_data==0.5]
                            rec_error_test = ((t_model - test_data)**2).mean(1).mean(0)
                            print ("Epoch: %d , Test-err %.5g , train-err %.5g , time: %f"%(self.epoch, rec_error_test, rec_error_train, t))
                    else:
                        print ("Epoch: %d , time: %f"%(self.epoch, t))

        print('*** Training finished')


    def SGD_update(self, dEdW_data, dEdW_model, dEdv_bias_data, dEdv_bias_model, dEdh_bias_data, dEdh_bias_model, dEdD_data, dEdD_model):        
        # Gradients 
        dW = -dEdW_data      + dEdW_model
        dv = -dEdv_bias_data + dEdv_bias_model
        dh = -dEdh_bias_data + dEdh_bias_model
        if self.is_conditional:
            dD = -dEdD_data      + dEdD_model
        if self.centering:
            dv = dv - torch.matmul(self.oh, dW)
            dh = dh - torch.matmul(self.ov, dW.t())
        # Add regularization term
        if self.regularization=='l2':
            dW += self.l2 * 2*self.W
            dv += self.l2 * 2*self.v_bias
            dh += self.l2 * 2*self.h_bias
        elif self.regularization=='l1':
            dW += self.l1 * torch.sign(self.W)
            dv += self.l1 * torch.sign(self.v_bias)
            dh += self.l1 * torch.sign(self.h_bias)
        # Update parameters in-place
        # and clip
        if self.is_conditional:
            gnorm = torch.norm(dW) + torch.norm(dv) + torch.norm(dh) +torch.norm(dD)
        else:
            gnorm = torch.norm(dW) + torch.norm(dv) + torch.norm(dh)
        if gnorm>10:
            myclip = 10./gnorm
        else:
            myclip = 1
        self.W.add_(self.lr * dW*myclip)
        self.v_bias.add_(self.lr * dv*myclip)
        self.h_bias.add_(self.lr * dh*myclip)
        if self.is_conditional:
            self.D.add_(self.lr * dD*myclip)

    def Adam_update(self, t, dEdW_data, dEdW_model, dEdv_bias_data, dEdv_bias_model, dEdh_bias_data, dEdh_bias_model):        
        # Gradients 
        dW = -dEdW_data      + dEdW_model
        dv = -dEdv_bias_data + dEdv_bias_model
        dh = -dEdh_bias_data + dEdh_bias_model
        if self.centering:
            dv = dv - torch.matmul(self.oh, dW)
            dh = dh - torch.matmul(self.ov, dW.t())
        # Add regularization term
        if self.regularization=='l2':
            dW += self.l2 * 2*self.W
            dv += self.l2 * 2*self.v_bias
            dh += self.l2 * 2*self.h_bias
        elif self.regularization=='l1':
            dW += self.l1 * torch.sign(self.W)
            dv += self.l1 * torch.sign(self.v_bias)
            dh += self.l1 * torch.sign(self.h_bias)
        # momentum beta1
        self.m_dW = self.beta1*self.m_dW+(1-self.beta1)*dW
        self.m_dv = self.beta1*self.m_dv+(1-self.beta1)*dv
        self.m_dh = self.beta1*self.m_dh+(1-self.beta1)*dh
        # momentum beta2
        self.v_dW = self.beta2*self.v_dW+(1-self.beta2)*(dW**2)
        self.v_dv = self.beta2*self.v_dv+(1-self.beta2)*(dv**2)
        self.v_dh = self.beta2*self.v_dh+(1-self.beta2)*(dh**2)
        # bias correction
        m_dW_corr = self.m_dW/(1-self.beta1**t)
        m_dv_corr = self.m_dv/(1-self.beta1**t)
        m_dh_corr = self.m_dh/(1-self.beta1**t)
        v_dW_corr = self.v_dW/(1-self.beta2**t)
        v_dv_corr = self.v_dv/(1-self.beta2**t)
        v_dh_corr = self.v_dh/(1-self.beta2**t)
        # Update
        self.W = self.W + self.lr*(m_dW_corr/(torch.sqrt(v_dW_corr)+self.epsilon))
        self.v_bias = self.v_bias + self.lr*(m_dv_corr/(torch.sqrt(v_dv_corr)+self.epsilon))
        self.h_bias = self.h_bias + self.lr*(m_dh_corr/(torch.sqrt(v_dh_corr)+self.epsilon))
        
    def reconstruct(self, data, k):
        data = torch.Tensor(data).to(self.device).to(self.mytype)
        v_model = self.forward(data, k)
        return data.detach().cpu().numpy(), v_model.detach().cpu().numpy()
    
    def generate(self, n_samples, k, h_binarized=True, from_visible=False, beta=None):
        if beta is None:
            beta = self.model_beta
        if from_visible:
            v = torch.randint(high=2, size=(n_samples, self.n_visible), device=self.device, dtype=self.mytype)
        else:
            if h_binarized:
                h = torch.randint(high=2, size=(n_samples, self.n_hidden), device=self.device, dtype=self.mytype)
            else:
                h = torch.rand(n_samples, self.n_hidden, device=self.device, dtype=self.mytype)
            _, v = self.h_to_v(h)
        v_model = self.forward(v, k, beta)
        return v_model.detach().cpu().numpy()
    
    def clip_weights(self):
        self.W = torch.clip(self.W,self.min_W,self.max_W)
        self.W_t = self.W.t()
    
    def clip_bias(self):
        self.v_bias = torch.clip(self.v_bias,self.min_W,self.max_W)
        self.h_bias = torch.clip(self.h_bias,self.min_W,self.max_W)

    def _prob_h_given_v(self,v, beta=None):
        if beta is None:
            beta = self.model_beta
        return torch.sigmoid(beta*self.delta_eh(v))
    
    def _prob_v_given_h(self,h, beta=None):
        if beta is None:
            beta = self.model_beta
        return torch.sigmoid(beta*self.delta_ev(h))
    
    def delta_eh(self,v):
        if self.energy_type == 'hopfield':
            if self.use_mask:
                return self._delta_eh_hopfield_masked(v)
            else:
                return self._delta_eh_hopfield(v)
        elif self.energy_type == 'linear_circuit_4':
            if self.use_mask:
                return self._delta_eh_linear_circuit_4_masked(v)
            else:
                return self._delta_eh_linear_circuit_4(v)
            
        
    def delta_ev(self,h):
        if self.energy_type == 'hopfield':
            if self.use_mask:
                return self._delta_ev_hopfield_masked(h)
            else:
                return self._delta_ev_hopfield(h)
        elif self.energy_type == 'linear_circuit_4':
            if self.use_mask:
                return self._delta_ev_linear_circuit_4_masked(h)
            else:
                return self._delta_ev_linear_circuit_4(h)


    # **** Hopfield transfer functions
    def _delta_eh_hopfield(self, v):
        return torch.mm(v, self.W_t) + self.h_bias 
    def _delta_ev_hopfield(self, h):
        return torch.mm(h, self.W) + self.v_bias
    # **** (masked) Hopfield transfer functions
    def _delta_eh_hopfield_masked(self, v):
#        Wtm = self.W_t *self.mask.unsqueeze(-1)
#        return torch.bmm(v.unsqueeze(1), Wtm).squeeze(1) + self.h_bias + torch.mm(self.mask , self.D_t)
        if self.is_conditional:
            return torch.mm(v*self.mask, self.W_t) + self.h_bias + torch.mm(self.mask , self.D_t)
        else:
            return torch.mm(v*self.mask, self.W_t) + self.h_bias
    def _delta_ev_hopfield_masked(self, h):
        return torch.mm(h, self.W) + self.v_bias


    # **** linear_circuit_4 transfer functions
    def _delta_ev_linear_circuit_4(self, h):
        return torch.mm(torch.mul(h, 2) - 1, self._k_diff) + self._vb_posneg
    def _delta_eh_linear_circuit_4(self, v):
        return torch.mm(torch.mul(v, 2) - 1, self._k_diff_t) + self._hb_posneg
    # **** (masked) linear_circuit_4 transfer functions
    def _delta_ev_linear_circuit_4_masked(self, h):
        return torch.mm(torch.mul(h, 2) - 1, self._k_diff) + self._vb_posneg
    def _delta_eh_linear_circuit_4_masked(self, v):
        if self.is_conditional:
            return torch.mm(torch.mul(v*self.mask, 2) - 1, self._k_diff_t) + self._hb_posneg + torch.mm(torch.mul(self.mask, 2) - 1, self._D_diff_t)
        else:
            return torch.mm(torch.mul(v*self.mask, 2) - 1, self._k_diff_t) + self._hb_posneg



    def _update_circuit_variables(self):
        self._k_pos = self.k_pos()
        self._k_neg = self.k_neg()
        self._v_bias_pos = self.v_bias_pos()
        self._v_bias_neg = self.v_bias_neg()
        self._h_bias_pos = self.h_bias_pos()
        self._h_bias_neg = self.h_bias_neg()
        self._k_diff = self._k_pos - self._k_neg
        self._k_diff_t = self._k_diff.t()
        self._v_bias_pos_diff = self._v_bias_pos * (0.5 - self.ground_v)
        self._v_bias_neg_diff = self._v_bias_neg * (0.5 - self.ground_v)
        self._h_bias_pos_diff = self._h_bias_pos * (0.5 - self.ground_h)
        self._h_bias_neg_diff = self._h_bias_neg * (0.5 - self.ground_h)
        self._vb_posneg = - self._v_bias_pos_diff + self._v_bias_neg_diff
        self._hb_posneg = - self._h_bias_pos_diff + self._h_bias_neg_diff
        if self.is_conditional:
            self._D_pos = self.D_pos()
            self._D_neg = self.D_neg()
            self._D_diff = self._D_pos - self._D_neg
            self._D_diff_t = self._D_diff.t()

    
    def derivatives(self,v,h):
        if self.energy_type == 'hopfield':
            return self.derivatives_hopfield(v,h)
        elif self.energy_type == 'linear_circuit_4':
            return self.derivatives_linear_circuit_4(v,h)
        

    # CHANGE THIS FUNCTION TO USE THE CORRECT FREE ENERGY
    def free_energy(self,v, beta=None):
        if beta is None:
            beta = self.model_beta
        if self.energy_type == 'hopfield':
            return self._free_energy_hopfield(v, beta)
        elif self.energy_type == 'linear_circuit_4':
            return self._free_energy_hopfield(v)

    def energy(self,v,h):
        if self.energy_type == 'hopfield':
            return self._energy_hopfield(v,h)
        elif self.energy_type == 'linear_circuit_4':
            return self._energy_linear_circuit_4(v,h)
        
    
    def derivatives_hopfield(self,v,h):
        # h has shape (N, n_h) and v has shape (N, n_v), we want result to have shape (N, n_h, n_v)
        if self.centering:
            dEdW = -torch.einsum('ij,ik->ijk', h-self.oh, v-self.ov)
        else:
            dEdW = -torch.einsum('ij,ik->ijk', h, v*self.mask)
        dEdv_bias = -v*self.mask
        dEdh_bias = -h
        if self.is_conditional:
            dEdD = -torch.einsum('ij,ik->ijk', h, self.mask)
        # They have to be renormalized according to the size of the mask
        #masksizefactor = self.n_visible/self.mask.sum(-1)
        if self.is_conditional:
            return dEdW, dEdv_bias, dEdh_bias, dEdD
            #return dEdW*masksizefactor.unsqueeze(1).unsqueeze(1), dEdv_bias*masksizefactor.unsqueeze(1), dEdh_bias, dEdD#*masksizefactor.unsqueeze(1).unsqueeze(1)
        else:
            return dEdW, dEdv_bias, dEdh_bias, None
            #return dEdW*masksizefactor.unsqueeze(1).unsqueeze(1), dEdv_bias*masksizefactor.unsqueeze(1), dEdh_bias, None
    

    def derivatives_linear_circuit_4(self, v, h):
        v_square = torch.square(v).unsqueeze(1)
        vneg_square = torch.square(1 - v).unsqueeze(1)
        negh = 1-h
        h_square = torch.square(h).unsqueeze(2)
        hneg_square = torch.square(negh).unsqueeze(2)
        v_masked = v*self.mask
        negv_masked = 1-v_masked
        v_square_masked = torch.square(v_masked).unsqueeze(1)
        vneg_square_masked = torch.square(1 - v_masked).unsqueeze(1)

        ein_h_vm = torch.einsum('ij,ik->ijk', h, v_masked)
        ein_negh_vm = torch.einsum('ij,ik->ijk', negh, v_masked)
        ein_h_negvm = torch.einsum('ij,ik->ijk', h, negv_masked)
        ein_negh_negvm = torch.einsum('ij,ik->ijk', negh, negv_masked)

        dEdk_pos = 0.5*((-2*ein_h_vm + v_square_masked + h_square) + (-2*ein_negh_negvm + vneg_square_masked + hneg_square))
        dEdk_neg = 0.5*((-2*ein_h_negvm + vneg_square_masked + h_square) + (-2*ein_negh_vm + v_square_masked + hneg_square))
        dkdw_pos = self.dk_pos().unsqueeze(0)
        dkdw_neg = self.dk_neg().unsqueeze(0)
        dEdW = dEdk_pos * dkdw_pos + dEdk_neg * dkdw_neg

        dEdv_bias_pos = -self.ground_v * v_masked + 0.5 * torch.square(v_masked)
        dEdv_bias_neg = -self.ground_v * negv_masked + 0.5 * torch.square(negv_masked)
        dv_biasdv_pos = self.dv_bias_pos().unsqueeze(0)
        dv_biasdv_neg = self.dv_bias_neg().unsqueeze(0)
        dEdv_bias = dEdv_bias_pos * dv_biasdv_pos + dEdv_bias_neg * dv_biasdv_neg
        
        dEdh_bias_pos = -self.ground_h * h + 0.5 * torch.square(h)
        dEdh_bias_neg = -self.ground_h * (negh) + 0.5 * torch.square(negh)
        dh_biasdh_pos = self.dh_bias_pos().unsqueeze(0)
        dh_biasdh_neg = self.dh_bias_neg().unsqueeze(0)
        dEdh_bias = dEdh_bias_pos * dh_biasdh_pos + dEdh_bias_neg * dh_biasdh_neg

        if self.is_conditional:
            ## No this gradient is wrong! (this is same shape as W, but it is not like this in C-RBM)
            negm = 1-self.mask
            m_square = torch.square(self.mask).unsqueeze(1)
            mneg_square = torch.square(negm).unsqueeze(1)
            
            ein_h_m = torch.einsum('ij,ik->ijk', h, self.mask)
            ein_h_negm = torch.einsum('ij,ik->ijk', h, negm)
            ein_negh_m = torch.einsum('ij,ik->ijk', negh, self.mask)
            ein_negh_negm = torch.einsum('ij,ik->ijk', negh, negm)

            dEdD_pos = 0.5*((-2*ein_h_m + m_square + h_square) + (-2*ein_negh_negm + mneg_square + hneg_square))
            dEdD_neg = 0.5*((-2*ein_h_negm + mneg_square + h_square) + (-2*ein_negh_m + m_square + hneg_square))
            dDdw_pos = self.dD_pos().unsqueeze(0)
            dDdw_neg = self.dD_neg().unsqueeze(0)
            dEdD = dEdD_pos * dDdw_pos + dEdD_neg * dDdw_neg

            #negm = 1-self.mask
            #dEdD = torch.einsum('ij,ik->ijk',dEdh_bias_pos*dh_biasdh_pos, self.mask) + torch.einsum('ij,ik->ijk',dEdh_bias_neg*dh_biasdh_neg, negm)

        # They have to be renormalized according to the size of the mask
        #masksizefactor = self.n_visible/self.mask.sum(-1)
        if self.is_conditional:
            return dEdW, dEdv_bias, dEdh_bias, dEdD
            #return dEdW*masksizefactor.unsqueeze(1).unsqueeze(1), dEdv_bias*masksizefactor.unsqueeze(1), dEdh_bias, dEdD#*masksizefactor.unsqueeze(1).unsqueeze(1)
        else:
            return dEdW, dEdv_bias, dEdh_bias, None
            #return dEdW*masksizefactor.unsqueeze(1).unsqueeze(1), dEdv_bias*masksizefactor.unsqueeze(1), dEdh_bias, None



    # ***** Get high-level circuit weights 
    def k_pos(self):
        return torch.relu(self.W)
    def k_neg(self):
        return torch.relu(-self.W)
    def dk_pos(self):
        return (self.W > 0).to(self.W.dtype)
    def dk_neg(self):
        return -(self.W < 0).to(self.W.dtype)
    def v_bias_pos(self):
        return torch.relu(self.v_bias)
    def v_bias_neg(self):
        return torch.relu(-self.v_bias)
    def dv_bias_pos(self):
        return (self.v_bias > 0).to(self.v_bias.dtype)
    def dv_bias_neg(self):
        return -(self.v_bias < 0).to(self.v_bias.dtype)
    # ***** Get high-level circuit bias
    def h_bias_pos(self):
        return torch.relu(self.h_bias)
    def h_bias_neg(self):
        return torch.relu(-self.h_bias)
    def dh_bias_pos(self):
        return (self.h_bias > 0).to(self.h_bias.dtype)
    def dh_bias_neg(self):
        return -(self.h_bias < 0).to(self.h_bias.dtype)
    # ***** Get high-level conditional weights
    def D_pos(self):
        return torch.relu(self.D)
    def D_neg(self):
        return torch.relu(-self.D)
    def dD_pos(self):
        return (self.D > 0).to(self.D.dtype)
    def dD_neg(self):
        return -(self.D < 0).to(self.D.dtype)


    # **** PLOTTING
    def plot_weights(self,t):
        Ndata = self.W.shape[0]
        # Reshape the matrix into a 3D array
        data_3d = self.W.detach().cpu().numpy().reshape(Ndata, 28, 28)
        # Determine the number of rows and columns for the subplot grid
        num_rows = int(np.ceil(np.sqrt(Ndata)))
        num_cols = int(np.ceil(Ndata / num_rows))
        # Create a figure and axis for the plot
        fig, ax = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(10, 10))
        # Iterate over the submatrices and plot them
        for i in range(Ndata):
            row = i // num_cols
            col = i % num_cols
            ax[row, col].imshow(data_3d[i],cmap='magma')
            ax[row, col].axis('off')
        # Remove empty subplots if the number of submatrices doesn't fill the entire grid
        if num_rows * num_cols > Ndata:
            for i in range(Ndata, num_rows * num_cols):
                row = i // num_cols
                col = i % num_cols
                fig.delaxes(ax[row, col])
        # Adjust the spacing between subplots
        plt.suptitle('Weights epoch {}'.format(t))
        plt.subplots_adjust(wspace=0.05, hspace=0.05, top=0.9)
        # Get the minimum and maximum values from the data
        vmin = np.min(self.W.detach().cpu().numpy())
        vmax = np.max(self.W.detach().cpu().numpy())
        # Create a dummy image for the colorbar
        dummy_img = np.zeros((1, 1))  # Dummy image with all zeros
        # Add a colorbar using the dummy image as the mappable
        cax = fig.add_axes([0.93, 0.15, 0.02, 0.7])  # Position of the colorbar
        plt.colorbar(plt.imshow(dummy_img, cmap='magma', vmin=vmin, vmax=vmax), cax=cax)
        # Adjust the height of the colorbar axes to match the height of the figure
        cax.set_aspect('auto')
    # ** Plotting bias
    def plot_bias(self,t):
        h_bias = self.h_bias.detach().cpu().numpy()
        v_bias = self.v_bias.detach().cpu().numpy()
        # Set up the figure with two subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
        # Plot histogram for hidden biases
        ax1.hist(h_bias, bins=20, color='blue', edgecolor='black')
        ax1.set_xlabel('Values')
        ax1.set_ylabel('Frequency')
        ax1.set_title('Hidden Biases epoch {}'.format(t))
        # Plot histogram for visible biases
        ax2.hist(v_bias, bins=20, color='red', edgecolor='black')
        ax2.set_xlabel('Values')
        ax2.set_ylabel('Frequency')
        ax2.set_title('Visible Biases epoch {}'.format(t))
        # Adjust layout for better readability
        plt.tight_layout()