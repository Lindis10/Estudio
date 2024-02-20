'''
Dado un arreglo de numeros contar cuantos numeros impares hay y cuantos numeros pares hay
e indicar cuanto es la suma de pares e impares
'''

numeros = [2, 5, 8, 3, 9, 6, 7, 1, 4]
numeros_pares = 0
numeros_impares = 0
acumulador_pares = 0
acumulador_impares = 0
indice = 0

while(indice < len(numeros)):
    if(numeros[indice] % 2 == 0):
        numeros_pares += 1
        acumulador_pares += numeros[indice]
    else:
        numeros_impares +=1
        acumulador_impares += numeros[indice]
    indice += 1
print(f"la cantidad de numeros pares es de {numeros_pares}")
print(f"la cantidad de numeros impares es de {numeros_impares}") 
print(f"la sumatoria de los numeros pares es de {acumulador_pares}")
print(f"la sumatoria de los numeros impares es de {acumulador_impares}")

