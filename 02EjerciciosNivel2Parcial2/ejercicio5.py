'''
En la línea de llamadas de un hospital están indagando sobre los síntomas de enfermedad de
los pacientes, para identificar si tienen COVID 19. El boot debe hacer unas preguntas, y
almacenar las respuestas en una lista. Las preguntas son: Edad, ¿Tiene fiebre? ¿Tiene tos?
¿Tiene dificultades para respirar? ¿Tiene dolor de cabeza?. Estas preguntas solo se le hacen a
personas que sean mayores de edad, así que cuando una persona indique ser menor, no se le
pregunta nada más y el programa se termina. La información debe quedar almacenada en una
lista como ésta:
[[Edad, fiebre, tos, dificultad respiración, dolor de cabeza], [51, No, Sí, No, No], [21, No, No,
No, No, Sí], [18, Sí, No, Sí, Sí], [78, Sí, Sí, Sí, Sí]]
'''

base_de_datos = []
edad = 18
while(edad >= 18):
    edad = int(input("Ingrese su edad \n"))
    if(edad >= 18):
      pregunta_1 = input("¿Tiene fiebre? \n")
      pregunta_2 = input("¿Tiene tos? \n")
      pregunta_3 = input("¿Tiene dificultades para respirar? \n")
      pregunta_4 = input("¿Tiene dolor de cabeza? \n")
      base_de_datos.append([edad, pregunta_1, pregunta_2, pregunta_3, pregunta_4])
    else:
       print("El usuario debe ser mayor de edad para continuar")

print(base_de_datos)
