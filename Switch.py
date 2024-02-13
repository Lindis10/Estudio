resultado_operacion = "BAD_PARAMS"

match resultado_operacion:
    case "ERROR":
        print("Ups, hubo un error en el proceso")
    case "EXITO":
        print("proceso satisfactorio")
    case "BAD_PARAMS":
        print("Parametros mal ingresados")
    case _:
        print("resultado inesperado del proceso")