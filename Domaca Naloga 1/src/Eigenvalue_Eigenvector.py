import numpy as np
from numpy.linalg import eig


def Eigenvalue_Eigenvector(matrika):
    value,vector=eig(matrika)
    return (value,vector)