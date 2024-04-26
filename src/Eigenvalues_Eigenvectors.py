import numpy as np
import sys
from tabulate import tabulate
sys.path.append('.')
from src.QR_decomposition_Givens_rotations import QR_Decomposition_using_Givens_Rotations
from src.QR_decomposition_Gram_Schmidt import Gram_Schmidt_QR_decomposition



def Eigenvalues_Eigenvectors_Givens(A, iterations, show):
    Ak = np.copy(A)
    n = len(A)
    QQ = np.identity(n)
    for k in range(iterations):
        # Za izračun lastnih vrednosit in vektorjev uporabimo že obstoječo funkcijo za iračun QR razcepa z Givesovimi rotacijami
        Q, R, givens = QR_Decomposition_using_Givens_Rotations(Ak)
        # V vsaki iteraciji popravimo vredsnoti Ak z novo izračunanimi matrikamo Q in R
        Ak = R @ Q
        QQ = QQ@Q

        # Vpogled v spreminjanje lastnih vrednosti po vsakih 500. iteraciji
        if show == True:
            if k%500 == 0:
                print("A",k,"=")
                print(tabulate(Ak))
                print("\n")
        
    Eigenvalues = Ak
    Eigenvectors = QQ
    return Eigenvalues, Eigenvectors



# Dodatna implementacija izračuna lastnih vrednsoti in vektorjev z Gram-Schmidt metodo QR razcepa 
def Eigenvalues_Eigenvectors_Gram_Schmidt(A, iterations, show):
    Ak = np.copy(A)
    n = len(A)
    QQ = np.identity(n)
    for k in range(iterations):
        Q, R = Gram_Schmidt_QR_decomposition(Ak)
        Ak = R @ Q
        QQ = QQ@Q
        # we "peek" into the structure of matrix A from time to time
        # to see how it looks
        
        if show == True:
            if k%500 == 0:
                print("A",k,"=")
                print(tabulate(Ak))
                print("\n")
        
    Eigenvalues = Ak
    Eigenvectors = QQ
    return Eigenvalues, Eigenvectors
