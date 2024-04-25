import numpy as np
import pandas as pd
import time
import sys
sys.path.append('.')
from DN_1.src.QR_decomposition_Gram_Schmidt import Gram_Schmidt_QR_decomposition
from DN_1.src.QR_decomposition_Givens_rotations import QR_Decomposition_using_Givens_Rotations
import matplotlib.pyplot as plt
from DN_1.src.Random_Matrix import random_symmetric_tridiagonal
from DN_1.src.Eigenvalues_Eigenvectors import Eigenvalues_Eigenvectors_Givens
from DN_1.src.Eigenvalues_Eigenvectors import Eigenvalues_Eigenvectors_Gram_Schmidt

np.set_printoptions(precision=5, suppress=True)


# Število iteracj za izračun lastnih vrednsoti in vektorjev
iterations = 1000
# Prikaz vmesnih iračunov lastnih vrednosti -> vsakih 10000 korakov
show = True


#Testiramo print metodo podatkovnega tipa SimeticnaTridiagonalna
test = random_symmetric_tridiagonal(3)
print(test)
#Testiramo __setitem__ metodo podatkovnega tipa SimeticnaTridiagonalna
test[0,0] = 100
#Testiramo __setitem__ metodo podatkovnega tipa SimeticnaTridiagonalna
test[1,0] = 100
#Testiramo __setitem__ metodo podatkovnega tipa SimeticnaTridiagonalna
test[0,1] = 100
#Testiramo metodo firstindex 
print(test.firstindex())
#Testiramo metodo lastindex 
print(test.lastindex())
#Testiramo metodo __mul__ 
print(test*test)
#Testiramo metodo __matmul__ 
print(test@test)

X = np.array([2,3,5,10,15,20,25,30,50,100,200,300,400,500,600,700,800,900,1000,1500])
Y = [None]*len(X)

X_Givens = np.copy(X)
Y_Givens = [None]*len(X)

X_np = np.copy(X)
Y_np = [None]*len(X)

for i in range(0,len(X)-7):
    A = random_symmetric_tridiagonal(X[i])
    start = time.time()
    (Gram_Sc_Q, Gram_Sc_R) = Gram_Schmidt_QR_decomposition(A)
    end = time.time()
    time_Spent = end-start
    Y[i] = time_Spent
    print("Matrix " + str(X[i]) + "x" + str(X[i]) + " done")



for i in range(0,len(X_Givens)-4):
    A = random_symmetric_tridiagonal(X_Givens[i])
    start = time.time()
    (Givens_Q, Givens_R,rotations) = QR_Decomposition_using_Givens_Rotations(A)
    end = time.time()
    time_Spent = end-start
    Y_Givens[i] = time_Spent
    print("Matrix " + str(X_Givens[i]) + "x" + str(X_Givens[i]) + " done")


#testiramo str metodo podatkovnega tipa ZgornjeDiagonalna
print(str(Givens_R))
#testiramo len metodo len tipa ZgornjeDiagonalna
print(len(Givens_R))
#testiramo metodo __getitem__ len tipa ZgornjeDiagonalna
print(Givens_R[0][0])
#Testiramo metodo __mul__ 
print(Givens_R*Givens_R)
#Testiramo metodo __matmul__ 
print(Givens_R@Givens_R)

#testiramo str metodo podatkovnega tipa Givens
print(str(rotations))



for i in range(0,len(X_np)):
    A = random_symmetric_tridiagonal(X_np[i])
    start = time.time()
    (Gram_Sc_Q, Gram_Sc_R) = np.linalg.qr(A)
    end = time.time()
    time_Spent = end-start
    Y_np[i] = time_Spent
    print("Matrix " + str(X_np[i]) + "x" + str(X_np[i]) + " done")

print("")
print(Y)
print("")
print(Y_Givens)
print("")
# Initialise the subplot function using number of rows and columns 
figure, axis = plt.subplots(2, 2) 


# Adding labels and title
plt.xlabel('Velikost matrike AxA')
plt.ylabel('Čas izvajanja funkacije QR')

axis[0, 0].plot(X[0:len(Y)], Y, color='royalblue') 
axis[0, 0].set_title("Grahamova metoda QR razcepa")
axis[0, 0].set_xlabel('Velikost matrike AxA')  # X label
axis[0, 0].set_ylabel('Čas izvajanja funkcije QR')  # Y label

