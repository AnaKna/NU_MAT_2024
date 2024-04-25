# 1. DOMAČA NALOGA: QR razcep simetriˇcne tri-diagonalne matrike

# Ana Knafelc, april 2024

## Navodila

<br/>


## Mapa src

V mapi "**src**" se nahajajo glavne funkcije za izračun:
- QR razcepa z uporabo Givensovih rotacij
- QR razcepa po Gram-Schmidt metodi
- Lastnih vrednosti in lastnih vektorjev matrike z uporabo QR razcepa po metodi Givens
- Lastnih vrednosti in lastnih vektorjev matrike z uporabo QR razcepa po metodi Gram-Schmidt

<br/>

V skripti **QR_decomposition_Givens_rotations.py** se nahaj funkcija *QR_Decomposition_using_Givens_Rotations*, ki izračuna QR razcep vhodne matrike z uporabo Givensovih rotacij.

<br/>

V skripti **QR_decomposition_Gram_Schmidt.py** se nahaj funkcija *Gram_Schmidt_QR_decomposition*, ki izračuna QR razcep vhodne matrike po Gram-Schmidt metodi.

<br/>

V skripti **Eigenvalues_Eigenvectors.py** se nahajajo funkciji *Eigenvalues_Eigenvectors_Givens* in *Eigenvalues_Eigenvectors_Gram_Schmidt*, ki izračunata lastne vrednosti in vektorje vhodne funkcije s pomočjo QR razcepa po metodi Givens in Gram-Schmidt.

<br/>

V skripti **Data_type.py** se nahajajo definicije različnih podatkovnih tipov: *SimetricnaTridiagonalna*, *ZgornjaDvodiagonalna* in *Givens*.

<br/>

V skripti **Random_Matrix.py** se nahaja funkcija *random_symmetric_tridiagonal*, ki kot izhod vrne naključno simetrično, tridiagonalno matriko.


<br/>
<br/>

## Mapa tests

V mapi "**tests**" se nahajajo naslednji testi:
- Test za računanje pokritosti kode
- Razcep matrike A, ki je predstavljen v poročilu naloge
- Test pravilnosti delovanja funkcije QR razcepa z različnimi metodami
- Test pravilnosti delovanja funkcije za računanje lastnih vrednoti in vektorjev z različnimi metodami

<br/>

V skripti **00_Pokritost_kode.py** se izvedejo vse funkcije in njihove metode z namenom testiranja delovanja celotnega programa.\
Test pokritosti kode izvedemo v terminalu z naslednjimi zaporednimi ukazi:
```shell
python -m coverage run DN_1\tests\00_Pokritost_kode.py report
```
in
```shell
coverage report -m
```

<br/>
<br/>

V skripti **01_Razcep_matrike_A.pyy** se izvede QR razcep matrike A in izračunj njenih lastnih vrednsoti in vektorjev, kot je opisano v poročilu naloge. 

<br/>


V skripti **03_QR_decomposition_test.py** se izvede celovit test delovanja funkcije QR razcepa z uporabo Givensovih rotacij in po Gram-Schmidt metodi. Rezultate primerjamo z QR funkcijo iz knjižnjice numpy.

<br/>

V skripti **04_Eigenvalues_and_vectors_test.pyy** se izvede celovit test delovanja funkcije za izračun lastnih vrednosti in vektorjev z QR razcepom po metodi Givens in Gram-Schmidt metodi. Rezultate primerjamo z funkcijo za izračun lastnih vrednosti in vektorjev iz knjižnjice numpy.
