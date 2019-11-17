import numpy as np

B = np.arange(1,101,1)
A = (B.reshape(10,10))**2

C = A[A%3 == 0]
C_conv = C.astype(int)

print('\n')
print('Divisible by 3: \n')
print(C)