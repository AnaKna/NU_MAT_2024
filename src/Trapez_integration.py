import math
import numpy as np
from sympy import symbols


# Izračun integrala po sestavljenem pravilu
# Za računanje integrala polinomov
# a = spodnja meja integrala
# b = zgornja meja integrala
# N = število razdelitev območja
def trapez_int(funkcija,a,b,N):
    # Definirajmo velikost pod-območja
    h = (b-a)/N
    # Aproksimacija integrala na območju [a,a+h]
    integral = 0.5 * h * funkcija(a)
    
    for i in range(1,N):
        integral = integral + h*funkcija(a + h*i)

    x = symbols('x')  # Definiramo spremenljivko funkcije
    odvod = funkcija(x).diff(x)
    drugi_odvod = odvod.diff(x)
    vrednosti = []
    M = (b-a)*200
    for i in range(0,M+1):
        vrednosti.append(drugi_odvod.subs({x: (a + (b-a)*i/M)}))
        
    # Določimo max. vrednost drugega odvoda funkcije, ki jo želimo integrirati in izračunamo približek napake algoritma
    max_value = np.max(vrednosti)
    Error = (b-a)**3 * max_value
    Estimated_Error = Error / (12*(N**2))
    
    # Aproksimacija integrala na območju [a+ N*h,b]
    integral = integral + 0.5 * h * funkcija(a + N*h)
    return integral, Estimated_Error



# Izračun integrala po sestavljenem pravilu
# Za računanje funkcije sin(x)/x
# a = spodnja meja integrala
# b = zgornja meja integrala
# N = število razdelitev območja
def trapez_int_sin(funkcija_sin,a,b,N):
    # Definirajmo velikost pod-območja
    h = (b-a)/N
    # Aproksimacija integrala na območju [a,a+h]
    # integral = 0.5 * h * funkcija_sin(a) -> limita sin(0)/0 = 1
    integral = 0.5 * h * 1
    
    for i in range(1,N):
        integral = integral + h*funkcija_sin(a + h*i)


    x = symbols('x')  # Definiramo spremenljivko funkcije
    odvod = funkcija_sin(x).diff(x)
    drugi_odvod = odvod.diff(x)
    vrednosti = []
    M = (b-a)*200
    for i in range(0,M+1):
        vrednost = drugi_odvod.subs({x: (a + (b-a)*i/M)})
        if math.isnan(vrednost) == False:
           vrednosti.append(vrednost)
            
        
    # Določimo max. vrednost drugega odvoda funkcije, ki jo želimo integrirati in izračunamo približek napake algoritma
    max_value = np.max(vrednosti)
    Error = (b-a)**3 * max_value
    Estimated_Error = Error / (12*(N**2))
    
    # Aproksimacija integrala na območju [a+ N*h,b]
    integral = integral + 0.5 * h * funkcija_sin(a + N*h)
    return integral, Estimated_Error

