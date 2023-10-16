from tqdm import tqdm
import numpy as np
from scipy import interpolate
from sklearn.preprocessing import RobustScaler

from datetime import datetime
import time

from multiprocessing import Pool
import psutil
from os.path import join
from os import makedirs
import argparse
import pickle

def parallelize_processing(tab, func, verbose, n_process=len(psutil.Process().cpu_affinity())):
    """
        This function is a wrapper to compute the function (func) in parallel on the provided input (tab)
            tab : (list)
            func : (function)
            verbose : (boolean) 
            n_process : (int) the number used to split the tab list of argument, default is len(psutil.Process().cpu_affinity())
    """
    if verbose:
        print("Starting", n_process, "processus ...")
    tab_split = np.array_split(tab, n_process)
    pool = Pool(n_process)
    resout = pool.map(func, tab_split)
    pool.close()
    pool.join()
    return resout


def get_opposed_ecdf(data, right=True):
    """
        Function to compute (1 - Empirical CDF) from the provided data ("Opposed ECDF")
            data : (array) data to compute the Empirical CDF
            right : (boolean) decides on which side the CDf is computed, default is True (right)
    """
    nval = data.shape[0]
    dist = data
    np.sort(dist)
    values, counts = np.unique(dist, return_counts=True)
    x = values
    if right:
        y = np.cumsum(counts[::-1])[::-1]/nval
    else:
        y = np.cumsum(counts[::])[::]/nval
    return x, y, values, counts

def findx(x, y, val2find):
    """
        Return the x-value corresponding to the y-value to find (val2find) from the x and y points that are provided
            x : (array) x-axis data
            y : (array) y-axis data
            val2find : (array) y-value for which we want to find the x-value
    """
    f = interpolate.interp1d(y, x, fill_value='extrapolate')
    x_corresp = f(val2find)
    return x_corresp

def get_pvalues_dimension(obs, dim, side):
    """
        This function returns the P(obs => X) or P(obs <= X) depending on the side argument from the observation and dimension
            obs : (float) value of the observation
            dim : (int) integer representing the dimension for which we want the probability
            side : (str) "left" or "right" depending on the probability that is expected 
    """

    # import global variable which contain normal reconstruction error dimensions
    global normal_data_distributions_left, normal_data_distributions_right 

    if side=="left":
        benignDataDistributions = normal_data_distributions_left
    elif side=="right":
        benignDataDistributions = normal_data_distributions_right
    else:
        assert side in ["left", "right"], 'side argument must be "left" or "right"'

    # Get the corresponding 1-cdf(x) curve
    x, y = benignDataDistributions[dim]
    
    # Find p-value of corresponding observation
    if len(x) > 1:
        # If we have several observations we can compute the discrete pvalue
        pvalue = max(0,findx(y, x, obs))
    else:
        # If we have a single observation in the normal distribution then we can compute the discrete pvalue by checking if the value was existing or not.
        if obs in x:
            pvalue = 1
        else:
            pvalue = 0
    return pvalue

def get_pvalues_vector(vecerror):
    """
        This function computes the pvalues for each of the components of the vector.
        It computes both the P(obs => X) and P(obs <= X) probabilities to used later
            vecerror : (array) one reconstruction error vector of the vector to explain
    """
    ndim = vecerror.shape[0]
    vecP_left = np.ones(ndim)
    vecP_right = np.ones(ndim)
    for i in range(ndim):
        vecP_left[i] = get_pvalues_dimension(obs=vecerror[i], dim=i, side="left")
        vecP_right[i] = get_pvalues_dimension(obs=vecerror[i], dim=i, side="right")
    # saturate pvalues between 0 and 1
    np.clip(vecP_left, 0, 1, out=vecP_left)
    np.clip(vecP_right, 0, 1, out=vecP_right)
    return vecP_left, vecP_right


def compute_pvalues_on_batch(batch):
    """
        This function computes sequentially the pvalues for the provided inputs
            batch : (array) the batch of the vectors to explain
    """
    # Initialize output vector
    result = np.ones(batch.shape)
    for i, elt in enumerate(batch):
        # For each vector compute the P(obs => X) and P(obs <= X) in the discrete case
        vecP_left, vecP_right = get_pvalues_vector(elt)
        # The final pvalue is the minimum between the two previous pvalues
        result[i] = np.minimum.reduce([vecP_left, vecP_right])
    return result


def compute_pvalues(recerror, verbose):
    """
        This function is a wrapper to compute the pvalues of the inputs in parallel and aggregates the results 
            recerror : (array) reconstruction errors of the vectors to explain
            verbose : (boolean) if True it provides more information on the processing
    """
    # Compute pvalues in parallel
    res = parallelize_processing(recerror, compute_pvalues_on_batch, verbose=verbose)
    # Aggregate results
    pvalues = np.concatenate([*res])
    return pvalues


def ae_pvalues(model, normal_data, data_to_explain, output_folder=".", verbose=False):
    """
        This function computes the pvalues per dimensions to provide explanations
            model : any autoencoder model
            normal_data : (array) data (as float32)
            data_to_explain : (array) data (as float32)
            output_folder : (str) output folder to store the benign distributions
            verbose : (boolean) if True it provides more information on the processing
    """

    # Some verifications
    ## Check data validity
    assert normal_data.shape[1] == data_to_explain.shape[1]

    ## Autoencode normal data
    reconstructed_normal_data = model(normal_data)

    # Autoencode data to explain
    reconstructed_data_to_explain = model(data_to_explain)

    # Compute the explanations using the pvalues
    return ae_pvalues_no_model(normal_data, reconstructed_normal_data, data_to_explain, reconstructed_data_to_explain, output_folder=output_folder, verbose=verbose)


