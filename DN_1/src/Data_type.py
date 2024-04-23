import numpy as np


class SimetricnaTridiagonalna:
    """Simetrična tridiagonalna matrika"""

    def __init__(self, glavna_diagonala, stranska_diagonala):
        """
        glavna_diagonala: Seznam elementov glavne diagonale.
        stranska_diagonala: Seznam elementov zgornje in spodnje diagonale.
        """
        
        if len(stranska_diagonala) != len(glavna_diagonala) - 1:
            raise ValueError("Neveljavna dolžina stranske diagonale.")
        
        self.glavna_diagonala = glavna_diagonala
        self.stranska_diagonala = stranska_diagonala
        self.n = len(self.glavna_diagonala)
        self.matrix = np.zeros((self.n, self.n))

        for i in range(self.n):
            if i < self.n-1:
                self.matrix[i][i+1] = self.stranska_diagonala[i] 
                self.matrix[i+1][i] = self.stranska_diagonala[i]
                self.matrix[i][i] = glavna_diagonala[i]
            else:
                self.matrix[i][i] = glavna_diagonala[i] 


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

        

    def __setitem__(self, point, value):
        """
        Sprememba ne-ničelnega elementa znotraj simetrične tridiagonalne matrike
        """
        i, j = point

        if i < 0 or i >= self.n or j < 0 or j >= self.n:
            raise IndexError("Indeks izven dosega")
        
        if i == j:
            self.glavna_diagonala[i] = value
            self.matrix[i][i] = value

        if i - j == 1:
            self.stranska_diagonala[j] = value
            self.matrix[i][j] = value
            self.matrix[j][i] = value
        
        if i - j == -1:
            self.stranska_diagonala[i] = value
            self.matrix[i][j] = value
            self.matrix[j][i] = value
        
        if(np.abs(i - j) > 1):
            raise IndexError("Indeks izven dosega")
        


    def __getitem__(self, index):
        if index < 0 or index >= self.n:
            raise IndexError("Index out of range")
        return self.matrix[index]

    
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

    def __mul__(self, other):
        return self.matrix * other
    
    def __matmul__(self, other):
        result = np.dot(self.matrix, other)
        return result


class ZgornjaDvodiagonalna:
    """Zgornje dvodiagonalna matrika"""

    def __init__(self, matrika):
        
        if len(matrika[0]) != len(matrika):
            raise ValueError("Matrika ni pravokotna.")
        
        row_num = len(matrika)

        self.matrika = matrika
        self.glavna_diagonala = np.zeros(row_num)
        self.nad_diagonala = np.zeros(row_num - 1)
        self.druga_nad_diagonala = np.zeros(row_num - 2)


        for i in range(0,row_num):
            self.glavna_diagonala[i] = matrika[i][i]

        for i in range(0,row_num-1):
            self.nad_diagonala[i] = matrika[i][i+1]
        
        for i in range(0,row_num-2):
            self.druga_nad_diagonala[i] = matrika[i][i+2]


    def __str__(self):
        """
        Zapis matrike.
        """ 
        return str(self.matrika)
    
    def __len__(self):
        return len(self.matrika)
    
    def __getitem__(self, index):
        if index < 0 or index >= len(self.matrika):
            raise IndexError("Index out of range")
        return self.matrika[index]
    

    def __mul__(self, other):
        return self.matrika * other
    

    def __matmul__(self, other):
        result = np.dot(self.matrika, other)
        return result
    


class Givens:
    """Zgornje dvodiagonalna matrika"""

    def __init__(self, rotacije, indeksi_vrstic):
        self.rotacije = rotacije
        self.indeksi = indeksi_vrstic

    def __str__(self):
        return f"Rotacije: {self.rotacije}\nIndeksi vrstic: {self.indeksi}"

