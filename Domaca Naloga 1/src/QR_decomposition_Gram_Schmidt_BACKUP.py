import numpy as np
from collections import namedtuple


def Gram_Schmidt_QR_decomposition(matrix):
    # Pogoj za nadaljevanje: Matrika mora biti velikosti NxN
    if len(matrix[0]) != len(matrix[0]):
            raise ValueError("Matrika ni kvadratna")
    
    # Izračun števila stolpcev in vrstic
    num_columns = len(matrix[0])
    num_rows = len(matrix[0])

    # Ustvarimo matriko "a_list", ki vsebuje parametre a1, a2, a3.... an
    a_list = [list(row) for row in zip(*matrix)]
    #print("LIST A: " + str(a_list))

    # Ustvari prazno matriko velikosti num_rows x num_columns
    u_list = np.zeros((num_rows, num_columns))
    e_list = np.zeros((num_rows, num_columns))
    #print("A LIST: " + str(a_list))
    u_calculation = np.zeros((num_rows, num_columns))

    # Definicija U1 in E1
    u_list[0] = a_list[0]
    e_list[0] = u_list[0] / np.linalg.norm( u_list[0])
    #print("E LIST: " + str(e_list))

    # Računanje parametrov u1, u2, u3... un
    for i in range(1,len(a_list)):
        u_calculation = 0
        u_calculation = a_list[i]

        for j in range(0,i):
            #print("CALCLUATING")
            #print(u_calculation)
            #print(a_list[i])
            #print(e_list[j])
            #print("j: " + str(j))
            #print("j: " + str(j) + " calculation u: " + str(u_calculation) + " - (" + str(a_list[i]) + " * "   + str(e_list[j]) + ") * " + str(e_list[j]))
            #print("j: " + str(j) + " calculation u: " + str(u_calculation) + " - (" + str(a_list[i] @ e_list[j]) + ") * " + str(e_list[j]))
            u_calculation = u_calculation - (a_list[i] @ e_list[j])* e_list[j]
            #print("U CALCULATION: " + str(u_calculation))
        u_list[i] = u_calculation
        e_list[i] = u_list[i] / np.linalg.norm(u_list[i])
        #print("MATRIX U : " + str(u_list))
        #print("E CALCULATION: " + str(u_list[i]) + " / " + str(np.linalg.norm(u_list[i])))
        #print("E CALCULATION: " + str(e_list[i]))
    Q = np.transpose(e_list)
    #print("KONČNA MATRIKA Q" +  str(Q))
    R = np.zeros((num_rows, num_columns))

    for i in range (0, num_columns):
        for j in range (0,num_rows):
            R[i,j] = a_list[j] @ e_list[i]



    
    threshold = 1e-15
    decimals = 5
    matrix = np.array(matrix)
    matrix_rounded = np.where(abs(matrix) < threshold, 0, matrix)
    matrix_rounded = np.round(matrix_rounded, decimals)
    Q_rounded = np.where(abs(Q) < threshold, 0, Q)
    Q_rounded = np.round(Q_rounded, decimals)
    R_rounded = np.where(abs(R) < threshold, 0, R)
    R_rounded = np.round(R_rounded, decimals)

    # Find the maximum column width for each column
    col_widths = [max(len(str(item)) for item in col) for col in zip(*matrix_rounded)]

    zapis = "\nOsnovna matrika:\n"
    for row in matrix_rounded:
        # Format each element in the row with spacing based on column width
        formatted_row = [f"{item:{col_widths[i]}}" for i, item in enumerate(row)]
        zapis = zapis + str(formatted_row) + "\n"
        #print("|"+ " | ".join(formatted_row) + "|")


    zapis = zapis + ("\n\nQ matrika:\n")
    col_widths = [max(len(str(item)) for item in col) for col in zip(*Q_rounded)]
    for row in Q_rounded:
        # Format each element in the row with spacing based on column width
        formatted_row = [f"{item:{col_widths[i]}}" for i, item in enumerate(row)]
        zapis = zapis + str(formatted_row) + "\n"
        #print("|"+ " | ".join(formatted_row) + "|")

    zapis = zapis + "\n\nR matrika:\n"
    col_widths = [max(len(str(item)) for item in col) for col in zip(*R_rounded)]
    for row in R_rounded:
        # Format each element in the row with spacing based on column width
        formatted_row = [f"{item:{col_widths[i]}}" for i, item in enumerate(row)]
        zapis = zapis + str(formatted_row) + "\n"
        #print("|"+ " | ".join(formatted_row) + "|")
    QR = zapis.replace("'","")
    #R_QtA = np.transpose(Q) @ A
    QRDecomposition = namedtuple('QRDecomposition', ['QR', 'Q', 'R'])

    return QRDecomposition(QR, Q, R)
