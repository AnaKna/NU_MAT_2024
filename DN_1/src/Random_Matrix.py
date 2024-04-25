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
    matrix = SimetricnaTridiagonalna(main_diag,off_diag)
    return matrix

