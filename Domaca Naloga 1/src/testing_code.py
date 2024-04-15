import numpy as np
from QR_decomposition_Gram_Schmidt import Gram_Schmidt_QR_decomposition
from QR_decomposition_Givens_rotations import QR_Decomposition_using_Givens_Rotations
from Data_type import SimetricnaTridiagonalna

np.set_printoptions(precision=5, suppress=True)


"""
A_matrix = [[1,1,0],
            [1,0,1],
            [0,1,1]]

B_matrix = [[3, 1, 0, 0], 
            [1, -1, 2, 0],
            [0, 2, 1, 1],
            [0, 0, 1, 1]]
"""


A_zgornja_diagonala = [1,1]
A_diagonala = [1,0,1]
A_spodnja_diagonala = [1,1]

A = SimetricnaTridiagonalna(A_diagonala, A_zgornja_diagonala, A_spodnja_diagonala)


B_zgornja_diagonala = [1,2,1]
B_diagonala = [3,-1,1,1]
B_spodnja_diagonala = [1,2,1]

B = SimetricnaTridiagonalna(B_diagonala, B_zgornja_diagonala, B_spodnja_diagonala)

C_zgornja_diagonala = [1,1,2,1]
C_diagonala = [2,3,2,1,4]
C_spodnja_diagonala = [1,1,2,1]

C = SimetricnaTridiagonalna(C_diagonala, C_zgornja_diagonala, C_spodnja_diagonala)


(Q_GS_A, R_GS_A) = Gram_Schmidt_QR_decomposition(A)
(Q_GS_B, R_GS_B) = Gram_Schmidt_QR_decomposition(B)

(Q_GR_A, R_GR_A) = QR_Decomposition_using_Givens_Rotations(A)
(Q_GR_B, R_GR_B) = QR_Decomposition_using_Givens_Rotations(B)


print("\nGram Schmidt method: matrix A \n")
print("Matrix Q: \n" +  str(Q_GS_A))
print("\nMatrix R: \n" +  str(R_GS_A))
print("\nA = Q * R \n" +  str(Q_GS_A @ R_GS_A))

print("\nGivens rotation method: matrix A \n")
print("Matrix Q: \n" +  str(Q_GR_A))
print("\nMatrix R: \n" +  str(R_GR_A))
print("\nA = Q * R \n" +  str(Q_GR_A @ R_GR_A))



print("\nGram Schmidt method: matrix B \n")
print("Matrix Q: \n" +  str(Q_GS_B))
print("\nMatrix R: \n" +  str(R_GS_B))
print("\nA = Q * R \n" +  str(Q_GS_B @ R_GS_B))

print("\nGivens rotation method: matrix B \n")
print("Matrix Q: \n" +  str(Q_GR_B))
print("\nMatrix R: \n" +  str(R_GR_B))
print("\nA = Q * R \n" +  str(Q_GR_B @ R_GR_B))


(Q_GR_C, R_GR_C) = QR_Decomposition_using_Givens_Rotations(C)


print("\nGivens rotation method: matrix C \n")
print("Matrix Q: \n" +  str(Q_GR_C))
print("\nMatrix R: \n" +  str(R_GR_C))
print("\nA = Q * R \n" +  str(Q_GR_C @ R_GR_C))