axis[0, 1].plot(X_Givens[0:len(Y_Givens)], Y_Givens, color='green') 
axis[0, 1].set_title("Givensova metoda QR razcepa")
axis[0, 1].set_xlabel('Velikost matrike AxA')  # X label
axis[0, 1].set_ylabel('Čas izvajanja funkcije QR')  # Y label

axis[1, 0].plot(X_np, Y_np, color='orange') 
axis[1, 0].set_title("QR razcep s knjižnjico Numpy")
axis[1, 0].set_xlabel('Velikost matrike AxA')  # X label
axis[1, 0].set_ylabel('Čas izvajanja funkcije QR')  # Y label

axis[1, 1].plot(X, Y, label = "Grahm", color='royalblue')
axis[1, 1].plot(X_Givens, Y_Givens, label = "Givens", color='green') 
axis[1, 1].plot(X_np, Y_np, label = "Numpy", color='orange') 
axis[1, 1].set_title("Primerjava metod")
# Displaying the graph
plt.show()




#-----------------------------#
#-----------------------------#
#-----------------------------#



X = np.array([2,3,5,10,15,20,25,30,50,100,200,300,400])
Y = [None]*len(X)

X_Givens = np.copy(X)
Y_Givens = [None]*len(X)

X_np = np.copy(X)
Y_np = [None]*len(X)

for i in range(0,len(X)-5):
    A = random_symmetric_tridiagonal(X[i])
    start = time.time()
    (Gram_Sc_val, Gram_Sc_vec) = Eigenvalues_Eigenvectors_Gram_Schmidt(A, iterations,show)
    end = time.time()
    time_Spent = end-start
    Y[i] = time_Spent
    print("Matrix " + str(X[i]) + "x" + str(X[i]) + " done")


for i in range(0,len(X_Givens)-5):
    A = random_symmetric_tridiagonal(X_Givens[i])
    start = time.time()
    (Givens_val, Givens_vec) = Eigenvalues_Eigenvectors_Givens(A, iterations,show)
    end = time.time()
    time_Spent = end-start
    Y_Givens[i] = time_Spent
    print("Matrix " + str(X_Givens[i]) + "x" + str(X_Givens[i]) + " done")



for i in range(0,len(X_np)):
    A = random_symmetric_tridiagonal(X_np[i])
    start = time.time()
    (Gram_Sc_Q, Gram_Sc_R) = np.linalg.qr(A)
    end = time.time()
    time_Spent = end-start
    Y_np[i] = time_Spent
    print("Matrix " + str(X_np[i]) + "x" + str(X_np[i]) + " done")

print("")
print(Y)
print("")
print(Y_Givens)
print("")


# Initialise the subplot function using number of rows and columns 
figure, axis = plt.subplots(2, 2) 


# Adding labels and title
plt.xlabel('Velikost matrike AxA')
plt.ylabel('Čas računanja lastnih vrednosti in vektorjev')

axis[0, 0].plot(X[0:len(Y)], Y, color='royalblue') 
axis[0, 0].set_title("Grahmova metoda računanja") 
axis[0, 0].set_xlabel('Velikost matrike AxA')  # X label
axis[0, 0].set_ylabel('Čas izvajanja funkcije')  # Y label

axis[0, 1].plot(X_Givens[0:len(Y_Givens)], Y_Givens, color='green') 
axis[0, 1].set_title("Givensova metoda računanja")
axis[0, 1].set_xlabel('Velikost matrike AxA')  # X label
axis[0, 1].set_ylabel('Čas izvajanja funkcije')  # Y label

axis[1, 0].plot(X_np, Y_np, color='orange') 
axis[1, 0].set_title("Numpy funkcije za računanje lastnih vrednosti in vektorjev") 
axis[1, 0].set_xlabel('Velikost matrike AxA')  # X label
axis[1, 0].set_ylabel('Čas izvajanja funkcije')  # Y label

axis[1, 1].plot(X, Y, label = "Grahm", color='royalblue')
axis[1, 1].plot(X_Givens, Y_Givens, label = "Givens", color='green') 
axis[1, 1].plot(X_np, Y_np, label = "Numpy", color='orange')
axis[1, 1].set_xlabel('Velikost matrike AxA')  # X label
axis[1, 1].set_ylabel('Čas izvajanja funkcije')  # Y label

# Displaying the graph
plt.show()

