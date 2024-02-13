puntuacion = 125

if(puntuacion <= 30 and puntuacion >= 1):
    print("el usuario es de calificacion baja")
elif(puntuacion > 30 and puntuacion <= 60):
    print("el usuario es de calificacion media")
elif(puntuacion > 60 and puntuacion <=100):
    print("el usuario es de calificacion superior")
else:
    print("Por favor ingresar un numero entre 1 a 100")