#' # Vaja 02 - Linearni sistemi

#' Reši sistem linearnih enačb
#' ```
#'  x + 2y - 7 = 1
#'  2x - y -3z = 2
#'  x - z = 3
#' ```
#' Če želimo sistem rešiti z računalnikom, ga moramo spremeniti v matrično obliko 
#' $Ax = b$.

A = [1 2 -1; 2 -1 -3; 1 0 -1.0] # matrika sistema

b = [1, 2, 3] # desne strani

x = A \ b # rešitev sistema $A x = b (A \ b = A^{-1}b)$

#' Preiskus naredimo tako, da preverimo, če je $Ax -b$ enak 0.

A * x - b

#' Sistem lahko rešimo tudi z LU razcepom, tako da sistem $LUx=b$ prevedemo
#' na dva sistema $Ly=b$ in $Ux=y$.

using LinearAlgebra

L, U, p = lu(A)

x = U \ (L \ b[p])

norm(A * x - b, Inf)

#' Julia faktorje razcepa zapakira v en objekt.

F = lu(A)
x = F \ b

#' ## Tridiagonalne matrike

using Vaje02
T = Tridiag([1, 2], [3, 4, 5], [6, 7])

T[1, 1], T[1, 3]

#' Produkt matrike z vektorjem

T * [1, 2, 3]

#' Delejenje z leve oziroma operator `\`.

#' # Slučajni sprehod

"Generator naključnih števil porazdeljenih kot Bin(p)"
rand_bin(p) = (rand() < p) ? 1 : -1
[rand_bin(0.6) for i = 1:10]

# Slučajni sprehod 
sprehod(p, n) = cumsum([rand_bin(p) for i = 1:n])

sprehod(0.6, 10)
using Plots
scatter(sprehod(0.5, 100))

n = 100
p = 0.495
T = Tridiag(-p*ones(2*n-2), ones(2*n-1), -(1-p)*ones(2*n-2))
k = T\ones(2*n-1)
scatter(-n:n, k)