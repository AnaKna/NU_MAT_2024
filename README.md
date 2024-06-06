# 1. DOMAČA NALOGA: Gauss-Legendrove kvadrature

# Ana Knafelc, maj 2024

## Opis

V projektu je podana implementacija funkcije za izračun integrala z Gauss-Legendreovim integracijskim pravilom in s sestavljenim pravilom.

<br/>


## Mapa src

V mapi "**src**" se nahajajo glavne funkcije za izračun:
- integrala z Gauss-Legendreovim integracijskim pravilom,
- integrala s sestavljenim pravilom (s pomočjo Trapeznega pravila in Gauss-Legendrove metode) 

<br/>

V skripti **Gauss_Legendre.py** sta definirani funkciji *Gauss_Legendre* in *Gauss_Legendre_Error*, ki izračunata integral funkcije z Gauss-Legendreovim integracijskim pravilom in predvideno napako algoritma.
Funkciji sta implementirani na osnovi izpeljave integracijskega pravila za dve točki.

Primer uporabe:

    x = symbols('x')  ->  Definicija spremenljivke
    funkcija = x**4+3  ->  Definicija funkcije
    stopnja_polinoma = 4
    a = 1  ->  Zgornja meja integrala
    b = 4  ->  Spodnja meja integrala
    približek, napaka = Gauss_Legendre(funkcija,stopnja_polinoma,x,a,b)

<br/>

Skripta **Gauss_Legendre_Composition.py** vsebuje funkciji *GL_composite_int* in *GL_composite_int_Error*, ki izračunata aproksimacijo integrala funkcije preko sestavljenega pravila s pomočjo Gauss-Legendreove metode in predvideno napako.
Funkciji sta implementirani implementiranu na osnovi izpeljave integracijskega pravila za dve točki.

Primer uporabe:

    x = symbols('x')  ->  Definicija spremenljivke
    funkcija = sin(x)/x  # Define the function
    stopnja_polinoma = 0
    a = 0  ->  Zgornja meja integrala
    b = 5  ->  Spodnja meja integrala
    N = 175  ->  število razcepov integracijskega območja
    približek, napaka = GL_composite_int(funkcija,stopnja,x,a,b,N)


<br/>

V skripti **Trapez_integration.py** je funkcija *trapez_int*, ki izračuna integral funkcije s pomočjo sestavljenega pravila (angl. Trapezoidal rule).
Funkcija je namenjena integraciji polinomov. Funkcija kot izhod vrne dve vrednosti: približek izračuna integrala in približek napake algoritma.

Primer uporabe:

    Definicija funkcije
    def f_x4_3(x):
        return x**4 + 3


    a = 1  ->  Zgornja meja integrala
    b = 4  ->  Spodnja meja integrala
    N = 100  ->  število razcepov integracijskega območja
    približek, napaka = trapez_int(f_x4_3,a,b,N)

<br/>

V skripti **Trapez_integration.py** se nahaja funkcija *trapez_int_sin*, ki izračuna integral funkcije s pomočjo sestavljenega pravila (angl. Trapezoidal rule).
Funkcija je namenjena integraciji funkcije sin(x)/x. Funkcija kot izhod vrne dve vrednosti: približek izračuna integrala in približek napake algoritma.

Primer uporabe:

    Definicija funkcije sin(x)/x
    def sin_div_x(x):
    if(x == 0):     
        if math.isnan(sin(x) / x):
            return 1.0
    else:
        return sin(x) / x


    a = 0  ->  Zgornja meja integrala
    b = 5  ->  Spodnja meja integrala
    N = 50000
    približek, napaka = trapez_int_sin(sin_div_x,a,b,N)

<br/>
<br/>

## Mapa tests

V mapi "**tests**" se nahajajo naslednji testi:
- Test sestavljenega Trapeznega pravila za polinom,
- Test sestavljenega Trapeznega pravila za funkcijo sin(x)/x, 
- Test Gauss-Legendreovega algoritma kjer je pogoj **stopnja_polinoma <= 2*število_točk_za_izračun_integrala - 1** izpolnjen,
- Test Gauss-Legendreovega algoritma kjer pogoj **stopnja_polinoma <= 2*število_točk_za_izračun_integrala - 1** ni izpolnjen,
- Test sestavljenega algoritma z Gauss-Legendrejevo metodo za polinom,
- Test sestavljenega algoritma z Gauss-Legendrejevo metodo za funkcijo sin(x)/x

<br/>
Vsi testi so uspešni z natančnostjo na 5 decimalk.
<br/>
<br/>
<br/>
<br/>

V skripti **00_Pokritost_kode.py** se izvedejo vse funkcije in njihove metode z namenom testiranja delovanja celotnega programa.\
Test pokritosti kode izvedemo v terminalu z naslednjimi zaporednimi ukazi:
```shell
python -m coverage run tests\00_Pokritost_kode.py report
```
in
```shell
coverage report -m
```
<br/>

Pokritost kode je 100%.
<br/>
