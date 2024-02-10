'''
preguntar al usuario por dos numeros, se debe validar que ambos numeros sean mayor a "0"
si no es el caso, se debe parar la ejecucion del programa
se debe mostrar en pantalla el resultado la division del primero y el segundo y se debe indicar 
para cada numero si es par
'''
primer_numero = int(input("ingresar primer numero \n"))
segundo_numero = int(input("ingresr segundo numero \n"))
if(primer_numero > 0 and segundo_numero > 0 ):
    print (f"el resultado de la division del {primer_numero} y {segundo_numero} es igual a {primer_numero / segundo_numero}")
    if(primer_numero % 2 == 0):
        print("el primer numero es par")
    else:
        print("el primer numero no es par")

    if(segundo_numero % 2 == 0):
        print("el segundo numero es par")
    else:
        print("el segundo numero no es par")

else :
    print("por favor ingrese un numero mayor a 0")

           