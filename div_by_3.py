"""
Create the following 10x10 ndarray, which is the squares of the first 100
positive integers. From this ndarray, determine all the elements that are
divisible by 3. Save the result as div_by_3.npy
"""

import numpy as np

B = np.arange(1,101,1)
A = (B.reshape(10,10))**2

C = A[A%3 == 0]
C_conv = C.astype(int)

print('\n')
print('Divisible by 3: \n')
print(C)
