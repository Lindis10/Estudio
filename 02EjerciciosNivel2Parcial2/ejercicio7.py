'''
La administración de un parqueadero desea almacenar los datos de sus clientes. Para eso,
envía un formulario a los números de celular que tienen almacenados en una lista. Los datos
que se piden en el formulario son: tipo de vehículo, marca, color y placa. Los datos deben
quedar en una lista como la siguiente, con un ejemplo de 4 números de celular:
[[Celular, tipo vehículo, marca, color, placa], [3110000000, Carro, Mazda, Negro, AAA 213],
[3214782723, Moto, Honda, Rojo, DES 23E], [3013892372, Carro, Renault, Verde, HAC 298],
[3215422529, Moto, Suzuki, Gris, JEW 88A]]
'''

base_de_datos = []
total_aforo_parqueadero = 10

for i in range(1, total_aforo_parqueadero + 1):
    pregunta_1 = input("Ingrese numero de celular \n")
    pregunta_2 = input("ingrese tipo de vehiculo \n")
    pregunta_3 = input("Ingrese la marca del vehiculo \n")
    pregunta_4 = input("Ingrese color del vehiculo \n")
    pregunta_5 = input("Ingrese la placa del vehiculo \n")
    base_de_datos.append([pregunta_1, pregunta_2, pregunta_3, pregunta_4, pregunta_5])
print(base_de_datos)