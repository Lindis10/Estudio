resultado_operacion = "BAD_PARAMS"

match resultado_operacion:
# Nos sirve para validar posibles valores para una variable

    case "ERROR": # identificar los posibles valores y que hacer si se cumple
        print("Ups, hubo un error en el proceso")
    case "EXITO":
        print("proceso satisfactorio")
    case "BAD_PARAMS":
        print("Parametros mal ingresados")
    case _:
        print("resultado inesperado del proceso")