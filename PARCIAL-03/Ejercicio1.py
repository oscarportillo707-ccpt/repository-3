def extraerCategoria(etiqueta):
    partes = etiqueta.split("-")
    categoria = partes[1][:]
    return categoria


def clasificarRuta(etiqueta):
    ruta = "Ruta Local" if etiqueta.endswith("SV") else "Ruta Internacional"
    return ruta


def main():

    while True:

        print("\n===== SISTEMA DE ENVÍOS =====")
        print("1. Ingresar etiqueta")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            etiqueta = input("Ingrese la etiqueta de rastreo: ")

            if etiqueta == "" or etiqueta is None:
                print("Error: La etiqueta está vacía. Fin")
                break

            partes = etiqueta.split("-")

            if len(partes) != 3:
                print("Error: formato inválido.")
                break

            categoria = extraerCategoria(etiqueta)

            print("\nCategoría:", categoria)

            resultadoRuta = clasificarRuta(etiqueta)

            print(resultadoRuta)

        elif opcion == "2":

            print("Finalizando el programa")
            break

        else:
            print("Opción inválida.")


main()
