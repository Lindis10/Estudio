# "==" es para validar igualdad entre ambos lados de una operacion
print(1 == 1)
# ">" Validar que la expresion del lado izq es mayor que el lado derecho
print(10 > 8)
print(8 > 10)
# "<" Valida que la expresion del lado izq es menor que el lado derecho
print(10 < 8)
print(8 < 10)
# "!=" Validar que ambos lados de la operacion son distintos
print(1 != 2)
print(1 != 1)
# ">=" Valida que el lado izq sea mayor o igual que el de la derecha
print(10 >= 10)
print(10 >= 12)
# "<=" Valida que el lado derecho sea mayor o igual al lado izq
print(10 <= 12)
print(12 <= 10)

# "and" Es verdadero cuando ambos lados de la expresion son verdaderos
print(10 <= 10 and 8 <= 8)
# "or" Es falso cuando ambos lados de la expresion son falsos, del resto, es verdadero
print(10 < 8 or 40 > 25)
print(10 > 12 or 25 >= 42)
# "not" negar lo que utilicemos
print(not 1 == 1)
print(not 1 != 1)