#' # Robni problem za Laplaceovo enačbo
#'  Rešujemo robni problem za Laplaceovo enačbo.

using Vaje03

rp = RobniProblemPravokotnikLaplace(
  [0, pi, -1, 1],
  [sin, sin, x -> 0.0, x -> 0.0]
)

Z = resi(rp, 0.1)

# ploskev narišemo z ukazom surface iz paketa Plots
using Plots
surface(Z[2:end-1, 2:end-1])

# Napolnitev Laplaceove matrike

L = laplaceova_matrika(10, 10)
spy(L)

using LinearAlgebra
F = lu(L)
# Faktorja L in U v razcepu imata
# več neničelnih elementov, kot originalna matrika.
spy(F.L)

spy(F.U)

#' ## Iterativne metode

Z = resi_iter(rp, 0.1, 1) # Gauss-Seidlova iteracija
surface(Z)

#' Poskusimo še za drug w

Z = resi_iter(rp, 0.1, 1.85)