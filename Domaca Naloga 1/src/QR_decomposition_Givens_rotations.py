from math import hypot
import numpy as np
from Data_type import Givens
from Data_type import ZgornjaDvodiagonalna

def QR_Decomposition_using_Givens_Rotations(matrix):

    # Zagotovimo, da je matrika oblike np.array()
    matrix = np.array(matrix)
    (num_rows, num_cols) = np.shape(matrix)
    

    # Določimo matriko Q kot enotsko matriko -> R = Q * G.T = G.T
    Q = np.identity(num_rows)
    Q_givens_rotations = []
    Q_givens_index = []
    # Določimo matriko R kot kopijo osnovne matrike
    R = matrix

    # Določimo elemente spodnje trikotne matrike brez diagonale
    (rows, cols) = np.tril_indices(num_rows, -1, num_cols)
    print("ROWS and COLS")
    print((rows, cols))

    for (row, col) in zip(rows, cols):
        # Givensove rotacije izvedemo samo za ne-ničelne elemnte
        if R[row, col] != 0:
            # (c, s) = Givens_Rotation_Matrix_Entries(R[0, 0], R[1, 0])
            (c, s) = Givens_Rotation(R[col, col], R[row, col])
            rotation = [c, s]
            index = [row,col]
            Q_givens_rotations.append(rotation)
            Q_givens_index.append(index)
            #print(Q_givens_rotations)
            #print(Q_givens_index)
            #print("\n")
            # Ustvarimo enotsko matriko G - matrika givensovih rotacij ima diagonalne elemnte enake 1 ali cos
            G = np.identity(num_rows)

            # Elementom na diagonali dodamo vrednost cos
            G[col][col] = c
            G[row][row] = c
            
            # Elementom na sekundarni diagonali dodamo vrednost sin oz. -sin
            G[row, col] = s
            G[col, row] = -s

            #print("MATRIKA G: \n" )
            #print(G)

            # Matrika Q_T = Gn * ... * G3 * G2 * G1 
            # Matrika Q = Gn_T* ... + G3_T * G2_T * G1_T 
            Q = np.dot(Q, G.T)
            
            #print("MATRIKA po množenju")
            #print(matrix@G)

            # Matrika R = Gn * ... * G3 * G2 * G1 * osnovn matrika
            # Matrika R = Q_T * osnovna matrika
            R = np.dot(Q.T, matrix)

    R = ZgornjaDvodiagonalna(R)
    Givnes_data = Givens(Q_givens_rotations,Q_givens_index)
    return (Q, R, Givnes_data)



# Računanje Givensovih elementov
def Givens_Rotation(a, b):
    r = hypot(a, b)
    c = a/r
    s = -b/r

    return (c, s)


"""
np.set_printoptions(precision=5, suppress=True)

# Input matrix
A = [[3, 1, 0, 0], 
     [1, -1, 2, 0],
     [0, 2, 1, 1],
     [0, 0, 1, 1]]

# Print input matrix
print('The A matrix is equal to:\n',A)
# Compute QR decomposition using Givens rotation
(Q, R) = QR_Decomposition_using_Givens_Rotations(A)

# Print orthogonal matrix Q
print('\n The Q matrix is equal to:\n',Q)

# Print upper triangular matrix R
print('\n The R matrix is equal to:\n',R)

# Print upper triangular matrix R
print('\n The Q*R matrix is equal to:\n',Q@R)

"""