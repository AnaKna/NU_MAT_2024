import numpy as np
from tabulate import tabulate
from QR_decomposition_Givens_rotations import QR_Decomposition_using_Givens_Rotations
from QR_decomposition_Gram_Schmidt import Gram_Schmidt_QR_decomposition


def Eigenvalues_Eigenvectors_Givens(A, iterations=50000):
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



def Eigenvalues_Eigenvectors_Gram_Schmidt(A, iterations=50000):
    Ak = np.copy(A)
    n = len(A)
    QQ = np.identity(n)
    for k in range(iterations):
        Q, R = Gram_Schmidt_QR_decomposition(Ak)
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
