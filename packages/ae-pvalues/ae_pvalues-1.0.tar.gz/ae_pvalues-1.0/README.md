# AE-pvalues

This is the implementation of _AE-pvalues_ proposed in the paper _Towards Understanding Alerts raised by Unsupervised Network Intrusion Detection Systems, RAID2023_ (https://doi.org/10.1145/3607199.3607247).
The method allows you to obtain explanations of the anomalies identified by an auto-encoder (AE).


## Authors

- [@mlanvin](https://gitlab.inria.fr/mlanvin)


## Installation


### Pip Installation

You can install it through pip

```bash
  pip install ae-pvalues
```


## Usage/Examples


```python
from ae_pvalues import ae_pvalues

model = # Any autoencoder

x_train = np.load("./demo/example/x_train.npy") # Normal data
x_test = np.load("./demo/example/x_test.npy") # Data to explain

order, pvalues = ae_pvalues(model, normal_data=x_train, data_to_explain=x_test)

```

If you installed the module then you can use ae-pvalues directly from the command line : 

```bash 
ae-pvalues -v ./demo/example/x_train.npy ./demo/example/rec_x_train.npy ./demo/example/x_test.npy ./demo/example/rec_x_test.npy -o outputs
```

`-v` : verbose mode

`-o` : output folder


This produces two output files namely:

* dimensions_abnormal_order.npy : order of dimension by abnormality
* dimensions_abnormal_pvalues.npy : raw pvalue scores


## Demo

A notebook is available in the demo folder to show an example of use.
Please note that the notebook requires the following dependencies : 

- scikit-learn
- tensorflow
- seaborn
- plotly

which can be installed with pip using the following comand line :
```bash
python3 -m pip install scikit-learn tensorflow seaborn plotly
```
