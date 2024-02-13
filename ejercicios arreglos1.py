'''
dado un arreglo de 10 numeros llamado numeros para cada uno de ellos imprimirlo e indicar 
si es par o no 
'''

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    if(numero % 2 == 0):
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} no es par")