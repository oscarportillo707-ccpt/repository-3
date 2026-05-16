from decimal import Decimal


def main():

    total = Decimal("0")

    while True:

        try:

            precio = input("Ingrese el precio del producto ó (0 para salir): ")

            precioDecimal = Decimal(precio)

            if precioDecimal == 0:
                break

            total += precioDecimal

            print(f"Total acumulado: ${total}")

        except ValueError:
            print("Error: debe ingresar un número válido.")

        except:
            print("Error: entrada inválida.")

    print(f"\nTotal final acumulado: ${total}")


main()
