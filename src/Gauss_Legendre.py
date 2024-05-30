import numpy as np
import math

# Gauss-Legendre Kvadratura
# Aproksimacija integrala za DVE TOČKI: n = 2
# Definiramo Legendre-jev polinom druge stopnje
# P2(x) = 1/2 * (3x^2 - 1)
# Definirajmo Legendre-jeve kolokacijske točke
# x1 = squrt(1/3) in x2 = squrt(-1/3)

# Uteži w1 in w2
# w1 = 2/(1-x1^2)*(P2'(x1)^2)
# P2'(x) = 3x
# P2'(x1) = 3 * squrt(1/3)
# P2'(x2) = 3 * squrt(-1/3)
# P2'(x1)^2 = 9 * 1/3 = 3
# P2'(x2)^2 = 9 * 1/3 = 3
# w1 = 2/(1-x1^2)*(3) = 1
# w2 = 2/(1-x2^2)*(3) = 1

# integral na območju [A,B]
# t1 = (B-A)*x1/2 + (B+A)/2
# t2 = (B-A)*x2/2 + (B+A)/2

# Izračun integrala:
# (f(t1) + f(t2)) * (B-A)/2 


def Gauss_Legendre(funkcija,stopnja_polinoma,variable,A,B):

    w1 = 1
    w2 = 1
    N = 2


    t1 = ((B-A)*(np.sqrt(1/3)))/2 + (B+A)/2
    t2 = ((B-A)*(-np.sqrt(1/3)))/2 + (B+A)/2

    fun_t1 = funkcija.subs({variable:t1})
    fun_t2 = funkcija.subs({variable:t2})

    integral = ((w1 * fun_t1 + w2 * fun_t2))*(B-A)/2



    število_odvodov = 2*N-1
    if(stopnja_polinoma <= število_odvodov):
        Error = 0
    else:
        # Izračun 2N-tega odvoda integracijske funkcije
        odvod = funkcija.diff(variable)
        for i in range(0,2*N-1):
            odvod = odvod.diff(variable)


        # Izračun vrednosti 2N-tega odvoda funkcije
        vrednosti = []
        M = (B-A)*500
        for i in range(0,M+1):
            vrednosti.append(abs(odvod.subs({variable:(A + (B-A)*i/M)})))
        
        # Določimo |max| odvoda
        max_value = np.max(vrednosti)
        Error = (B-A)**(2*N + 1) * math.factorial(N)**(4)
        Error = Error * max_value
        Error = Error / ((2*N +1) * (math.factorial(2*N)**3))   

    return integral, Error
