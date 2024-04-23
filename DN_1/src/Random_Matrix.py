import sys
sys.path.append('.')
import numpy as np
from DN_1.src.Data_type import SimetricnaTridiagonalna

def random_symmetric_tridiagonal(n):
    """
    Generacija simetrične tridiagonalne matrike v velikosti nxn

    Return: SimetricnaTridiagonalna
    """
    # Generate random values for the main diagonal
    main_diag = np.random.rand(n)
    
    # Generate random values for the upper and lower diagonals
    off_diag = np.random.rand(n-1)
    
    # Create the symmetric tridiagonal matrix
    #matrix = np.diag(main_diag) + np.diag(off_diag, k=1) + np.diag(off_diag, k=-1)
    matrix = SimetricnaTridiagonalna(main_diag,off_diag)
    return matrix

#
#def random_matrix(N):
#    return np.random.rand(N, N)






"""
matrika = random_symmetric_tridiagonal(5)
id = np.identity(5)
matrika_np = np.array(matrika.matrix)
print(matrika*id)
print("")
print(matrika@id)
print("")
print("")
print("")
print(matrika_np*id)
print("")
print(matrika_np@id)
"""
