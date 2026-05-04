def pedirCantidadEstudiantes():
    while True:
        try:
            cantidad = int(
                input("Ingrese la cantidad de estudiantes Ó (0 para salir): ")
            )
            if cantidad < 0:
                print(
                    "La cantidad de estudiantes no puede ser negativa. Intente nuevamente."
                )
                continue
            return cantidad
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")


def pedirNombreEstudiante():
    while True:
        nombre = input("Nombre del estudiante: ")
        if nombre.replace(" ", "").isalpha():
            return nombre
        else:
            print(
                "El nombre no puede contener números ni símbolos. Intente nuevamente."
            )


def pedirFaltas():
    while True:
        try:
            faltas = int(input("Cantidad de faltas: "))

            if faltas < 0:
                print("Las faltas no pueden ser negativas. Ingrese positivas")
            else:
                return faltas

        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")


while True:
    cantidadEstudiantes = pedirCantidadEstudiantes()

    if cantidadEstudiantes == 0:
        print("Programa finalizado.")
        break

    for i in range(1, cantidadEstudiantes + 1):
        print(f"\n--- Estudiante {i} ---")

        nombre = pedirNombreEstudiante()
        faltas = pedirFaltas()

        if faltas == 0:
            estado = "A"
        elif faltas <= 3:
            estado = "B"
        else:
            estado = "C"

        match estado:
            case "A":
                print(f"{nombre}: Asistencia perfecta")
            case "B":
                print(f"{nombre}: Asistencia regular")
            case "C":
                print(f"{nombre}: Asiste poco a clase")
