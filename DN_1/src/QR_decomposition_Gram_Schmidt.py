import numpy as np

def Gram_Schmidt_QR_decomposition(matrix):
    # Pogoj za nadaljevanje: Matrika mora biti velikosti NxN
    if len(matrix[0]) != len(matrix[0]):
            raise ValueError("Matrika ni kvadratna")
    
    # Izračun števila stolpcev in vrstic
    num_columns = len(matrix[0])
    num_rows = len(matrix[0])

    # Ustvarimo matriko "a_list", ki vsebuje parametre a1, a2, a3.... an
    a_list = [list(row) for row in zip(*matrix)]

    # Ustvari prazno matriko velikosti num_rows x num_columns
    u_list = np.zeros((num_rows, num_columns))
    e_list = np.zeros((num_rows, num_columns))
    u_calculation = np.zeros((num_rows, num_columns))

    # Definicija U1 in E1
    u_list[0] = a_list[0]
    e_list[0] = u_list[0] / np.linalg.norm( u_list[0])

    # Računanje parametrov u1, u2, u3... un
    for i in range(1,len(a_list)):
        u_calculation = 0
        u_calculation = a_list[i]

        for j in range(0,i):
            u_calculation = u_calculation - (a_list[i] @ e_list[j])* e_list[j]
        u_list[i] = u_calculation
        e_list[i] = u_list[i] / np.linalg.norm(u_list[i])

    Q = np.transpose(e_list)
    R = np.zeros((num_rows, num_columns))

    for i in range (0, num_columns):
        for j in range (0,num_rows):
            R[i,j] = a_list[j] @ e_list[i]

    return (Q,R)


