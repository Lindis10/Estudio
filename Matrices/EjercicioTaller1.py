matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

def suma_elementos(matriz):
    acumulador = 0
    for lista in matriz:
        for numero in lista:
            acumulador = acumulador + numero
    return acumulador

suma_elementos_matriz = suma_elementos(matriz)
print(f"La suma de los elementos de la matriz es: {suma_elementos_matriz}")
