import numpy as np
import pandas as pd
import time
import sys
sys.path.append('.')
from src.Random_Matrix import random_symmetric_tridiagonal
from src.Eigenvalues_Eigenvectors import Eigenvalues_Eigenvectors_Givens
from src.Eigenvalues_Eigenvectors import Eigenvalues_Eigenvectors_Gram_Schmidt
from src.Data_type import SimetricnaTridiagonalna


# Limita napake med pravo in izračunano vrednostjo
# Prava vrednosti - izračunana vrednost < limita
limit = 10e-10
# Število iteracj za izračun lastnih vrednsoti in vektorjev
iterations = 1000
# Prikaz vmesnih iračunov lastnih vrednosti -> vsakih 10000 korakov
show = False

# Generacija naključne simetrične, tridiagonalne matrike tipa SimetricnaTridiagonalna velikosti NxN
N = 5
A = random_symmetric_tridiagonal(N)

# QR razcep z uporabo knjižnjice Numpy
Val_np, Vec_np = np.linalg.eig(A)
# QR razcep z Gram-Schmidt metodo
Val_gram, Vec_gram = Eigenvalues_Eigenvectors_Gram_Schmidt(A,iterations,show)
# QR razcep z Givens metodo
Val_givens, Vec_givens = Eigenvalues_Eigenvectors_Givens(A,iterations,show)

# Lastne vrednosti matrike A so v diagonali matrike Val_gram in Val_givens
Val_gram_vec = np.zeros(N)
Val_givens_vec = np.zeros(N)
for i in range(len(A)):
    Val_gram_vec[i] = Val_gram[i][i]
    Val_givens_vec[i] = Val_givens[i][i]

print("")
print("Matrika A")
print(A)
print("")
print("-------------------------------------------------")
print("")
print("Lastni vektorji - Givens metoda:")
print(Vec_givens)
print("")
print("Lastni vektorji - Gram-Schmidt metoda:")
print(Vec_gram)
print("")
print("Lastni vektorji - np.linalg.eig(A):")
print(Vec_np)
print("")
print("-------------------------------------------------")
print("")
print("Lastne vrednosti - Givens metoda:")
print(Val_givens_vec)
print("")
print("Lastne vrednosti - Gram-Schmidt metoda:")
print(Val_gram_vec)
print("")
print("Lastne vrednosti - np.linalg.eig(A):")
print(Val_np)
print("")
print("-------------------------------------------------")
print("")
# Za lastni vektor in njegovo pripadajočo lastno vrensot matrike A velja:
# A * vector = value * vector
print("Za lastni vektor in njegovo pripadajočo lastno vrensot matrike A velja:")
print("A * lastni_vektor = lastna_vrednost * lastni_vektor")
print("")
print(str(A) + " * " + str(Vec_givens.T[0]) + " = " + str(Vec_givens.T[0]) + " * " + str(Val_givens_vec[0]))
print("")
print(str(A@Vec_givens.T[0]) + " = " +  str(Vec_givens.T[0]*Val_givens_vec[0]))
print("")
print("-------------------------------------------------")
print("")


# Ker so zaradi različnih metod računanja QR razcepa matrike A, pozicije vektorjev in vrednosti
# za vsako metodo različne, jih sortiramo in primerjamo zgolj njihove absolutne vrednosti
Val_np = np.sort(abs(Val_np))
Vec_np = np.sort(abs(Vec_np.T))
sort_order = np.argsort(Vec_np[:, 0])
Vec_np = Vec_np[sort_order]

Vec_gram = np.sort(abs(Vec_gram.T))
sort_order = np.argsort(Vec_gram[:, 0])
Vec_gram = Vec_gram[sort_order]

Vec_givens = np.sort(abs(Vec_givens.T))
sort_order = np.argsort(Vec_givens[:, 0])
Vec_givens = Vec_givens[sort_order]

Val_gram_vec = np.sort(abs(Val_gram_vec))
Val_givens_vec = np.sort(abs(Val_givens_vec))


# Primerjava lastnih vrednosti izračunanih z različnimi metodami -> False (vrednsoti se razlikujejo) ali True (vrednsoti so enake)
primerjava_vrenodsti = [""for _ in range(N)]

for i in range (0,len(A)):
    if abs(Val_np[i])-abs(Val_gram_vec[i]) < limit and abs(Val_np[i])-abs(Val_givens_vec[i]) < limit:
        primerjava_vrenodsti[i] = "True"
    else:
        primerjava_vrenodsti[i] = "False"

print("")


elements = set(primerjava_vrenodsti)
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
        

print("")


#Primerjava vrednosti lastnih vektorjev izračunanih z različnimi metodami -> False (vrednsoti se razlikujejo) ali True (vrednsoti so enake)
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


print("")



