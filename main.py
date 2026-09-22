def suma_de_listas(lista1, lista2):
    linea = []
    for i in range(len(lista1)):
        sum_resultado = lista1[i] + lista2[i]
        linea.append(sum_resultado)
    return linea
    
def suma_de_matrices(matriz1, matriz2):
    columna = []
    for i in range(len(matriz1)):
        sum_resultado = suma_de_listas(matriz1[i], matriz2[i])
        columna.append(sum_resultado)
    return columna
print(suma_de_matrices(matrix1, matrix2))

def ordenamiento_por_insercion(lista): 
    lista_ordenada = lista[:] 
    for i in range(1, len(lista_ordenada)): 
        clave = lista_ordenada[i] 
        j = i - 1 
        while j >= 0 and lista_ordenada[j] > clave: 
            lista_ordenada[j + 1] = lista_ordenada[j] 
            j -= 1 
    lista_ordenada[j + 1] = clave 
    print(lista_ordenada)
    return lista_ordenada
