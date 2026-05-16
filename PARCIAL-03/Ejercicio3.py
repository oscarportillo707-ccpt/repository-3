def solicitarTemperaturas():

    temperaturas = []

    while len(temperaturas) < 5:

        try:

            temperatura = int(
                input(f"Ingrese la temperatura {len(temperaturas) + 1}: ")
            )

            temperaturas.append(temperatura)

        except ValueError:
            print("Error: ingrese un número entero válido.")

    return temperaturas


def evaluarTemperaturas(temperaturas):

    print("\n===== RESULTADOS =====")

    for temperatura in temperaturas:

        print(f"\nTemperatura registrada: {temperatura}")

        match temperatura:

            case temperatura if temperatura <= 0:
                print("Alerta: Punto de Congelación")

            case 100:
                print("Alerta: Punto de Ebullición")

            case _:

                estado = (
                    "Estado: Estable" if 10 <= temperatura <= 30 else "Estado: Crítico"
                )

                print(estado)


def main():

    temperaturas = solicitarTemperaturas()

    evaluarTemperaturas(temperaturas)


main()
