import numpy as np
import time
import sys
import os
import matplotlib.pyplot as plt
sys.path.append('.')
print(sys.path)
from DN_1.src.QR_decomposition_Givens_rotations_OPT import QR_Decomposition_Givens_OPT
from DN_1.src.Random_Matrix import random_matrix, random_symmetric_tridiagonal
from DN_1.src.QR_decomposition_Givens_rotations import QR_Decomposition_using_Givens_Rotations

#from src.QR_decomposition_Givens_rotations import QR_Decomposition_using_Givens_Rotations
#import matplotlib.pyplot as plt
#from src.Random_Matrix import random_symmetric_tridiagonal


np.set_printoptions(precision=5, suppress=True)


X_Givens = np.array([2,3,5,10,15,20,25,30,50,100,200,300,400,500,600,700,800,900,1000,1500])
Y_Givens = [None]*len(X_Givens)

X_Givens_opt = np.copy(X_Givens)
Y_Givens_opt = [None]*len(X_Givens)

X_np = np.copy(X_Givens)
Y_np = [None]*len(X_Givens)




for i in range(0,len(X_Givens)-4):
    A = random_symmetric_tridiagonal(X_Givens[i])
    start = time.time()
    (Givens_Q, Givens_R,rotations) = QR_Decomposition_using_Givens_Rotations(A)
    end = time.time()
    time_Spent = end-start
    Y_Givens[i] = time_Spent
    print("Matrix " + str(X_Givens[i]) + "x" + str(X_Givens[i]) + " done")
    print(X_Givens[i])


for i in range(0,len(X_Givens_opt)-4):
    A = random_symmetric_tridiagonal(X_Givens_opt[i])
    start = time.time()
    (Givens_Q_opt, Givens_R_opt,rotations) = QR_Decomposition_Givens_OPT(A)
    end = time.time()
    time_Spent = end-start
    Y_Givens_opt[i] = time_Spent
    print("Matrix " + str(X_Givens_opt[i]) + "x" + str(X_Givens_opt[i]) + " done")
    print(X_Givens_opt[i])



for i in range(0,len(X_np)):
    A = random_symmetric_tridiagonal(X_np[i])
    start = time.time()
    (Gram_Sc_Q, Gram_Sc_R) = np.linalg.qr(A)
    end = time.time()
    time_Spent = end-start
    Y_np[i] = time_Spent
    print("Matrix " + str(X_np[i]) + "x" + str(X_np[i]) + " done")
    print(X_np[i])



# Initialise the subplot function using number of rows and columns 
figure, axis = plt.subplots(2, 2) 


# Adding labels and title
plt.xlabel('Velikost matrike AxA')
plt.ylabel('Čas izvajanja funkacije QR')

axis[0, 0].plot(X_Givens[0:len(Y_Givens)], Y_Givens, color='royalblue') 
axis[0, 0].set_title("Grahm graph") 
axis[0, 1].plot(X_Givens_opt[0:len(Y_Givens_opt)], Y_Givens_opt, color='green') 
axis[0, 1].set_title("Givens graph") 
axis[1, 0].plot(X_np, Y_np, color='orange') 
axis[1, 0].set_title("Numpy graph") 
axis[1, 1].plot(X_Givens, Y_Givens, label = "Grahm", color='royalblue')
axis[1, 1].plot(X_Givens_opt, Y_Givens_opt, label = "Givens", color='green') 
axis[1, 1].plot(X_np, Y_np, label = "Numpy", color='orange') 

# Displaying the graph
plt.show()


