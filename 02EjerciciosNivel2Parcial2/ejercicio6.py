'''
Un periódico nacional desea recopilar información de sus clientes a través del sitio web para
enviarle contenido personalizado a quienes deseen suscribirse. Si el cliente indica que quiere
suscribirse, se le pregunta el nombre, edad, ciudad de residencia, tema de interés y correo
electrónico. Elabore el programa que recopile los datos, el cual debe terminar cuando un
usuario indique que no desea suscribirse. Al final, la base de datos debe quedar similar al
siguiente ejemplo:
[[Nombre, edad, ciudad, tema , correo], [Cecilia, 43, Medellín, Salud, ceci@gmail.com],
[Antonio, 21, Bello, Tecnología, tonio@outlook.com], [Santiago, 34, Bogotá, Biología,
santi@gmail.com], [Daniela, 15, Astronomía, dani01@hotmail.com]]
'''

base_de_datos = []
desea_suscribirse = "si"

while(desea_suscribirse == "si"):
    desea_suscribirse = input("¿Desea suscribirse? \n")
    if(desea_suscribirse == "si"):
        pregunta_1 = input("Ingrese su nombre \n")
        pregunta_2 = int(input("Ingrese su edad \n"))
        pregunta_3 = input("Ingrese su cuidad de residencia \n")
        pregunta_4 = input("Ingrese su tema de interes \n")
        pregunta_5 = input("Ingrese su correo electronico \n")
        base_de_datos.append([pregunta_1, pregunta_2, pregunta_3, pregunta_4, pregunta_5])
    else:
        print("El usuario no desea suscribirse")
print(base_de_datos)
