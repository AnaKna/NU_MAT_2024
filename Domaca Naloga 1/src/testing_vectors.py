import numpy as np
from tabulate import tabulate
from QR_decomposition_Givens_rotations import QR_Decomposition_using_Givens_Rotations
from QR_decomposition_Gram_Schmidt import Gram_Schmidt_QR_decomposition
import numpy as np
from numpy.linalg import svd

# A is a square random matrix of size n
n = 3
A = np.random.rand(n, n)
print("A=")
print(tabulate(A))

def eigen_qr_simple(A, iterations=50000):
    Ak = np.copy(A)
    n = A.shape[0]
    QQ = np.eye(n)
    for k in range(iterations):
        Q, R, givens = QR_Decomposition_using_Givens_Rotations(Ak)
        Ak = R.matrika @ Q
        QQ = QQ @ Q
        # we "peek" into the structure of matrix A from time to time
        # to see how it looks
        if k%10000 == 0:
            print("A",k,"=")
            print(tabulate(Ak))
            print("\n")
    return Ak, QQ



# We call the function    
values_matrix, qq = eigen_qr_simple(A)

values_vector = np.zeros(len(A))

for i in range (0, len(A)):
    values_vector[i] = values_matrix[i][i]

values_matrix = np.zeros((len(A),len(A)))
for i in range (0, len(A)):
    values_matrix[i][i] = values_vector[i]


# We compare our results with the official numpy algorithm
print(np.linalg.eigvals(A))


val, vec = np.linalg.eig(A)


print("\n")
print("\n")
print("TEST NP:")
print(A@vec)
print("")
print(val*vec)



