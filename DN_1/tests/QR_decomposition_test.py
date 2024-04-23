import numpy as np
import pandas as pd
import time
import sys
sys.path.append('.')
from DN_1.src.QR_decomposition_Gram_Schmidt import Gram_Schmidt_QR_decomposition
from DN_1.src.QR_decomposition_Givens_rotations import QR_Decomposition_using_Givens_Rotations
from DN_1.src.Random_Matrix import random_symmetric_tridiagonal


# Generacija naključne simetrične, tridiagonalne matrike tipa SimetricnaTridiagonalna velikosti NxN
N = 5
A = random_symmetric_tridiagonal(N)

# QR razcep z uporabo knjižnjice Numpy
Q_np, R_np = np.linalg.qr(A)

# QR razcep z Gram-Schmidt metodo
Q_gram, R_gram = Gram_Schmidt_QR_decomposition(A)

# QR razcep z Givenst metodo
Q_givens, R_givens, givens = QR_Decomposition_using_Givens_Rotations(A)


limit = 10e-10


# Primerjava vrednosti izračunanih z različnimi metodami
primerjava = [["" for _ in range(N)] for _ in range(N)]

for i in range (0,len(A)):
    for j in range(0,len(A)):
        if abs(Q_np[i][j])-abs(Q_gram[i][j]) < limit and abs(Q_np[i][j])-abs(Q_givens[i][j]) < limit:
            primerjava[i][j] = "True"
        else:
            primerjava[i][j] = "False"



for row in primerjava:
    print (row)