def ae_pvalues_no_model(normal_data, reconstructed_normal_data, data_to_explain, reconstructed_data_to_explain, output_folder=".", verbose=False):
    """
        This function computes the pvalues per dimensions to provide explanations
            normal_data : (array) data (as float32)
            reconstructed_normal_data : (array) reconstructed data (passed through an autoencoder) (as float32)
            data_to_explain : (array) data (as float32)
            reconstructed_data_to_explain : (array) reconstructed data (passed through an autoencoder) (as float32)
            output_folder : (str) output folder to store the benign distributions
            verbose : (boolean) if True it provides more information on the processing
    """

    # Some verifications
    ## Check data validity
    assert normal_data.shape[1] == data_to_explain.shape[1] == reconstructed_normal_data.shape[1] == reconstructed_data_to_explain.shape[1]

    # Initialisation
    dim_vec = normal_data.shape[1]

    # Compute reconstruction error 
    recerror = (reconstructed_normal_data - normal_data)

    # init normal dist
    global normal_data_distributions_left, normal_data_distributions_right
    normal_data_distributions_left, normal_data_distributions_right = list(), list()

    t0 = time.time()
    # Get normal distributions
    if verbose:
        iterator = tqdm(range(dim_vec))
    else:
        iterator = (range(dim_vec))

    for i in iterator:
        x, y, _, _ = get_opposed_ecdf(recerror[:, i], right=False)
        normal_data_distributions_left.append([x, y])
        x, y, _, _ = get_opposed_ecdf(recerror[:, i], right=True)
        normal_data_distributions_right.append([x, y])
    t1 = time.time()

    if verbose:
        print("Generation benign distributions :", t1-t0, "secondes for", len(recerror), "samples, that is :", (t1-t0)/len(recerror), "secondes per sample")

    ## Save normal distributions
    with open(join(output_folder, "normal_data_distributions_left.pkls"), "wb") as fp:   #Pickling
        pickle.dump(normal_data_distributions_left, fp)
    with open(join(output_folder, "normal_data_distributions_right.pkls"), "wb") as fp:   #Pickling
        pickle.dump(normal_data_distributions_right, fp)

    if verbose:
        print("[*] Distributions calculated !")
        print("[*] Start computing pvalues !")

    #####################
    ## Compute PVALUES ##
    #####################
    
    # Clear objects
    del normal_data, reconstructed_normal_data, recerror

    # Compute reconstruction error 
    recerror = (reconstructed_data_to_explain - data_to_explain)

    t0 = time.time()
    pvalues = compute_pvalues(recerror, verbose)


    # Compute alpha scores of the reconstruction error using the robust scaler
    robust_scaler = RobustScaler(quantile_range=(1, 99))
    robust_scaler.fit(recerror)
    alpha_scores = np.abs(robust_scaler.transform(recerror))

    # Export features scores
    dimensions_abnormal_order = np.lexsort((alpha_scores, 1-pvalues))[::, ::-1]

    t1 = time.time()
    if verbose:
        print("Pvalues computation :", t1-t0, "secondes for", len(pvalues), "samples, that is :", (t1-t0)/len(pvalues), "secondes per sample")

    return dimensions_abnormal_order, pvalues


def main():
    """
        This function allows the user to use the ae-pvalues function directly from command line
            normal_data : (array) data (as float32)
            reconstructed_normal_data : (array) reconstructed data (passed through an autoencoder) (as float32)
            data_to_explain : (array) data (as float32)
            reconstructed_data_to_explain : (array) reconstructed data (passed through an autoencoder) (as float32)
            -o output_folder : (str) output folder to store the benign distributions
            verbose : (boolean) if True it provides more information on the processing
    """

    # Argument handler
    parser = argparse.ArgumentParser()    
    parser.add_argument("normal_data",  help="Data containing only the normal class")
    parser.add_argument("reconstructed_normal_data",  help="Reconstructed data to be explained (output of the autoencoder on the normal_data)")
    parser.add_argument("data_to_explain",  help="Data to be explained")
    parser.add_argument("reconstructed_data_to_explain",  help="Reconstructed data to be explained (output of the autoencoder on the data_to_explain)")
    parser.add_argument("-o",  help="Output folder", default=".")
    parser.add_argument("-v", help="verbose mode", action="store_true")
    args = parser.parse_args()

    # Create output folder if it doesn't exist
    makedirs(args.o, exist_ok=True)

    # Load model and Data
    normal_data = np.load(args.normal_data)
    reconstructed_normal_data = np.load(args.reconstructed_normal_data)
    data_to_explain = np.load(args.data_to_explain)
    reconstructed_data_to_explain = np.load(args.reconstructed_data_to_explain)

    if args.v:
        print("[*] Data Loaded.")
    
        print("[ ] Start pvalues computation ...")

    # Compute explanations using ae-pvalues
    dimensions_abnormal_order, pvalues = ae_pvalues_no_model(normal_data, reconstructed_normal_data, data_to_explain, reconstructed_data_to_explain, output_folder=args.o)

    if args.v:
        print("[*] Computations finished, saving ...")
    
    # Save outputs to files
    np.save(join(args.o, "dimensions_abnormal_order.npy"), dimensions_abnormal_order)
    np.save(join(args.o, "dimensions_abnormal_pvalues.npy"), pvalues)

    if args.v:
        print("[*] Terminated !")

if __name__ == "__main__":
    main()
