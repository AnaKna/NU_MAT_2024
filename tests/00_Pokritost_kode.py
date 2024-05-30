from sympy import symbols, integrate
from scipy import integrate
import sympy as sy 
import sys

sys.path.append('.')
from src.Gauss_Legendre import Gauss_Legendre
from src.Trapez_integration import trapez_int, trapez_int_sin, sin_div_x



# The function to be integrated: x**4 + 3
def f_x4_3(x):
    return x**4 + 3



NaN = sin_div_x(0)
print(NaN)




#--------------------------------SESTAVLJENO PRAVILO f(x) = sin(x) / x----------------------------------------------------------


#N = 186339 -> za natančnost na 10 decimalk
N = 100
sin_integration, sin_error = trapez_int_sin(sin_div_x,0,5,N)
true_result = integrate.quad(sin_div_x, 0, 5)[0]

print("")
print("Sestavljeno pravilo")
print("Funkcija: sin(x)/x")
print("Interval: [0,5]")
print("N = " + str(N))
print("Prava vredsnot: " + str(true_result))
print("Izračunana vrednsoti: " + str(sin_integration))
print("ABSOLUTE ERROR: " + str(abs(sin_integration - true_result)))
print("RELATIVE ERROR: " + str(abs(sin_integration - true_result)/true_result))
print("ESTIMATED ERROR: error <= |" + str(sin_error) + "|")



#--------------------------------SESTAVLJENO PRAVILO f(x) = x^4 + 3----------------------------------------------------------


N = 100
integration,error = trapez_int(f_x4_3,1,4,N)
result = integrate.quad(f_x4_3, 1, 4)[0]

print("")
print("")
print("Sestavljeno pravilo")
print("Funkcija: x**4 + 3" )
print("Interval: [1,4]")
print("N = " + str(N))
print("Prava vredsnot: " + str(result))
print("Izračunana vrednsoti: " + str(integration))
print("ABSOLUTE ERROR: " + str(abs(integration - result)))
print("RELATIVE ERROR: " + str(abs(integration - result)/result))
print("ESTIMATED ERROR: error <= |" + str(error) + "|")





#--------------------------------GAUSS-LEGENDOREOVO PRAVILO f(x) = x^4 + 3----------------------------------------------------------
# stopnja polinoma <= 2*število_točk_za_izračun_integrala - 1
# 4 <= 2*2 - 1
# 4 <= 3 -> FALSE

x = symbols('x')  # Define the variable
funkcija = x**4+3  # Define the function
stopnja = 4
a = 1
b = 4
približek, error = Gauss_Legendre(funkcija,stopnja,x,a,b)
true_result = sy.integrate(funkcija, (x, a, b))
true_result = float(true_result)


print("")
print("")
print("Gauss-Legendreovo integracijsko pravilo")
print("Funkcija: " + str(funkcija))
print("Interval: [1,4]")
print("Prava vrednost: " + str(true_result))
print("Izračunana vrednsoti: " + str(približek))
# Absolutna napaka
print("ABSOLUTE ERROR: " + str(abs(približek - true_result)))
# Relativna napaka
print("RELATIVE ERROR: " + str(abs(približek - true_result)/true_result))
print("CALCULATED ERROR: |" + str(float(error)) + "|")






#--------------------------------GAUSS-LEGENDEOROVO PRAVILO f(x) = x^2 + 3----------------------------------------------------------
# stopnja polinoma <= 2*število_točk_za_izračun_integrala - 1
# 5 <= 2*2 - 1
# 2 <= 3 -> TRUE

x = symbols('x')  # Define the variable
funkcija = x**2 + 3  # Define the function
stopnja = 2
a = 1
b = 4
približek, error = Gauss_Legendre(funkcija,stopnja,x,a,b)
true_result = sy.integrate(funkcija, (x, a, b))
true_result = float(true_result)


print("")
print("")
print("Gauss-Legendreovo integracijsko pravilo")
print("Funkcija: " + str(funkcija))
print("Interval: [" + str(a) + "," + str(b) + "]")
print("Prava vrednost: " + str(true_result))
print("Izračunana vrednsoti: " + str(približek))
# Absolutna napaka
print("ABSOLUTE ERROR: " + str(abs(približek - true_result)))
# Relativna napaka
print("RELATIVE ERROR: " + str(abs(približek - true_result)/true_result))
print("CALCULATED ERROR: |" + str(float(error)) + "|")