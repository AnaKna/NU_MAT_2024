import numpy as np

def random_symmetric_tridiagonal(n):
    # Generate random values for the main diagonal
    main_diag = np.random.rand(n)
    
    # Generate random values for the upper and lower diagonals
    off_diag = np.random.rand(n-1)
    
    # Create the symmetric tridiagonal matrix
    matrix = np.diag(main_diag) + np.diag(off_diag, k=1) + np.diag(off_diag, k=-1)
    
    return matrix


def random_matrix(N):
    return np.random.rand(N, N)