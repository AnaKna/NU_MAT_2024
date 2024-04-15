import numpy as np
from collections import namedtuple
from QR_decomposition_Gram_Schmidt import Gram_Schmidt_QR_decomposition


class SimetricnaTridiagonalna:
    """Simetrična tridiagonalna matrika"""

    def __init__(self, glavna_diagonala, zgornja_diagonala, spodnja_diagonala):
        """
        glavna_diagonala: Seznam elementov glavne diagonale.
        zgornja_diagonala: Seznam elementov zgornje diagonale.
        spodnja_diagonala: Seznam elementov spodnje diagonale.
        """
        
        if len(zgornja_diagonala) != len(glavna_diagonala) - 1:
            raise ValueError("Neveljavna dolžina zgornje diagonale.")
        
        if len(spodnja_diagonala) != len(glavna_diagonala) - 1 :
            raise ValueError("Neveljavna dolžina spodnje diagonale.")
        
        self.glavna_diagonala = glavna_diagonala
        self.zgornja_diagonala = zgornja_diagonala
        self.spodnja_diagonala = spodnja_diagonala

        self.n = len(self.glavna_diagonala)
        self.matrix = np.zeros((self.n, self.n))

        for i in range(self.n):
            self.matrix[i][i] = glavna_diagonala[i]

        for i in range(self.n-1):
            self.matrix[i][i+1] = self.zgornja_diagonala[i]   

        for i in range(self.n-1):
            self.matrix[i+1][i] = self.spodnja_diagonala[i] 

        for i in range(self.n):
                for j in range(self.n):
                    if self.matrix[i][j] != self.matrix[j][i]:
                        raise ValueError("Matrika ni simetrična.")

    def __str__(self):
        """
        Zapis matrike.
        """ 
        return str(self.matrix)
    
    def __len__(self):
        return self.n
    
    def __getitem__(self, index):
        if index < 0 or index >= self.n:
            raise IndexError("Index out of range")
        return self.matrix[index]

    
    def getindex(self, i, j):
        """
        Dostop do elementa matrike MATRIX[i][j]
        """
        element = self.matrix[i][j]
        return element

    def setindex(self, i, j, vrednost):
        """
        Sprememba vrednosti elementa MATRIX[i][j]
        """
        self.matrix[i][j] = vrednost
        return self.matrix
    
    def firstindex(self):
        """
        Prvi element matrike MATRIX[0][0]
        """
        return self.matrix[0][0]
    
    def lastindex(self):
        """
        Zadnji element matrike MATRIX[n][n]
        """
        return self.matrix[self.n - 1][self.n - 1]

    def multiply(self,matrika_ali_vektor):
        """
        Množenje matrike z matriko/vektorjem
        """
        mnozenje = np.dot(self.matrix,matrika_ali_vektor)
        return mnozenje






