'''
crear un programa que dado un arreglo de cinco numeros nos muestre en pantalla la sumatoria
de los elementos del arreglo, debe utilizarse un acumulador y un while
'''
numeros = [1, 2, 3, 4, 5]
indice = 0
acumulador = 0
while(indice < len(numeros)):
    acumulador = acumulador + numeros[indice]
    indice = indice + 1
print(acumulador)