import numpy as np
import sys
from tabulate import tabulate
sys.path.append('.')
from DN_1.src.QR_decomposition_Givens_rotations import QR_Decomposition_using_Givens_Rotations
from DN_1.src.QR_decomposition_Gram_Schmidt import Gram_Schmidt_QR_decomposition


#np.set_printoptions(precision=5, suppress=True)


def Eigenvalues_Eigenvectors_Givens(A, iterations=80000):
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
        
    Eigenvalues = Ak
    Eigenvectors = QQ
    return Eigenvalues, Eigenvectors



def Eigenvalues_Eigenvectors_Gram_Schmidt(A, iterations=80000):
    Ak = np.copy(A)
    n = len(A)
    QQ = np.identity(n)
    for k in range(iterations):
        Q, R = Gram_Schmidt_QR_decomposition(Ak)
        Ak = R @ Q
        QQ = QQ@Q
        # we "peek" into the structure of matrix A from time to time
        # to see how it looks
        
        if k%10000 == 0:
            print("A",k,"=")
            print(tabulate(Ak))
            print("\n")
        
    Eigenvalues = Ak
    Eigenvectors = QQ
    return Eigenvalues, Eigenvectors


"""
n = 3
A = random_symmetric_tridiagonal(n)
givenc_val,givenc_Vec = Eigenvalues_Eigenvectors_Givens(A)
gram_val,gram_Vec = Eigenvalues_Eigenvectors_Gram_Schmidt(A)
np_val,no_vec = np.linalg.eig(A)

print("Izračunani eigevalues Givens:")
print(givenc_val)
print("")
print("Izračunani eigevectors Givens:")
print(givenc_Vec)
print("")

print("Izračunani eigevalues Gram-Schmidt:")
print(gram_val)
print("")
print("Izračunani eigevectors Gram-Schmidt:")
print(gram_Vec)
print("")

print("Izračunani eigevalues  Numpy:")
print(np_val)
print("")
print("Izračunani eigevectors Numpy:")
print(no_vec)
"""