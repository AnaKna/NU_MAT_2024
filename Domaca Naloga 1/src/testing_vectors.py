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

def eigen_qr_simple(A, iterations=10000):
    Ak = np.copy(A)
    n = len(A)
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



A = np.array([[1,2,0],
              [2,3,1],
              [0,1,3]])

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

print("\nVALUES:")
print(values_vector)
print("\nTRUE VALUES:")
print(np.linalg.eigvals(A))


print("\nFIRST VECTOR CALCUALTED")
print(a_vector)
print("\nVECTOR TRUE")
print(vec)

print("\nDETERMINANTA")
print(np.linalg.det(A-np.eye(len(A))*values_vector))
print("\n")

print("CALCUALTION OF A*Vec=Val*Vec")
print("A*Vec\n")
#print(A*a_vector)
print(A@a_vector)

print("\nVel*Vec\n")
print(values_vector[0]*a_vector)
#print(values_vector[0]@a_vector)

Vb1 = Symbol('Vb1')
Vb2 = Symbol('Vb2')
Vb3 = Symbol('Vb3')
b_vector = Matrix([Vb1,Vb2,Vb3])
solution = solve(A@b_vector-values_vector[1]*b_vector)
print(solution)
