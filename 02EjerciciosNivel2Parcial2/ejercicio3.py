
'''
Realice el programa para la inscripción de estudiantes a la ceremonia de grados, teniendo en
cuenta que hay un límite de cupos, que es un tercio del total de sillas del auditorio. La
información que se debe pedir para la inscripción es la siguiente: Nombres y apellidos,
facultad, nombre del programa y nivel de formación (tecnología, pregrado, maestría,
doctorado). Además, el programa debe guardar el número de registro de cada inscrito. Las
inscripciones deben quedar en una lista similar a ésta:

[[Nombre, facultad, programa, nivel de formación, Cód. Inscripción], [Ana Muñoz,
Odontología, Odontología, pregrado, 001], [Cristian Padilla, Ingeniería, Ingeniería Eléctrica,
pregrado, 002], [Omar Restrepo, Química Farmacéutica, Regencia de farmacia, tecnología,
003], [Sandra Arango, Educación, Maestría en Pedagogía, Maestría, 004]]
'''
import math

total_sillas_auditorio = 10
lista_estudiantes = []

for i in range(1, math.floor((total_sillas_auditorio / 3)) + 1):
    nombre = input(f"Inserte nombre y apellido del estudiante {i}: \n")
    facultad = input(f"Inserte facultad del estudiante {i}: \n")
    programa = input(f"Inserte programa del estudiante {i}: \n")
    nivel_formacion = input(f"Inserte nivel de formación del estudiante {i}: \n")
    codigo_inscripcion = ''
    if(i >= 1 and i <= 9):
        codigo_inscripcion = f'00{i}'
    elif( i >= 10 and i <= 99):
        codigo_inscripcion = f'0{i}'
    else:
        codigo_inscripcion = f'{i}'
    lista_estudiantes.append([nombre, facultad, programa, nivel_formacion, codigo_inscripcion])
print("NO SE PERMITEN MAS INSCRIPCIONES, EL AUDITORIO ALCANZÓ SU AFORO. ATT LINDA CAROLAY")

print(lista_estudiantes)
