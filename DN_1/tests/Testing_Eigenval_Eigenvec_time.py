import numpy as np
import pandas as pd
import time
from QR_decomposition_Gram_Schmidt import Gram_Schmidt_QR_decomposition
from QR_decomposition_Givens_rotations import QR_Decomposition_using_Givens_Rotations
import matplotlib.pyplot as plt
from Random_Matrix import random_symmetric_tridiagonal
from Eigenvalues_Eigenvectors import Eigenvalues_Eigenvectors_Givens
from Eigenvalues_Eigenvectors import Eigenvalues_Eigenvectors_Gram_Schmidt


np.set_printoptions(precision=5, suppress=True)


X = np.array([2,3,5,10,15,20,25,30,50,100,200,300,400])
Y = [None]*len(X)

X_Givens = np.copy(X)
Y_Givens = [None]*len(X)

X_np = np.copy(X)
Y_np = [None]*len(X)

for i in range(0,len(X)-5):
    A = random_symmetric_tridiagonal(X[i])
    start = time.time()
    (Gram_Sc_val, Gram_Sc_vec) = Eigenvalues_Eigenvectors_Gram_Schmidt(A)
    end = time.time()
    time_Spent = end-start
    Y[i] = time_Spent
    print("Matrix " + str(X[i]) + "x" + str(X[i]) + " done")
    print(X[i])



for i in range(0,len(X_Givens)-5):
    A = random_symmetric_tridiagonal(X_Givens[i])
    start = time.time()
    (Givens_val, Givens_vec) = Eigenvalues_Eigenvectors_Givens(A)
    end = time.time()
    time_Spent = end-start
    Y_Givens[i] = time_Spent
    print("Matrix " + str(X_Givens[i]) + "x" + str(X_Givens[i]) + " done")
    print(X_Givens[i])


for i in range(0,len(X_np)):
    A = random_symmetric_tridiagonal(X_np[i])
    start = time.time()
    (Gram_Sc_Q, Gram_Sc_R) = np.linalg.qr(A)
    end = time.time()
    time_Spent = end-start
    Y_np[i] = time_Spent
    print("Matrix " + str(X_np[i]) + "x" + str(X_np[i]) + " done")
    print(X_np[i])

print("")
print(Y)
print("")
print(Y_Givens)
print("")


# Initialise the subplot function using number of rows and columns 
figure, axis = plt.subplots(2, 2) 


# Adding labels and title
plt.xlabel('Velikost matrike AxA')
plt.ylabel('Čas izvajanja funkacije Eigenval/Eigenvec')

axis[0, 0].plot(X[0:len(Y)], Y, color='royalblue') 
axis[0, 0].set_title("Grahm graph") 
axis[0, 1].plot(X_Givens[0:len(Y_Givens)], Y_Givens, color='green') 
axis[0, 1].set_title("Givens graph") 
axis[1, 0].plot(X_np, Y_np, color='orange') 
axis[1, 0].set_title("Numpy graph") 
axis[1, 1].plot(X, Y, label = "Grahm", color='royalblue')
axis[1, 1].plot(X_Givens, Y_Givens, label = "Givens", color='green') 
axis[1, 1].plot(X_np, Y_np, label = "Numpy", color='orange') 

# Displaying the graph
plt.show()


