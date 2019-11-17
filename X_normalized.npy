"""
Normalization is one of the most basic preprocessing techniques in data 
analytics. In this problem, create a random 5x5 ndarray and store it to 
variable X. Normalize X. Save your normalized ndarray as X_normalized.npy
"""

import numpy as np

X = np.random.random((5,5))
print('\n')
print('Random Array: \n')
print(X)
print('\n')

mean = np.mean(X)
SD = np.std(X)

centering = np.subtract(X, mean)
scaling = np.divide(centering, SD)

print('Norm: \n')
print(scaling)
