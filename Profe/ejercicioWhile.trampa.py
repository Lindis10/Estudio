'''
En un arreglo se guardan el número de invitados para la ceremonia de graduación de Linda de cada persona en 
el orden en que generan el requerimiento. Linda tiene muchos amigos entonces no puede permitir que las 
solicitudes sean de mas de 3 invitados, entonces, cualquier solicitud de mas de 3 invitados será descartada.

El salón social donde se realiza la fiesta tiene capacidad para 30 personas, debe imprimirse el número de 
solicitud hasta el cual el aforo da capacidad.

Debe utilizarse while.
'''
# Arreglo con solicitudes de invitación
solicitudes = [2, 3, 4, 7, 9, 3, 2, 1, 3, 2, 3, 3, 5, 7, 8, 3, 2, 1, 9, 3, 3, 6, 8, 3, 2, 3] 
invitados = 0 # Contador para saber si paramos de procesar solicitudes porque se completó el aforo
numero_solicitud = 0 # Cuando iniciamos hemos evaluado 0 solicitudes
solicitudes_aprobadas = []
solicitudes_rechazadas = []

while(invitados < 30 and numero_solicitud < len(solicitudes)):
    # Obtenemos el número de invitados de cada solicitud
    numero_invitados_solicitud = solicitudes[numero_solicitud]

    if(numero_invitados_solicitud <= 3 and invitados + numero_invitados_solicitud <= 30):
        invitados += numero_invitados_solicitud
        solicitudes_aprobadas.append(numero_solicitud)
    else:
        solicitudes_rechazadas.append(numero_solicitud)

    
    # Avanzamos a la siguiente solicitud
    numero_solicitud += 1
    
print(f"El número de solicitudes procesadas fue de {numero_solicitud} de un total de {len(solicitudes)} y el aforo final es de {invitados}")

# Linda dijo que necesita saber el número de solicitudes rechazadas con su indice y el de aprobadas

print(f"En total fueron {len(solicitudes_rechazadas)} solicitudes rechazadas")
print(solicitudes_rechazadas)
print(f"En total fueron {len(solicitudes_aprobadas)} solicitudes aprobadas")
print(solicitudes_aprobadas)
