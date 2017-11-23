# Use python 3

import sys
import numpy as np

matrixA = np.loadtxt("matrixA.txt", dtype='i', delimiter=',')
print(matrixA)

matrixB = np.loadtxt("matrixB.txt", dtype='i', delimiter=',')
print(matrixB)