'''
Cree el programa que almacena los productos nuevos en la base de datos de un
supermercado. Se debe pedir categoría del producto, marca, nombre y precio unitario.
Además, el programa debe asignarle automáticamente un código de identificación único a
cada producto. Al inicio del programa el usuario debe ingresar el número de registros que va
a realizar. Si el usuario va a ingresar 4 productos, la base de datos debe quedar en una lista
como la de este ejemplo:
[[Código, categoría, marca, nombre, precio], [01, Abarrotes, Aburrá, Frijol cargamanto, 4.500],
[02, Aseo, Ariel, Ariel en polvo 500g, 9300], [03, Bebidas, Postobón, Manzana 400ml, 2990],
[04, Abarrotes, Roa, Roa 500g, 2700]]
'''
numeros_de_registros = int(input("Ingrese el numero de registros a realizar \n"))
Base_de_datos = []

for i in range(1, numeros_de_registros + 1):
    categoria_del_producto = input(f"ingrese la categoria del producto {i}: \n")
    marca = input(f"Ingrese la marca del producto {i}: \n")
    nombre_del_producto = input(f"Ingrese el nombre del producto {i}: \n")
    valor_unitario = float(input(f"Ingrese el valor unitario del producto {i}: \n"))
    codigo_de_identificacion = ''
    if(i >= 1 and i <= 9):
        codigo_de_identificacion = f"0{i}"
    else: 
        codigo_de_identificacion = f"{i}"
    Base_de_datos.append([codigo_de_identificacion, categoria_del_producto, marca, nombre_del_producto, valor_unitario])

print(Base_de_datos)
