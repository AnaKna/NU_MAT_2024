from math import hypot
import numpy as np
import sys
sys.path.append('.')
from DN_1.src.Data_type import ZgornjaDvodiagonalna
from DN_1.src.Data_type import Givens
from DN_1.src.Data_type import SimetricnaTridiagonalna


def QR_Decomposition_using_Givens_Rotations(matrix):

    (num_rows, num_cols) = np.shape(matrix)
    

    # Določimo matriko Q kot enotsko matriko -> R = Q * G.T = G.T
    Q = np.identity(num_rows)
    Q_givens_rotations = []
    Q_givens_index = []
    # Določimo matriko R kot kopijo osnovne matrike
    R = np.copy(matrix)

    # Določimo elemente spodnje trikotne matrike brez diagonale
    (rows, cols) = np.tril_indices(num_rows, -1, num_cols)

    for (row, col) in zip(rows, cols):
        # Givensove rotacije izvedemo samo za ne-ničelne elemnte
        if R[row, col] != 0:
            (c, s) = Givens_Rotation(R[col, col], R[row, col])
            rotation = [c, s]
            index = [row,col]
            Q_givens_rotations.append(rotation)
            Q_givens_index.append(index)
            # Ustvarimo enotsko matriko G - matrika givensovih rotacij ima diagonalne elemnte enake 1 ali cos
            G = np.identity(num_rows)

            # Elementom na diagonali dodamo vrednost cos
            G[col][col] = c
            G[row][row] = c
            
            # Elementom na sekundarni diagonali dodamo vrednost sin oz. -sin
            G[row, col] = s
            G[col, row] = -s

            # Matrika Q_T = Gn * ... * G3 * G2 * G1 
            # Matrika Q = Gn_T* ... + G3_T * G2_T * G1_T 
            Q = np.dot(Q, G.T)
        
            # Matrika R = Gn * ... * G3 * G2 * G1 * osnovn matrika
            # Matrika R = Q_T * osnovna matrika
            R = np.dot(Q.T, matrix)

    R = ZgornjaDvodiagonalna(R)
    Q_givens = Givens(Q_givens_rotations,Q_givens_index)
    return (Q, R, Q_givens)



# Računanje Givensovih elementov
def Givens_Rotation(a, b):
    r = hypot(a, b)
    c = a/r
    s = -b/r
    return (c, s)
