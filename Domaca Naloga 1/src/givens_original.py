#########   Givens rotation module   ############

from math import copysign, hypot

import numpy as np

#########   Perform QR decomposition using Givens rotation   ############

def givens_rotation(A):

    (num_rows, num_cols) = np.shape(A)
    
    # Initialize Q,R
    # Q = orthogonal matrix
    # R =  upper triangular matrix
    Q = np.identity(num_rows)
    R = np.copy(A)

    # Iterate over lower triangular matrix.
    (rows, cols) = np.tril_indices(num_rows, -1, num_cols)
    print(rows, cols)
    for (row, col) in zip(rows, cols):

        # Compute Givens rotation matrix and
        # zero-out lower triangular matrix entries.
        if R[row, col] != 0:
            (c, s) = Givens_Rotation_Matrix_Entries(R[col, col], R[row, col])

            G = np.identity(num_rows)
            G[[col, row], [col, row]] = c
            G[row, col] = s
            G[col, row] = -s

            R = np.dot(G, R)
            Q = np.dot(Q, G.T)

    return (Q, R)


##### Compute matrix entries for Givens rotation. #####

def Givens_Rotation_Matrix_Entries(a, b):
    r = hypot(a, b)
    c = a/r
    s = -b/r

    return (c, s)