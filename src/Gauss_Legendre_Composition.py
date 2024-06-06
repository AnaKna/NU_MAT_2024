import math
import numpy as np

import sys
sys.path.append('.')
from src.Gauss_Legendre import Gauss_Legendre



# Funkcija ki izračuna aproksimacijo integrala funkcije na območju [a,b] po sestavljenem pravilu s pomočjo Gauss-Legendrove metode
def GL_composite_int(funkcija,stopnja,x,a,b,N):
    '''
    funkcija : funkcija, ki jo želimo integrirati
    stopnja : stopnja polinoma za izračun napake po formuli -> za funkcije, ki niso polinomske oblike (sin,cos,tan...) napiši 0
    x : spemenljivka funkcije
    a : spodnja meja integrala
    b : zgornja meja integrala
    N : število pod-območij
    '''

    
    # Definirajmo velikost pod-območja
    h = (b-a)/N
    integral = 0
    
    # Izračun po SESTAVLJENEM PRAVILU
    for i in range(0,N):
        spodnja_meja = a+h*i
        zgornja_meja = spodnja_meja+h
        integral_calc, error_calc = Gauss_Legendre(funkcija, stopnja, x, spodnja_meja, zgornja_meja)
        integral = integral + integral_calc

    
    P = 2 # Stopnja Legendre-jevega polinoma / število točk, ki jih uporabimo za aproksimacijo integrala funkcije
    
    error_est = GL_composite_int_Error(funkcija, P, x, a, b, N)
    
    return integral, error_est




def GL_composite_int_Error(funkcija,stopnja_metode,x,a,b,N):

    P = stopnja_metode
    # Izračun 2N-tega odvoda integracijske funkcije
    odvod = funkcija.diff(x)
    for i in range(0,2*P-1):
        odvod = odvod.diff(x)


    # Izračun vrednosti 2N-tega odvoda funkcije
    vrednosti = []
    M = int(np.ceil(((b-a)/0.01)))
    for i in range(0,M+1):
        if math.isnan(odvod.subs({x:(a + (b-a)*i/M)})):
            vrednosti.append(abs(odvod.subs({x:(a + (b-a)*i/M + 0.0001)})))
        else:
            vrednosti.append(abs(odvod.subs({x:(a + (b-a)*i/M)})))
    
    # Določimo |max| odvoda
    max_value = np.max(vrednosti)

    # Oceno napake pri izračunu integrala po sestavljenem pravilu s pomočjo Gauss-Legendrejeve mdetode izračunamo po spodnji enačbi:
    error_est = (b-a)**(2*P + 1) * (math.factorial(P))**(4)
    error_est = error_est * max_value
    error_est = error_est / (( N**(2*P)) * ( (2*P +1) * ((math.factorial(2*P))**3)))

    return error_est
