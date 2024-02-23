'''
Escribir un programa que almacene las asignaturas de un curso (física, química, historia,
matemáticas) en una lista y le pregunte al usuario su nombre y qué notas ha sacado en cada
curso) además se debe seguir preguntando a los usuarios su nombre y sus notas añadiendo a
una lista hasta que diga que no hay más usuarios. La lista queda de la siguiente manera:

[[nombre, física, química, historia, matemáticas], [Juan, 5 ,4,3,5],[Pedro,5,5,5,5], [Laura,5,5,5,5]]
'''

lista_estudiantes = []
numero_estudiantes = 3
lista_materias = ["fisica", "quimica", "historia", "matematicas"]

for i in range(0, numero_estudiantes):
    datos_usuario = []
    datos_usuario.append(input(f"Ingrese el nombre del usuario número {i + 1}: \n"))
    for materia in lista_materias:
        datos_usuario.append(float(input(f"Ingrese la nota de {materia} \n")))
    lista_estudiantes.append(datos_usuario)
    

print(f"{lista_estudiantes[0][0]} es muy bonita")

print(lista_estudiantes)





