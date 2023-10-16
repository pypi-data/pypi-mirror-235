import numpy as np
import math
import sys
import time
import matplotlib.pyplot as plt
import pickle
import os
import glob
import torch
import torch.fft as fft
import torch
import gzip
import io



def load_model(name, delete_previous=False):
    # Check if you have model load points
    filename_list = glob.glob('model_states/{}_t*.pkl'.format(name))
    if len(filename_list)>0:
        all_loadpoints = sorted([int(x.split('_t')[-1].split('.pkl')[0]) for x in filename_list])
        last_epoch = all_loadpoints[-1]
        print('** Model {} trained up to epoch {}, so I load it'.format(name,last_epoch))
        with open('model_states/{}_t{}.pkl'.format(name,last_epoch), "rb") as file:
            model = pickle.load(file)
        if delete_previous:
            # Remove all the previous loadpoints
            for x in all_loadpoints[:-1]:
                os.remove('model_states/{}_t{}.pkl'.format(name,x))
        return True, model
    else:
        print('** No load points for {}'.format(name))
        return False, []

def show_and_save(file_name,img, cmap='gray', vmin=None, vmax=None, save=False, savename= ''):
    plt.title(file_name)
    plt.imshow(img, cmap=cmap, vmin=vmin, vmax=vmax)
    if save:
        plt.savefig(savename)
        plt.close()
    else:
        plt.show()

def make_grid(array, nrow=8, padding=2):
    N = array.shape[0]
    H = array.shape[1]
    W = array.shape[2]
    grid_h = int(np.ceil(N / float(nrow)))
    grid_w = nrow
    grid = np.zeros([grid_h*(H+padding) + padding, grid_w*(W+padding) + padding])
    k = 0
    for y in range(grid_h):
        for x in range(grid_w):
            if k < N:
                grid[y*(H+padding):y*(H+padding) + H, x*(W+padding):x*(W+padding) + W] = array[k]
                k = k + 1
    return grid

def getbasebias(data):
    """ Returns the maximum likelihood estimate of the visible bias, given the data. If no data is given the RBMs \
        bias value is return, but is highly recommended to pass the data.

    :return: Base bias.
    :rtype: numpy array [1,  input dim]
    """
    save_mean = torch.clip(data.mean(0), 0.00001, 0.99999)
    return (torch.log(save_mean) - torch.log(1.0 - save_mean))


def Covariance_error(centered_data_original,centered_data_model,Nv):
    covariance_matrix_original = torch.matmul(centered_data_original.T, centered_data_original).mean(0) #/ (len(mean_vector)-1)
    covariance_matrix_model    = torch.matmul(centered_data_model.T   , centered_data_model   ).mean(0) #/ (len(mean_vector)-1)
    return torch.pow(covariance_matrix_original-covariance_matrix_model,2).triu().sum()*2/(Nv*(Nv-1))

def Third_moment_error(centered_data_original,centered_data_model,Nv):
    C_ijk_original = torch.einsum('ni,nj,nk->ijk', centered_data_original, centered_data_original, centered_data_original)/centered_data_model.shape[0]
    C_ijk_model    = torch.einsum('ni,nj,nk->ijk', centered_data_model   , centered_data_model   , centered_data_model   )/centered_data_model.shape[0]
    C_ijk = torch.pow(C_ijk_model-C_ijk_original,2)
    sum_ijk = 0.0
    #m = C_ijk.size(0)
    #for i in range(m):
    #    for j in range(i + 1, m):
    #        for k in range(j + 1, m):
    #            sum_ijk += C_ijk[i, j, k]
    #third_moment_error = sum_ijk*6/(len(mean_vector)*(len(mean_vector)-1)*(len(mean_vector)-2))
    upper_triangular = torch.triu(C_ijk, diagonal=1)
    sum_ijk = upper_triangular.sum(dim=(0, 1, 2))
    return sum_ijk * 6 / (Nv * (Nv - 1) * (Nv - 2))

def PowerSpectrum_MSE(v,v_model):
    # Apply 2D FFT to the signal
    signal_fft_original = fft.fft2(v)
    signal_fft_model    = fft.fft2(v_model)
    # Compute the power spectrum
    power_spectrum_original = torch.mean(torch.abs(signal_fft_original)**2,0)
    power_spectrum_model    = torch.mean(torch.abs(signal_fft_model   )**2,0)
    # MSE of the power spectrum
    return torch.mean((torch.log(power_spectrum_original) - torch.log(power_spectrum_model)) ** 2)


