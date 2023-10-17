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
                 mytype = torch.double,
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
        # Initialize weights
        self.W = torch.randn((n_hin,n_vis,),dtype=self.mytype, device=self.device)
        self.v_bias = torch.zeros((n_vis,) ,dtype=self.mytype, device=self.device)
        self.h_bias = torch.randn((n_hin,) ,dtype=self.mytype, device=self.device)
        self.logsigma_sq = torch.zeros((n_vis,) ,dtype=self.mytype, device=self.device)
        # Make weights contiguous
        self.W = self.W.contiguous()
        self.v_bias = self.v_bias.contiguous()
        self.h_bias = self.h_bias.contiguous()
        ## Initialize with normal distribution
        init.xavier_normal_(self.W)
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
            self.m_ds = 0*self.v_bias
            self.v_dW = 0*self.W
            self.v_dv = 0*self.v_bias
            self.v_dh = 0*self.h_bias
            self.v_ds = 0*self.v_bias
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
            #self.persistent_chains = torch.where(torch.rand(self.batch_size, self.n_visible) > 0.5, 1.0, 0.0).to(self.device).to(self.mytype)
            self.persistent_chains = torch.randn(self.batch_size, self.n_visible).to(self.device).to(self.mytype)
        self.centering = centering
        if self.centering:
            if average_data.shape[1]!=n_vis:
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
#        self.pre_generated_random_numbers = None
#        self.pre_generated_count = 10**6
#        self.used_random_count = 0


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
                self.logsigma_sq = temp_model.logsigma_sq.to(self.mytype)
        else:
            print('** No load points for {}'.format(pretrained_model))


    def v_to_h(self,v,beta=None):
        if beta is None:
            beta = self.model_beta
        return self.GaussBernoulli_v_to_h(v,beta)
    
    def h_to_v(self,h,beta=None):
        if beta is None:
            beta = self.model_beta
        return self.GaussBernoulli_h_to_v(h,beta)

    def GaussBernoulli_v_to_h(self,v,beta):
        if self.energy_type == 'hopfield':
            p_h = self._prob_h_given_v(v/self.sigma_sq, beta)
        else:
            p_h = self._prob_h_given_v(v, beta)
        sample_h = torch.bernoulli(p_h)
        return p_h,sample_h
    def GaussBernoulli_h_to_v(self,h,beta):
        if self.energy_type == 'hopfield':
            mean = self.delta_ev(h)
            sample_v = mean + torch.randn_like(mean) * self.sigma
        else:
            mean = self.delta_ev(h)*self.sigma_sq
            sample_v = mean + torch.randn_like(mean) * self.sigma
        
        return None,sample_v


        
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
#        print(v.mean(-1))
        h_ = h1
        for _ in range(k):
            pre_v_,v_ = self.h_to_v(h_, beta)
            pre_h_,h_ = self.v_to_h(v_, beta)
        return v_

    
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
                self.sigma_sq = torch.exp(self.logsigma_sq)
                self.sigma = torch.sqrt(self.sigma_sq)
            for _, v_data in enumerate(train_data):
                start_time = time.time()
                # Ignore the label in v_data[1]
                #v_data = v_data[0]
                if self.train_algo=='PCD':
                    # Update the chain after every batch 
                    self.persistent_chains = self.forward(self.persistent_chains,self.k)
                    v_model = self.persistent_chains
                elif self.train_algo=='RDM':
                    # This algo uses random samples
                    # ** we want to train with the same exact protocol that we will use for generation!
                    #v_model = torch.rand(self.batch_size, self.n_visible, device=self.device, dtype=self.mytype)
                    v_model = torch.randn(self.batch_size, self.n_visible, device=self.device, dtype=self.mytype)
                    v_model = self.forward(v_model, self.k)
                elif self.train_algo=='CD':
                    v_model = self.forward(v_data,self.k)
                
                # Apply model (Notice that I need p(h) which is element 0)
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
                dEdW_data , dEdv_bias_data,  dEdh_bias_data , dEds_data = self.derivatives(v_data,h_data)
                dEdW_model, dEdv_bias_model, dEdh_bias_model, dEds_model = self.derivatives(v_model,h_model)

                # Average over batch
                dEdW_data       = torch.mean(dEdW_data, dim=0)      
                dEdv_bias_data  = torch.mean(dEdv_bias_data, dim=0) 
                dEdh_bias_data  = torch.mean(dEdh_bias_data, dim=0) 
                dEdW_model      = torch.mean(dEdW_model, dim=0)     
                dEdv_bias_model = torch.mean(dEdv_bias_model, dim=0)
                dEdh_bias_model = torch.mean(dEdh_bias_model, dim=0)
                if self.energy_type=='hopfield':
                    dEds_data = torch.mean(dEds_data, dim=0)
                    dEds_model = torch.mean(dEds_model, dim=0)

                # Update weights and biases
                if self.optimizer =='Adam':
                    self.Adam_update(self.epoch+1,
                                    dEdW_data, 
                                    dEdW_model, 
                                    dEdv_bias_data, 
                                    dEdv_bias_model, 
                                    dEdh_bias_data, 
                                    dEdh_bias_model,
                                    dEds_data,
                                    dEds_model,
                                    )
                elif self.optimizer =='SGD':
                    self.SGD_update(dEdW_data,
                                    dEdW_model,
                                    dEdv_bias_data,
                                    dEdv_bias_model,
                                    dEdh_bias_data,
                                    dEdh_bias_model,
                                    dEds_data,
                                    dEds_model,
                                    )
            
                if self.energy_type !='hopfield':
                    self.clip_weights()
                    self.clip_bias()
                    self._update_circuit_variables()
                else:
                    self.W_t = self.W.t()
                    self.sigma_sq = torch.exp(self.logsigma_sq)
                    self.sigma = torch.sqrt(self.sigma_sq)

                self.epoch += 1

                # Store the model state
                if self.epoch in self.t_to_save:
                    #print('*saving*')
                    with open("model_states/{}_t{}.pkl".format(self.name,self.epoch), "wb") as file:
                        pickle.dump(self, file)

                if self.epoch % 100 ==0:
                    t = time.time()-start_time
                    if print_error:
                        v_model = self.forward(v_data, 1)
                        rec_error_train = ((v_model - v_data)**2).mean(1).mean(0)
                        if not print_test_error:
                            print ("Epoch: %d , train-err %.5g , time: %f"%(self.epoch, rec_error_train, t))
                        else:
                            t_model = self.forward(test_data, 1)
                            rec_error_test = ((t_model - test_data)**2).mean(1).mean(0)
                            print ("Epoch: %d , Test-err %.5g , train-err %.5g , time: %f"%(self.epoch, rec_error_test, rec_error_train, t))
                    else:
                        print ("Epoch: %d , time: %f"%(self.epoch, t))

        print('*** Training finished')


    def SGD_update(self, dEdW_data, dEdW_model, dEdv_bias_data, dEdv_bias_model, dEdh_bias_data, dEdh_bias_model, dEds_data, dEds_model):        
        # Gradients 
        dW = -dEdW_data      + dEdW_model
        dv = -dEdv_bias_data + dEdv_bias_model
        dh = -dEdh_bias_data + dEdh_bias_model
        if self.energy_type=='hopfield':
            ds = -dEds_data + dEds_model
        # Update parameters in-place
        # and clip
        if self.energy_type=='hopfield':
            gnorm = torch.norm(dW) + torch.norm(dv) + torch.norm(dh) + torch.norm(ds)
        else:
            gnorm = torch.norm(dW) + torch.norm(dv) + torch.norm(dh)
        myclip = (self.lr*10.) / gnorm if gnorm > 10 else self.lr
        self.W.add_(dW*myclip)
        self.v_bias.add_(dv*myclip)
        self.h_bias.add_(dh*myclip)
        if self.energy_type=='hopfield':
            self.logsigma_sq.add_(ds*myclip)


    
    def Adam_update(self, t, dEdW_data, dEdW_model, dEdv_bias_data, dEdv_bias_model, dEdh_bias_data, dEdh_bias_model, dEds_data, dEds_model):        
        # Gradients 
        dW = -dEdW_data + dEdW_model
        dv = -dEdv_bias_data + dEdv_bias_model
        dh = -dEdh_bias_data + dEdh_bias_model
        ds = -dEds_data + dEds_model
        # Compute betas raised to the power of t
        beta1_t = self.beta1 ** t
        beta2_t = self.beta2 ** t
        # Update momentum terms
        self.m_dW = self.beta1 * self.m_dW + (1 - self.beta1) * dW
        self.m_dv = self.beta1 * self.m_dv + (1 - self.beta1) * dv
        self.m_dh = self.beta1 * self.m_dh + (1 - self.beta1) * dh
        self.m_ds = self.beta1 * self.m_ds + (1 - self.beta1) * ds
        # Update second moments
        self.v_dW = self.beta2 * self.v_dW + (1 - self.beta2) * (dW**2)
        self.v_dv = self.beta2 * self.v_dv + (1 - self.beta2) * (dv**2)
        self.v_dh = self.beta2 * self.v_dh + (1 - self.beta2) * (dh**2)
        self.v_ds = self.beta2 * self.v_ds + (1 - self.beta2) * (ds**2)
        # Bias correction terms
        m_dW_corr = self.m_dW / (1 - beta1_t)
        m_dv_corr = self.m_dv / (1 - beta1_t)
        m_dh_corr = self.m_dh / (1 - beta1_t)
        m_ds_corr = self.m_ds / (1 - beta1_t)
        v_dW_corr = self.v_dW / (1 - beta2_t)
        v_dv_corr = self.v_dv / (1 - beta2_t)
        v_dh_corr = self.v_dh / (1 - beta2_t)
        v_ds_corr = self.v_ds / (1 - beta2_t)
        # Compute the gradients
        gW = m_dW_corr / (torch.sqrt(v_dW_corr) + self.epsilon)
        gv = m_dv_corr / (torch.sqrt(v_dv_corr) + self.epsilon)
        gh = m_dh_corr / (torch.sqrt(v_dh_corr) + self.epsilon)
        gs = m_ds_corr / (torch.sqrt(v_ds_corr) + self.epsilon)
        # Clip and update
        gnorm = torch.norm(gW) + torch.norm(gv) + torch.norm(gh) + torch.norm(gs)
        if gnorm >10:
            myclip = self.lr*10/gnorm
        else:
            myclip = self.lr
        self.W.add_(gW * myclip)
        self.v_bias.add_(gv * myclip)
        self.h_bias.add_(gh * myclip)
        self.logsigma_sq.add_(gs * myclip)

        
    def reconstruct(self, data, k, beta=None):
        if beta is None:
            beta = self.model_beta
        if self.energy_type !='hopfield':
            self.clip_weights()
            self.clip_bias()
            self._update_circuit_variables()
        else:
            self.W_t = self.W.t()
            self.sigma_sq = torch.exp(self.logsigma_sq)
            self.sigma = torch.sqrt(self.sigma_sq)
        data = torch.Tensor(data).to(self.device).to(self.mytype)
        v_model = self.forward(data, k, beta)
        return data.detach().cpu().numpy(), v_model.detach().cpu().numpy()
    
    def generate(self, n_samples, k, h_binarized=True, from_visible=False, beta=None):
        if beta is None:
            beta = self.model_beta
        if self.energy_type !='hopfield':
            self.clip_weights()
            self.clip_bias()
            self._update_circuit_variables()
        else:
            self.W_t = self.W.t()
            self.sigma_sq = torch.exp(self.logsigma_sq)
            self.sigma = torch.sqrt(self.sigma_sq)
        if from_visible:
            #v = torch.randint(high=2, size=(n_samples, self.n_visible), device=self.device, dtype=self.mytype)
            #v = torch.rand(size=(n_samples, self.n_visible), device=self.device, dtype=self.mytype)
            v = torch.randn(size=(n_samples, self.n_visible), device=self.device, dtype=self.mytype)
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
            return self._delta_eh_hopfield(v)
        elif self.energy_type == 'linear_circuit_4':
            return self._delta_eh_linear_circuit_4(v)
            
        
    def delta_ev(self,h):
        if self.energy_type == 'hopfield':
            return self._delta_ev_hopfield(h)
        elif self.energy_type == 'linear_circuit_4':
            return self._delta_ev_linear_circuit_4(h)


    # **** Hopfield transfer functions
    def _delta_eh_hopfield(self, v):
        return torch.mm(v, self.W_t) + self.h_bias
        #return F.linear(v, self.W, bias =self.h_bias)
    def _delta_ev_hopfield(self, h):
        return torch.mm(h, self.W) + self.v_bias
        #return F.linear(h, self.W_t, bias =self.v_bias)
        #return torch.matmul(h, self.W) + self.v_bias


    # **** linear_circuit_4 transfer functions
    def _delta_ev_linear_circuit_4(self, h):
        return torch.mm(torch.mul(h, 2) - 1, self._k_diff) + self._vb_posneg
    def _delta_eh_linear_circuit_4(self, v):
        return torch.mm(torch.mul(v, 2) - 1, self._k_diff_t) + self._hb_posneg


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
        # for the gaussian units
        self.sigma = torch.pow(self._k_pos.sum(0) + self._k_neg.sum(0) + self._v_bias_pos, -0.5) 
        self.sigma_sq = self.sigma*self.sigma

    
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
        v_diff = v - self.v_bias
        v_over_sigma = v/self.sigma_sq

        if self.centering:
            dEdW = -torch.einsum('ij,ik->ijk', h-self.oh, v-self.ov)/self.sigma_sq
        else:
            dEdW = -torch.einsum('ij,ik->ijk', h, v_over_sigma)
        dEdv_bias = -(v_diff)/self.sigma_sq
        dEdh_bias = -h
        #dEds = -( (v-self.v_bias)**2/self.sigma_sq.unsqueeze(0)*0.5 - torch.mm(h,self.W)*v/self.sigma_sq.unsqueeze(0))
        dEds = - 0.5*(v_diff ** 2) / self.sigma_sq + torch.mm(h, self.W) * v_over_sigma
        return dEdW, dEdv_bias, dEdh_bias, dEds
    

    def derivatives_linear_circuit_4(self, v, h):
        v_square = torch.square(v).unsqueeze(1)
        vneg_square = torch.square(1 - v).unsqueeze(1)

        h_square = torch.square(h).unsqueeze(2)
        hneg_square = torch.square(1 - h).unsqueeze(2)
        
        dEdk_pos = (-torch.einsum('ij,ik->ijk', h, v) + 0.5 * v_square + 0.5 * h_square) + (-torch.einsum('ij,ik->ijk', 1 - h, 1 - v) + 0.5 * vneg_square + 0.5 * hneg_square)
        dEdk_neg = (-torch.einsum('ij,ik->ijk', h, 1 - v) + 0.5 * vneg_square + 0.5 * h_square) + (-torch.einsum('ij,ik->ijk', 1 - h, v) + 0.5 * v_square + 0.5 * hneg_square)
        
        dkdw_pos = self.dk_pos().unsqueeze(0)
        dkdw_neg = self.dk_neg().unsqueeze(0)
        
        dEdW = dEdk_pos * dkdw_pos + dEdk_neg * dkdw_neg
        
        dEdv_bias_pos = -self.ground_v * v + 0.5 * torch.square(v)
        dEdv_bias_neg = -self.ground_v * (1 - v) + 0.5 * torch.square(1 - v)
        
        dv_biasdv_pos = self.dv_bias_pos().unsqueeze(0)
        dv_biasdv_neg = self.dv_bias_neg().unsqueeze(0)
        
        dEdv_bias = dEdv_bias_pos * dv_biasdv_pos + dEdv_bias_neg * dv_biasdv_neg
        dEdh_bias_pos = -self.ground_h * h + 0.5 * torch.square(h)
        dEdh_bias_neg = -self.ground_h * (1 - h) + 0.5 * torch.square(1-h)
        
        dh_biasdh_pos = self.dh_bias_pos().unsqueeze(0)
        dh_biasdh_neg = self.dh_bias_neg().unsqueeze(0)
        dEdh_bias = dEdh_bias_pos * dh_biasdh_pos + dEdh_bias_neg * dh_biasdh_neg
        
        return dEdW, dEdv_bias, dEdh_bias, None


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