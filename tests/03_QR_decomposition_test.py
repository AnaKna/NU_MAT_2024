import numpy as np
import pandas as pd
import time
import sys
sys.path.append('.')
from src.QR_decomposition_Gram_Schmidt import Gram_Schmidt_QR_decomposition
from src.QR_decomposition_Givens_rotations import QR_Decomposition_using_Givens_Rotations
from src.Random_Matrix import random_symmetric_tridiagonal

np.set_printoptions(precision=5, suppress=True)

# Generacija naključne simetrične, tridiagonalne matrike tipa SimetricnaTridiagonalna velikosti NxN
N = 3
A = random_symmetric_tridiagonal(N)

# QR razcep z uporabo knjižnjice Numpy
Q_np, R_np = np.linalg.qr(A)

# QR razcep z Gram-Schmidt metodo
Q_gram, R_gram = Gram_Schmidt_QR_decomposition(A)

# QR razcep z Givenst metodo
Q_givens, R_givens, givens = QR_Decomposition_using_Givens_Rotations(A)




print("")
print("Matrika A")
print(A)
print("")
print("-------------------------------------------------")
print("")
print(" Matrika Q - Givens metoda:")
print(Q_givens)
print("")
print(" Matrika Q - Gram-Schmidt metoda:")
print(Q_gram)
print("")
print(" Matrika Q - np.linalg.qr(A):")
print(Q_np)
print("")
print("-------------------------------------------------")
print("")
print(" Matrika R - Givens metoda:")
print(R_givens)
print("")
print(" Matrika R - Gram-Schmidt metoda:")
print(R_gram)
print("")
print(" Matrika R - np.linalg.qr(A):")
print(R_np)
print("")
print("-------------------------------------------------")
print("")




limit = 10e-10


# Primerjava vrednosti izračunanih z različnimi metodami
primerjava = [["" for _ in range(N)] for _ in range(N)]

for i in range (0,len(A)):
    for j in range(0,len(A)):
        if abs(Q_np[i][j])-abs(Q_gram[i][j]) < limit and abs(Q_np[i][j])-abs(Q_givens[i][j]) < limit:
            primerjava[i][j] = "True"
        else:
            primerjava[i][j] = "False"


flattened_matrix = [element for row in primerjava for element in row]
# Check if all elements are the same by converting to a set
are_all_elements_same = len(set(flattened_matrix))
if are_all_elements_same == 1:
    print("Vrednosti Q se ujemajo!")
else:
    for i in range(len(primerjava)):
        for j in range(len(primerjava)):
            if primerjava[i][j] == "False":
                print("Vrednosti Q se ne ujemajo!")
                print("Napaka na proziciji: [" + str(i) + "][" + str(j) + "]")
                print("Prava vrednost Q: " + str(Q_np[i][j]))
                print("Izračunana vrednost Q - Givens: " + str(Q_givens[i][j]))
                print("Izračunana vrednost Q - Gram: " + str(Q_gram[i][j]))





# Primerjava vrednosti izračunanih z različnimi metodami
primerjava_R = [["" for _ in range(N)] for _ in range(N)]

for i in range (0,len(A)):
    for j in range(0,len(A)):
        if abs(R_np[i][j])-abs(R_gram[i][j]) < limit and abs(R_np[i][j])-abs(R_givens[i][j]) < limit:
            primerjava_R[i][j] = "True"
        else:
            primerjava_R[i][j] = "False"

print("")

flattened_matrix = [element for row in primerjava_R for element in row]
# Check if all elements are the same by converting to a set
are_all_elements_same = len(set(flattened_matrix))
if are_all_elements_same == 1:
    print("Vrednosti R se ujemajo!")
else:
    for i in range(len(primerjava_R)):
        for j in range(len(primerjava_R)):
            if primerjava_R[i][j] == "False":
                print("Vrednosti R se ne ujemajo!")
                print("Napaka na proziciji: [" + str(i) + "][" + str(j) + "]")
                print("Prava vrednost R: " + str(R_np[i][j]))
                print("Izračunana vrednost R - Givens: " + str(R_givens[i][j]))
                print("Izračunana vrednost R - Gram: " + str(R_gram[i][j]))


print("")