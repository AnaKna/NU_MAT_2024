#' # Potenčna metoda
#' 
#' Iščemo lastni vektor matrike A za največjo lastno vrednost.

#' ## Invariantna mera za Markovsko verigo
P = [0.1 0.4 0.5;
  0 0.5 0.5;
  0.2 0 0.8]

using Vaje05

#' Invariantna mera je lastni vektor za $P^T$ za lastno vrednost 1.

p, lambda = potencna(P', ones(3))
p = p / sum(p)

#' Invariantna mera za Markovsko verigo na 6 vozliščih,
#'  ki definira dvodelni graf.

P = [
  0 0.3 0 0.4 0 0.3;
  0.1 0 0.2 0 0.7 0;
  0 0.5 0 0.2 0 0.3;
  0.4 0 0.2 0 0.4 0;
  0 0.5 0 0.2 0 0.3;
  0.4 0 0.2 0 0.4 0
]

using LinearAlgebra
eigen(P')

p, lambda = potencna(P', rand(6))

#' Če ima matrika A več različnih lastnih vrednosti,
#' ki so po absolutni vrednosti največje, potem potenčna metoda
#' ne konvergira za vsak začetni približek. V prejšnem primeru je
#' imela matrika lastne vrednosti 1 in -1. Problem rešimo s premikom.

B = P + I

p, lambda = potencna(B', rand(6))

p / sum(p) # normiramo, da dobimo verjetnostno porazdelitev

using Plots
scatter(p, title="Invariantna porazdelitev za MV na 6 točkah")