matriz = [
    [0, 2, 0],
    [4, 5, 6],
    [7, 8, 0]
    ]

def suma_elementos(matriz):
    acumulador = 0
    for lista in matriz:
        for numero in lista:
            acumulador = acumulador + numero
    return acumulador

suma_elementos_matriz = suma_elementos(matriz)
print(f"La suma de los elementos de la matriz es: {suma_elementos_matriz}")


# Suma de los elementos de una columna de una matriz

def suma_de_una_columna(matriz, indice):
    acumulador = 0
    for lista in matriz:
        for indi, numero in enumerate(lista):
            if(indi == indice):
                acumulador += numero
    print(f"La suma de la columna {indice} es: {acumulador}")
suma_de_una_columna(matriz, 0)


#Indique si hay algun valor negativo en una matriz



def valor_negativo(matriz):
    contador = 0
    for lista in matriz:
        for numero in lista: 
            if(numero <0):
                contador += 1
    print(f"La cantidad de numeros negativos encontrados en la matriz es de {contador}")

valor_negativo(matriz)

#Columna con más ceros

def columna_con_ceros(matriz, numero_de_columnas_de_la_matriz):
    contador_de_ceros = [0]*numero_de_columnas_de_la_matriz
    for lista in matriz:
        for indi, numero in enumerate(lista):
            if(numero == 0): 
                contador_de_ceros[indi] += 1 
    indi_mayor = 0
    numero_mayor = contador_de_ceros[0]
    for indi, numero in enumerate(contador_de_ceros):
        if(numero > numero_mayor):
            numero_mayor = numero 
            indi_mayor = indi
    print(f"La columna con el mayor numero de ceros es {indi_mayor} con un total de {numero_mayor} ceros")
columna_con_ceros(matriz, 3)