def suma_de_listas(lista1, lista2):
    linea = []
    for i in range(len(lista1)):
        sum_resultado = lista1[i] + lista2[i]
        linea.append(sum_resultado)
    return linea
list1 = [1, 2, 3]
list2 = [4, 5, 6]

print(suma_de_listas(list1, list2))

matrix1 = [[2, 3, 4], [5, 6, 7]]
matrix2 = [[1, 2, 1], [2, 1, 2]]



def suma_de_matrices(matriz1, matriz2):
    columna = []
    for i in range(len(matriz1)):
        sum_resultado = suma_de_listas(matriz1[i], matriz2[i])
        columna.append(sum_resultado)
    return columna
print(suma_de_matrices(matrix1, matrix2))