import numpy as np

class Givens:
  """
  Razred za shranjevanje zaporedja rotacij in indeksov vrstic pri QR razcepu z Givenssovimi rotacijami.

  Atributi:
    rotacije: Seznam parov [cos(α), sin(α)], ki predstavljajo rotacije.
    indeksi_vrstic: Seznam indeksov vrstic, na katere se rotacije nanašajo.
  """

  def __init__(self, rotacije, indeksi_vrstic):
    self.rotacije = rotacije
    self.indeksi_vrstic = indeksi_vrstic

  def __str__(self):
    return f"Rotacije: {self.rotacije}\nIndeksi vrstic: {self.indeksi_vrstic}"


def qr(H):
  """
  Funkcija za izračun QR razcepa matrike H tipa ZgornjiHessenberg z Givenssovimi rotacijami.

  Argumenti:
    H: Matrika tipa ZgornjiHessenberg.

  Vrne:
    Q: Matrika tipa Givens, ki shranjuje rotacije in indekse vrstic.
    R: Zgornje trikotna matrika.
  """

  n = H.shape[0]
  R = H.copy()
  Q = Givens([], [])

  for k in range(n - 1):
    # Izračun kota rotacije in vektorja p
    c, s = givens_rotacija(R[k + 1:, k])
    p = np.zeros(n)
    p[k + 1:] = R[k + 1:, k]
    p[k] = p[k + 1]

    # Posodobitev matrike R
    R[k + 1:, :] = np.dot(np.diag([1, c]), R[k + 1:, :]) - np.outer(s * p, p)

    # Posodobitev matrike Q
    Q.rotacije.append([c, s])
    Q.indeksi_vrstic.append(k + 1)

  return Q, R


def givens_rotacija(v):
  """
  Funkcija za izračun kota rotacije in vektorja p za Givenssovo rotacijo.

  Argumenti:
    v: Vektor, na katerega se rotacija nanaša.

  Vrne:
    c: Kosinus kota rotacije.
    s: Sinus kota rotacije.
  """

  v_norm = np.linalg.norm(v)
  c = v[0] / v_norm
  s = np.sign(v[0]) * np.sqrt(1 - c**2)
  return c, s


H = np.array([
  [2, 1, 0],
  [1, 3, 2],
  [0, 1, 4]
])

Q, R = qr(H)
print(f"Matrika Q:\n{Q}")
print(f"Matrika R:\n{R}")
