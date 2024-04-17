import numpy as np
import time
from QR_decomposition_Gram_Schmidt import Gram_Schmidt_QR_decomposition
from QR_decomposition_Givens_rotations import QR_Decomposition_using_Givens_Rotations
from Data_type import SimetricnaTridiagonalna
from Data_type import Givens
from Data_type import *
np.set_printoptions(precision=5, suppress=True)




# Input matrix
C_zgornja_diagonala = [1,1,2,1]
C_diagonala = [2,3,2,1,4]
C_spodnja_diagonala = [1,1,2,1]

C = SimetricnaTridiagonalna(C_diagonala, C_zgornja_diagonala, C_spodnja_diagonala)


start = time.time()
(Gram_Sc_Q, Gram_Sc_R) = Gram_Schmidt_QR_decomposition(C)
end = time.time()
print(Gram_Sc_Q)
print(Gram_Sc_R)
print("Gram–Schmidt QR decomposition: " + str(1000*(end-start)) + " ms")



start = time.time()
(Givens_Q, Givens_R, givens_data) = QR_Decomposition_using_Givens_Rotations(C)
end = time.time()

print("QR decomposition using Givens rotations: " + str(1000*(end-start)) + " ms")

# in seconds
start = time.time()

end = time.time()

# in miliseconds
#print(str(1000*(end-start)) + " ms")



A = [[3, 1, 0, 0], 
     [1, -1, 2, 0],
     [0, 2, 1, 1],
     [0, 0, 1, 1]]

# Fill this in!
eigvals, eigvecs = np.linalg.eig(A)

# Notice that we can use variables in a print!
# f'something {var}' means sub in the var in the string
print(f'Eigenvalues = {eigvals}') 
print(f'Eigenvectors: \n{eigvecs}')


print("\n")
print(A@eigvecs)
print("\n")
print(eigvals.T*eigvecs)
print("\n")





(Givens_Q, Givens_R, givens_data) = QR_Decomposition_using_Givens_Rotations(A)


A_decomposed = Givens_R.matrika * Givens_Q
Q_decomposed = np.eye(len(Givens_Q))
Q_decomposed = np.array(Givens_Q)

for i in range (0, 470000):
    Q, R, givens = QR_Decomposition_using_Givens_Rotations(A_decomposed)
    Q_decomposed = Givens_Q@Q
    A_decomposed = Givens_R.matrika @ Givens_Q


values_matrix = Q_decomposed.T@A@Q_decomposed
value = np.zeros(len(A))

for i in range(0,len(A)):
    value[i] = values_matrix[i][i]

print("Q DECOMPOSED")
print(Q_decomposed)

print("A DECOMPOSED")
print(A_decomposed)

print("VALUES")
print(A_decomposed)
print(value)

# We compare our results with the official numpy algorithm
print("ORIGINAL")
print(np.linalg.eigvals(A))