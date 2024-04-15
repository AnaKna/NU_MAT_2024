module Vaje01

"""
  x0 = zacetni_priblizek(a)

Izračunaj začetni približek za kvadratni koren števila `a` z uporabo eksponenta števila s
plavajočo vejico. 
"""
function zacetni_priblizek(a)
  exp = div(exponent(a), 2) # sqrt(2^x) = 2^(x/2)

  if exp > 0
    return 1 << exp # magični začetni približek 2^(exp/2)
  else
    return 1 / (1 << -exp)
  end
end

"""
  y = koren(x)

Izračunaj vrednost kvadratnega korena danega števila `x˙. 
"""
function koren(a)
  x0 = zacetni_priblizek(a)
  for i = 1:10
    x = (x0 + a / x0) / 2
    if abs(x - x0) < 5e-11
      println("Število korakov $i")
      return x
    end
    x0 = x
  end
  throw("Iteracija ne konvergira")
end

export koren

end # module Vaje01
