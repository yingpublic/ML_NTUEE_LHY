# Use python 3

import sys
import numpy as np

matrixA = np.loadtxt("matrixA.txt", dtype='i', delimiter=',')
# print(matrixA)

matrixB = np.loadtxt("matrixB.txt", dtype='i', delimiter=',')
# print(matrixB)

# ans = np.matmul(matrixA,matrixB)
ans = np.dot(matrixA,matrixB)
#print(ans)

#ans2 = sorted(ans)
#print(ans2)

ans.sort()
#print(ans)
print(*ans, sep="\n")
sys.stdout=open("ans_one.txt","w")
print(*ans, sep="\n")
sys.stdout.close()
