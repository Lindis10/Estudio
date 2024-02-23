'''
Elabore un listado de compra de medicamentos con datos pedidos a los clientes de una
farmacia, hasta el día de la compra ingresado sea “domingo”, en ese momento se debe parar
el programa. Los datos que se deben proporcionar son los siguientes: Día de la compra,
nombre del medicamento, marca, precio por unidad y cantidad a comprar. Almacene los datos
en una lista, que debe quedar como se ve en este ejemplo:
[[Día, nombre, marca, precio/unidad, cantidad], [Lunes, Acetaminofén, Laprof, 200, 5],
[Martes, Aspirina, Bayer, 850, 2], [Jueves, Loratadina, Genfar, 420, 10]]
'''

lista_dias = []
continua_ejecucion = True

while(continua_ejecucion):
    datos_de_la_compra = []
    datos_de_la_compra.append(input("ingrese día de la semana de la compra \n"))
    if(datos_de_la_compra[0] == "domingo"):
        continua_ejecucion = False
    datos_de_la_compra.append(input("ingrese nombre del medicamento \n"))
    datos_de_la_compra.append(input("ingrese nombre marca medicamento \n"))
    datos_de_la_compra.append(float(input("ingrese precio del medicamento \n")))
    datos_de_la_compra.append(int(input("ingrese la cantidad del medicamento \n")))

    lista_dias.append(datos_de_la_compra)

print(lista_dias)


