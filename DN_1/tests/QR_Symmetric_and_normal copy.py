import sys
sys.path.append('.')
from DN_1.src.Random_Matrix import random_symmetric_tridiagonal
from DN_1.src.Random_Matrix import random_matrix
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt


X_tir_sim = np.array([2,3,5,10,15,20,25,30,50,100,200,300,400,500,600,700,800,900,1000,1500,2000,2500,3000])
Y_tri_sim = [None]*len(X_tir_sim)

X_random = np.copy(X_tir_sim)
Y_random = [None]*len(X_tir_sim)


for i in range(0,len(X_tir_sim)):   
    A = random_symmetric_tridiagonal(X_tir_sim[i])
    start = time.time()
    Q,R = np.linalg.qr(A)
    end = time.time()
    time_Spent = end-start
    Y_tri_sim[i] = time_Spent


for i in range(0,len(X_random)):   
    A = random_matrix(X_random[i])
    start = time.time()
    Q,R = np.linalg.qr(A)
    end = time.time()
    time_Spent = end-start
    Y_random[i] = time_Spent




# Initialise the subplot function using number of rows and columns 
#figure, axis = plt.subplots(2, 2) 


# Adding labels and title
#plt.xlabel('Velikost matrike AxA')
#plt.ylabel('Čas izvajanja funkacije QR')

#axis[0, 0].plot(X_tir_sim, Y_tri_sim, label = "Tri and Sym", color='royalblue') 
#axis[0, 0].plot(X_random, Y_random, label = "Random", color='green') 


plt.xlabel('Velikost matrike AxA')
plt.ylabel('Čas izvajanja funkcije Numpy QR')
plt.plot(X_tir_sim, Y_tri_sim, label = "Triangular and Symmetric Matrix", color='royalblue') 
plt.plot(X_random, Y_random, label = "Random", color='green') 
# Displaying the graph
plt.legend()
plt.show()