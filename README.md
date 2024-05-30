# 1. DOMAČA NALOGA: Gauss-Legendrove kvadrature

# Ana Knafelc, maj 2024

## Opis

V projektu je podana implementacija funkcije za izračun integrala z Gauss-Legendreovim integracijskim pravilom in s sestavljenim pravilom.

<br/>


## Mapa src

V mapi "**src**" se nahajajo glavne funkcije za izračun:
- integrala z Gauss-Legendreovim integracijskim pravilom
- integrala s sestavljenim praivlom 

<br/>

V skripti **Gauss_Legendre.py** se nahaj funkcija *Gauss_Legendre*, ki izračuna integrala funkcije z Gauss-Legendreovim integracijskim pravilom.
Funkcija je bila definirana na izpeljavi integracijskega pravila za dve točki: N = 2

<br/>

V skripti **Trapez_integration.py** se nahaj funkcija *trapez_int*, ki izračuna integral funkcije s pomočjo sestavljenega pravila (angl. Trapezoidal rule).
Funkcija je namenjena integraciji polinomov. Funkcija kot izhod vrne dve vrednosti: približek izračuna integrala in približek napake algoritma

<br/>

V skripti **Trapez_integration.py** se nahaj funkcija *trapez_int_sin*, ki izračuna integral funkcije s pomočjo sestavljenega pravila (angl. Trapezoidal rule).
Funkcija je namenjena integraciji funkcije sin(x)/x. Funkcija kot izhod vrne dve vrednosti: približek izračuna integrala in približek napake algoritma

<br/>
<br/>

## Mapa tests

V mapi "**tests**" se nahajajo naslednji testi:
- Test sestavljenega pravila za polinom
- Test sestavljenega pravila za funkcijo sin(x)/x
- Test Gauss-Legendrovega algoritma kjer je pogoj **stopnja_polinoma <= 2*število_točk_za_izračun_integrala - 1** izpolnjen
- Test Gauss-Legendrovega algoritma kjer pogoj **stopnja_polinoma <= 2*število_točk_za_izračun_integrala - 1** ni izpolnjen

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
