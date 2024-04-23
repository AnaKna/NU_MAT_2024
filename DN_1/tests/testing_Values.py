import numpy as np
import pandas as pd
import time
import sys
sys.path.append('.')
from DN_1.src.QR_decomposition_Gram_Schmidt import Gram_Schmidt_QR_decomposition
from DN_1.src.QR_decomposition_Givens_rotations import QR_Decomposition_using_Givens_Rotations
import matplotlib.pyplot as plt
from DN_1.src.Random_Matrix import random_symmetric_tridiagonal



A = random_symmetric_tridiagonal(3)
Q,R,rot = QR_Decomposition_using_Givens_Rotations(A)
Q_np,R_np = np.linalg.qr(A)


print(Q)
print("")
print(Q_np)
print("")


for i in range (0,len(Q)):
    for j in range(0,len(Q)):
        if abs(Q_np[i][j])-abs(Q[i][j]) < 10e-10:
            print("0")
        else:
            print(abs(Q_np[i][j])-abs(Q[i][j]))

for i in range (0,len(Q)):
    for j in range(0,len(Q)):
        if abs(R_np[i][j])-abs(R[i][j]) < 10e-10:
            print("0")
        else:
            print(abs(R_np[i][j])-abs(R[i][j]))


print("")


A = random_symmetric_tridiagonal(3)
Q,R = Gram_Schmidt_QR_decomposition(A)
Q_np,R_np = np.linalg.qr(A)


print(Q)
print("")
print(Q_np)
print("")


for i in range (0,len(Q)):
    for j in range(0,len(Q)):
        if abs(Q_np[i][j])-abs(Q[i][j]) < 10e-10:
            print("0")
        else:
            print(abs(Q_np[i][j])-abs(Q[i][j]))

for i in range (0,len(Q)):
    for j in range(0,len(Q)):
        if abs(R_np[i][j])-abs(R[i][j]) < 10e-10:
            print("0")
        else:
            print(abs(R_np[i][j])-abs(R[i][j]))