import numpy as np
import sys
sys.path.append('.')
from src.QR_decomposition_Gram_Schmidt import Gram_Schmidt_QR_decomposition
from src.QR_decomposition_Givens_rotations import QR_Decomposition_using_Givens_Rotations
from src.Eigenvalues_Eigenvectors import Eigenvalues_Eigenvectors_Givens
from src.Eigenvalues_Eigenvectors import Eigenvalues_Eigenvectors_Gram_Schmidt
from src.Data_type import SimetricnaTridiagonalna

np.set_printoptions(precision=5, suppress=True)
# Prava vrednosti - izračunana vrednost < limita
# Število iteracj za izračun lastnih vrednsoti in vektorjev
iterations = 1000
# Prikaz vmesnih iračunov lastnih vrednosti -> vsakih 10000 korakov
show = False

glavna_diagonala = [1,1,1]
stranska_diagonala = [1,1]

A = SimetricnaTridiagonalna(glavna_diagonala,stranska_diagonala)

"""
A = np.array([[1,1,0],
              [1,1,1],
              [0,1,1]])
"""

Q,R,givens = QR_Decomposition_using_Givens_Rotations(A)
print("")
print("")
print("QR razcep z Givensovimi rotacijami:")
print("")
print("Matrika Q")
print(Q)
print("")
print("Matrika R")
print(R)
print("")
print("A = Q * R")
print(Q@R.matrika)
print("")
print(givens)
print("")
print("")


Q,R = Gram_Schmidt_QR_decomposition(A)
print("")
print("")
print("QR razcep z Gram-Schmidt metodo:")
print("")
print("Matrika Q")
print(Q)
print("")
print("Matrika R")
print(R)
print("")
print("A = Q * R")
print(Q@R)
print("")
print("")


Q,R = np.linalg.qr(A)
print("")
print("")
print("QR razcep s pomočjo numpy knjižnjice -> np.linalg.qr(A):")
print("")
print("Matrika Q")
print(Q)
print("")
print("Matrika R")
print(R)
print("")
print("A = Q * R")
print(Q@R)
print("")
print("")


#######################
#######################
#######################




values, vectors = Eigenvalues_Eigenvectors_Givens(A, iterations,show)
print("")
print("")
print("Lastne vrednosti in vektorji pridobljeni z Givensovimi rotacijami:")
print("")
print("Lastne vredsnoti")
print(values)
print("")
print("Lastni vektorji")
print(vectors)
print("")
print("")


print("Za lastni vektor in njegovo pripadajočo lastno vrednot matrike A velja:")
print("")
print("A * lastni_vektor = lastna_vrednost * lastni_vektor")
print("")

for i in range(0,len(A)):
    print("Lastni vektor " + str(i) + " in lastna vrednost " + str(i) + ":")
    print(str(A) + " * " + str(vectors.T[i]) + " = " + str(vectors.T[i]) + " * " + str(values[i][i]))
    print(str(A@vectors.T[i]) + " = " +  str(vectors.T[i]*values[i][i]))
    print("")


values, vectors = Eigenvalues_Eigenvectors_Gram_Schmidt(A,iterations,show)
print("")
print("")
print("Lastne vrednosti in vektorji pridobljeni z Gram-Schmidt metodo:")
print("")
print("Lastne vredsnoti")
print(values)
print("")
print("Lastni vektorji")
print(vectors)
print("")
print("")


values, vectors = np.linalg.eig(A)
print("")
print("")
print("Lastne vrednosti in vektorji pridobljeni z numpy funkcijo -> np.linalg.eig(A):")
print("")
print("Lastne vredsnoti")
print(values)
print("")
print("Lastni vektorji")
print(vectors)
print("")
print("")




