import numpy as np
import pandas as pd
import time
import sys
sys.path.append('.')
from DN_1.src.Random_Matrix import random_symmetric_tridiagonal
from DN_1.src.Eigenvalues_Eigenvectors import Eigenvalues_Eigenvectors_Givens
from DN_1.src.Eigenvalues_Eigenvectors import Eigenvalues_Eigenvectors_Gram_Schmidt


# Limita napake med pravo in izračunano vrednostjo
# Prava vrednosti - izračunana vrednost < limita
limit = 10e-10

# Generacija naključne simetrične, tridiagonalne matrike tipa SimetricnaTridiagonalna velikosti NxN
N = 5
A = random_symmetric_tridiagonal(N)

# QR razcep z uporabo knjižnjice Numpy
Val_np, Vec_np = np.linalg.eig(A)
Val_np = np.sort(abs(Val_np))
Vec_np = np.sort(abs(Vec_np.T))
Val_gram_vec = [0] * N

# Get the order of indices that would sort the first column
sort_order = np.argsort(Vec_np[:, 0])

# Sort the matrix based on that order
Vec_np = Vec_np[sort_order]

# QR razcep z Gram-Schmidt metodo
Val_gram, Vec_gram = Eigenvalues_Eigenvectors_Gram_Schmidt(A)
Vec_gram = np.sort(abs(Vec_gram.T))
sort_order = np.argsort(Vec_gram[:, 0])
Vec_gram = Vec_gram[sort_order]
# QR razcep z Givenst metodo
Val_givens, Vec_givens = Eigenvalues_Eigenvectors_Givens(A)
Vec_givens = np.sort(abs(Vec_givens.T))
sort_order = np.argsort(Vec_givens[:, 0])
Vec_givens = Vec_givens[sort_order]

Val_gram_vec = np.zeros(N)
Val_givens_vec = np.zeros(N)
for i in range(len(A)):
    Val_gram_vec[i] = Val_gram[i][i]
    Val_givens_vec[i] = Val_givens[i][i]

Val_gram_vec = np.sort(abs(Val_gram_vec))
Val_givens_vec = np.sort(abs(Val_givens_vec))


# Primerjava vrednosti izračunanih z različnimi metodami
primerjava_vrenodsti = [""for _ in range(N)]

for i in range (0,len(A)):
    if abs(Val_np[i])-abs(Val_gram_vec[i]) < limit and abs(Val_np[i])-abs(Val_givens_vec[i]) < limit:
        primerjava_vrenodsti[i] = "True"
    else:
        primerjava_vrenodsti[i] = "False"




elements = set(primerjava_vrenodsti)
# Check if all elements are the same by converting to a set
are_all_elements_same = len(set(elements))
if are_all_elements_same == 1:
    print("Lastne vrednosti se ujemajo!")
else:
    for i in range(len(primerjava_vrenodsti)):
            if primerjava_vrenodsti[i] == "False":
                print("Lastne vrednosti se ne ujemajo!")
                print("Napaka na proziciji: [" + str(i) + "]")
                print("Prava lastna vrednost: " + str(Val_np[i]))
                print("Izračunana lastna vrednost Givens: " + str(Val_givens_vec[i]))
                print("Izračunana lastna vrednost Gram: " + str(Val_gram_vec[i]))
        





# Primerjava vrednosti izračunanih z različnimi metodami
primerjava_vektorjev = [["" for _ in range(N)] for _ in range(N)]

for i in range (0,len(A)):
    for j in range(0,len(A)):
        if abs(Vec_np[i][j])-abs(Vec_gram[i][j]) < limit and abs(Vec_np[i][j])-abs(Vec_givens[i][j]) < limit:
            primerjava_vektorjev[i][j] = "True"
        else:
            primerjava_vektorjev[i][j] = "False"


print("")
flattened_matrix = [element for row in primerjava_vektorjev for element in row]
# Check if all elements are the same by converting to a set
are_all_elements_same = len(set(flattened_matrix))
if are_all_elements_same == 1:
    print("Vrednosti vektorjev se ujemajo!")
else:
    for i in range(len(primerjava_vektorjev)):
        for j in range(len(primerjava_vektorjev)):
            if primerjava_vektorjev[i][j] == "False":
                print("Vrednosti lastnih vektorjev se ne ujemajo!")
                print("Napaka na proziciji: [" + str(i) + "][" + str(j) + "]")
                print("Prava vrednost vektorja: " + str(Vec_np[i][j]))
                print("Izračunana vrednost vektorja Givens: " + str(Vec_givens[i][j]))
                print("Izračunana vrednost vektorja Gram: " + str(Vec_gram[i][j]))
        

    

