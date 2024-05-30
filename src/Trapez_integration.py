import math
import numpy as np
from sympy import symbols, sin


# The function to be integrated: sin(x)/x
def sin_div_x(x):
  if(x == 0):     
    if math.isnan(sin(x) / x):
        return 1.0
  else:
    return sin(x) / x



# Izračun integrala po sestavljenem pravilu
# Za računanje integrala polinomov
# a = spodnja meja integrala
# b = zgornja meja integrala
# N = število razdelitev območja
def trapez_int(funkcija,a,b,N):
    h = (b-a)/N
    integral = 0.5 * h * funkcija(a)
    
    for i in range(1,N):
        integral = integral + h*funkcija(a + h*i)

    x = symbols('x')  # Define the variable
    odvod = funkcija(x).diff(x)
    drugi_odvod = odvod.diff(x)
    vrednosti = []
    M = (b-a)*200
    for i in range(0,M+1):
        vrednosti.append(drugi_odvod.subs({x: (a + (b-a)*i/M)}))
        

    max_value = np.max(vrednosti)
    Error = (b-a)**3 * max_value
    Estimated_Error = Error / (12*(N**2))
    
    integral = integral + 0.5 * h * funkcija(a + N*h)
    return integral, Estimated_Error



# Izračun integrala po sestavljenem pravilu
# Za računanje funkcije sin(x)/x
# a = spodnja meja integrala
# b = zgornja meja integrala
# N = število razdelitev območja
def trapez_int_sin(funkcija_sin,a,b,N):
    h = (b-a)/N
    integral = 0.5 * h * 1
    
    for i in range(1,N):
        integral = integral + h*funkcija_sin(a + h*i)
        #print("Iteracija: " + str(i))


    x = symbols('x')  # Define the variable
    odvod = funkcija_sin(x).diff(x)
    drugi_odvod = odvod.diff(x)
    vrednosti = []
    M = (b-a)*200
    for i in range(0,M+1):
        vrednost = drugi_odvod.subs({x: (a + (b-a)*i/M)})
        if math.isnan(vrednost) == False:
           vrednosti.append(vrednost)
            
        

    max_value = np.max(vrednosti)
    Error = (b-a)**3 * max_value
    Estimated_Error = Error / (12*(N**2))


    
    integral = integral + 0.5 * h * funkcija_sin(a + N*h)
    return integral, Estimated_Error

