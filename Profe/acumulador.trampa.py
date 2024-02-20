'''
Acumulador: Similar al contador, es una variable numerica que utilizamos para llevar las cuentas de algo
pero en este caso lo usamos para acumular valores que vamos sumando

Ej:

acumulador = 0
'''
# Tenemos nuestro arreglo con x numeros
numeros = [3, 4, 2, 1, 2]

# Queremos almacenar en la variable acumulador la sumatoria de los elementos del arreglo
acumulador = 0

for numero in numeros:
    # Sumamos para cada iteración el número en cuestión a acumulador
    acumulador += numero # Este atajo es lo mismo que decir acumulador = acumulador + numero

# Imprimimos el resultado final
print(acumulador)

