from math import hypot
import numpy as np
import sys
sys.path.append('.')
from DN_1.src.Data_type import ZgornjaDvodiagonalna
from DN_1.src.Data_type import Givens
from DN_1.src.Random_Matrix import random_matrix,random_symmetric_tridiagonal
from DN_1.src.QR_decomposition_Givens_rotations import QR_Decomposition_using_Givens_Rotations

def QR_Decomposition_Givens_OPT(matrix):
    num_rows, num_cols = matrix.shape
    
    Q = np.identity(num_rows)
    R = matrix.copy()  # Create a copy of the input matrix
    Q_givens_rotations = []
    Q_givens_index = []
    
    # Iterate over the lower triangular part of the matrix
    for col in range(num_cols):
        for row in range(col + 1, num_rows):
            a, b = R[col, col], R[row, col]
            if b != 0:
                r = hypot(a, b)
                c, s = a / r, -b / r
                
                # Update Q and R matrices
                G = np.identity(num_rows)
                G[[col, row], [col, row]] = c
                G[row, col], G[col, row] = s, -s
                Q = np.dot(Q, G.T)
                R = np.dot(G, R)
                
                # Store Givens rotation parameters and indices
                Q_givens_rotations.append([c, s])
                Q_givens_index.append([row, col])
    
    R = ZgornjaDvodiagonalna(R)
    Q_givens = Givens(Q_givens_rotations, Q_givens_index)
    return Q, R, Q_givens




A = random_symmetric_tridiagonal(3)
Q,R,rot = QR_Decomposition_using_Givens_Rotations(A)
Q_opt,R_opt,rot_opt = QR_Decomposition_Givens_OPT(A)
Q_np,R_np = np.linalg.qr(A)


print(Q)
print("")
print(Q_np)
print("")
print(Q_opt)


print("")
print(rot)
print("")
print(rot_opt)
