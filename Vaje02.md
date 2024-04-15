# Navodila za 2. vaje

## Linearni sistemi enačb

### Naloga 1
Reši primer linearnega sistema enačb z LU razcepom in z vgrajenim operatorjem `\`.

```math
  x + y -2z = 1
  x -y + z = 2
  2x -2z = 3
```

### Naloga 2

Definiraj podatkovni tip za tridiagonalno matriko in implementiraj operatorja `*` in `\` in
funkcijo `lu` za računanje LU razcepa brez pivotiranja.

Uporabi tridiagonalne matrike za obravnavo [slučajnega sprehoda](https://en.wikipedia.org/wiki/Random_walk). Izračunaj povprečno število korakov, ki jih potrebujemo da se od izhodišča oddaljimo za $k$ korakov.