def ComputeAATS(v,v_model):
    CONCAT = torch.cat((v,v_model),1)
    dAB = torch.cdist(CONCAT.t(),CONCAT.t())    
    torch.diagonal(dAB).fill_(float('inf'))
    dAB = dAB.cpu().numpy()

    # the next line is use to tranform the matrix into
    #  d_TT d_TF   INTO d_TF- d_TT-  where the minus indicate a reverse order of the columns
    #  d_FT d_FF        d_FT  d_FF
    dAB[:int(dAB.shape[0]/2),:] = dAB[:int(dAB.shape[0]/2),::-1] 
    closest = dAB.argmin(axis=1) 
    n = int(closest.shape[0]/2)

    ninv = 1/n
    correctly_classified = closest>=n   #np.concatenate([(closest[:n] < n), (closest[n:] >= n)])
    AAtruth = (closest[:n] >= n).sum()*ninv  # for a true sample, proba that the closest is in the set of true samples
    AAsyn = (closest[n:] >= n).sum()*ninv  # for a fake sample, proba that the closest is in the set of fake samples

    return AAtruth, AAsyn



# **** Compute FID score
# Generally, if inputting grayscale images into RGB networks, you would just copy the grayscale channel three times. 
# However, it is unclear how FID behaves in this case, as the original Inception network was probably not trained on grayscale images.
# Also, standard FID score uses inception_v3, which is not designed on Mnist, but for larger images of realistic scenes.
# So I use for activation an autoencoder that I have trained previously on MNIST.

def Compute_FID(synthetic_images, real_images):
    device = synthetic_images.device
    batch_size = 64
    dims = 2048

    global inception_model
    try:
        inception_model
    except:
        # Use the following autoencoder for the FID activation
        model_name = 'AE-200000_n2_hs50_SGD_MSE_lr0.01_bs100'
        isloadable, inception_model = load_model(model_name, delete_previous=False)
        if not isloadable:
            print('I need {} in order to calculate FID'.format(model_name))
            sys.exit()


    synthetic_activations = inception_model.encoder(synthetic_images.to(torch.double)).detach().cpu().numpy()
    real_activations = inception_model.encoder(real_images.to(torch.double)).detach().cpu().numpy()

    # Compute mean and covariance
    mu_synthetic = np.mean(synthetic_activations)
    mu_real = np.mean(real_activations)

    #sigma_synthetic = torch.matmul((synthetic_activations - mu_synthetic).t(), synthetic_activations - mu_synthetic) / synthetic_activations.shape[0]
    #sigma_real = torch.matmul((real_activations - mu_real).t(), real_activations - mu_real) / real_activations.shape[0]
    sigma_synthetic = np.cov(synthetic_activations, rowvar=False)
    sigma_real = np.cov(real_activations, rowvar=False)

    # Compute the FID score
    diff = mu_synthetic - mu_real
    #fid_score = torch.sqrt(torch.trace(sigma_synthetic + sigma_real - 2 * torch.sqrt(sigma_synthetic @ sigma_real)))

    # calculate sum squared difference between means
    ssdiff = np.sum((diff)**2.0)
    # calculate sqrt of product between cov
    # Compute eigenvalue decomposition of sigma1.dot(sigma2)
    eigenvalues, eigenvectors = np.linalg.eig(sigma_synthetic.dot(sigma_real))
    # Take the square root of the eigenvalues
    sqrt_eigenvalues = np.sqrt(eigenvalues)
    # Reconstruct the matrix using the square root of eigenvalues and eigenvectors
    covmean = eigenvectors.dot(np.diag(sqrt_eigenvalues)).dot(np.linalg.inv(eigenvectors))

    # calculate score
    fid = ssdiff + np.trace(sigma_synthetic + sigma_real - 2.0 * covmean)
    return fid

def Compute_S(v,v_model):
    v = v.detach().cpu().numpy()
    v_model = v_model.detach().cpu().numpy()
    # define a mixed set for crossentropy
    v_cross = v.copy()
    v_cross[:int(0.5*v_cross.shape[0])] = v_model[:int(0.5*v_cross.shape[0])]

    # Convert the array to bytes
    bytes_io = io.BytesIO()
    np.save(bytes_io, v)
    bytes_src = bytes_io.getvalue()
    np.save(bytes_io, v_cross)
    bytes_cross = bytes_io.getvalue()

    # Compress the bytes using gzip
    compressed_src = gzip.compress(bytes_src)
    compressed_cross = gzip.compress(bytes_cross)

    # Calculate the entropy
    byte_count_src = len(compressed_src)
    byte_count_cross = len(compressed_cross)
    value_counts_src = np.bincount(np.frombuffer(compressed_src, dtype=np.uint8))
    value_counts_cross = np.bincount(np.frombuffer(compressed_cross, dtype=np.uint8))
    probabilities_src = value_counts_src / byte_count_src
    probabilities_cross = value_counts_cross / byte_count_cross
    entropy_src = -np.sum(probabilities_src * np.log2(probabilities_src))
    entropy_cross = -np.sum(probabilities_cross * np.log2(probabilities_cross))

    return entropy_cross/entropy_src - 1


