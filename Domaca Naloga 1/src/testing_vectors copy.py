import numpy as np
from tabulate import tabulate
from QR_decomposition_Givens_rotations import QR_Decomposition_using_Givens_Rotations
from QR_decomposition_Gram_Schmidt import Gram_Schmidt_QR_decomposition
import numpy as n
from sympy import Symbol, symbols, solve, Matrix

# A is a square random matrix of size n

"""
n = 3
A = np.random.rand(n, n)
print("A=")
print(tabulate(A))
"""

def eigen_qr_simple(A, iterations=50000):
    Ak = np.copy(A)
    n = len(A)
    QQ = np.identity(n)
    for k in range(iterations):
        Q, R, givens = QR_Decomposition_using_Givens_Rotations(Ak)
        Ak = R.matrika @ Q
        QQ = QQ@Q
        # we "peek" into the structure of matrix A from time to time
        # to see how it looks
        if k%10000 == 0:
            print("A",k,"=")
            print(tabulate(Ak))
            print("\n")
    return Ak, QQ



A = np.array([[1,2,1],
              [2,-3,1],
              [1,1,-3]])


"""
# We call the function    
values_matrix, qq = eigen_qr_simple(A)
values_vector = np.zeros(len(A))
for i in range (0, len(A)):
    values_vector[i] = values_matrix[i][i]
values_matrix = np.zeros((len(A),len(A)))
for i in range (0, len(A)):
    values_matrix[i][i] = values_vector[i]

val, vec = np.linalg.eig(A)
a_vector = np.zeros(len(A))
for i in range (0,len(A)):
    a_vector[i] = qq[i][0]

"""

"""

#Q,R,rot = QR_Decomposition_using_Givens_Rotations(A)
Q,R,rot = QR_Decomposition_using_Givens_Rotations(A)

print(rot)

QQ,RR = np.linalg.qr(A)
print("Q MATRIX:")
print(Q)
print("\nR MATRIX:")
print(R)

print("\nTRUE Q MATRIX:")
print(QQ)
print("\nTRUE R MATRIX:")
print(RR)

print("\nA:")
print(Q@R.matrika)
print("\nA F:")
print(QQ@RR)
"""


values_matrix, qq = eigen_qr_simple(A)
val, vec = np.linalg.eig(A)
print("\nVECTOR TRUE")
print(vec)
print("")
print(qq)



# Example usage
n = 5  # Size of the matrix
random_matrix = random_symmetric_tridiagonal(n)
print("Random symmetric tridiagonal matrix:")
print(random_matrix)

