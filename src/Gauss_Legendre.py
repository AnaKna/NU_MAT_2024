import numpy as np
import math

# Gauss-Legendre Kvadratura
# Aproksimacija integrala za DVE TOČKI: n = 2
# Definiramo Legendre-jev polinom druge stopnje
# P2(x) = (3x^2 - 1)/2
# Definirajmo Legendre-jeve kolokacijske točke - ničle Legendre-jevega polinoma druge stopnje
# x1 = squrt(1/3) in x2 = squrt(-1/3)

# Izračun uteži w1 in w2
# w1 = 2/(1-x1^2)*(P2'(x1)^2)
# Odvod Legendre-jevega polinoma druge stopnje
# P2'(x) = 3x
# P2'(x1) = 3 * squrt(1/3)
# P2'(x2) = 3 * squrt(-1/3)
# P2'(x1)^2 = 9 * 1/3 = 3
# P2'(x2)^2 = 9 * 1/3 = 3
# w1 = 2/(1-x1^2)*(P2'(x1)^2)
# w1 = 2/(1-x1^2)*(3) = 1
# w2 = 2/(1-x2^2)*(P2'(x2)^2)
# w2 = 2/(1-x2^2)*(3) = 1

# Sprememba integracijskega območja iz [-1,1] na območje [A,B]
# x1 = (B-A)*t/2 + (B+A)/2
# x2 = (B-A)*t/2 + (B+A)/2

# Izračun integrala:
# ( w1*f(x1) + w2*f(x2) ) * (B-A) / 2 


def Gauss_Legendre(funkcija,stopnja_polinoma,variable,A,B):

    w1 = 1    # Utež w1
    w2 = 1    # Utež w2
    N = 2     # Stopnja Legendre-jevega polinoma / število točk, ki jih uporabimo za aproksimacijo integrala funkcije


    x1 = ((B-A)*(np.sqrt(1/3)))/2 + (B+A)/2
    x2 = ((B-A)*(-np.sqrt(1/3)))/2 + (B+A)/2

    fun_t1 = funkcija.subs({variable:x1})
    fun_t2 = funkcija.subs({variable:x2})

    # Izračun aproksimacije integrala:
    # ( w1*f(x1) + w2*f(x2) ) * (B-A) / 2 
    integral = ((w1 * fun_t1 + w2 * fun_t2))*(B-A)/2



    število_odvodov = 2*N-1
    # Če je stopnja polinoma <= 2*N-1 je aproksimacija integrala točka in je Error = 0
    if(stopnja_polinoma <= število_odvodov & stopnja_polinoma != 0):
        Error = 0
    else:
        # Izračun 2N-tega odvoda integracijske funkcije
        odvod = funkcija.diff(variable)
        for i in range(0,2*N-1):
            odvod = odvod.diff(variable)


        # Izračun vrednosti 2N-tega odvoda funkcije
        vrednosti = []
        M = int(np.ceil(((B-A)/0.01)))
        for i in range(0,M+1):
            if math.isnan(odvod.subs({variable:(A + (B-A)*i/M)})):
                vrednosti.append(abs(odvod.subs({variable:(A + (B-A)*i/M + 0.0001)})))
            else:
                vrednosti.append(abs(odvod.subs({variable:(A + (B-A)*i/M)})))
        
        # Določimo |max| odvoda
        max_value = np.max(vrednosti)
        # Ker število polinoma ni <= 2*N-1 približek napake izračunamo po spodnji enačbi
        Error = (B-A)**(2*N + 1) * math.factorial(N)**(4)
        Error = Error * max_value
        Error = Error / ((2*N +1) * (math.factorial(2*N)**3))   

    return integral, Error
