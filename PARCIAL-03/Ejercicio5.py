def solicitarNombre():

    while True:

        nombreCompleto = input("Ingrese su nombre completo: ")

        if nombreCompleto.replace(" ", "").isalpha():
            return nombreCompleto

        else:
            print("Error: ingrese un nombre válido.")


def transformarNombre():

    nombreCompleto = solicitarNombre()

    partesNombre = nombreCompleto.split()

    nombreInvertido = partesNombre[::-1]

    print("\n===== RESULTADO =====")

    for palabra in nombreInvertido:

        letrasSeparadas = ""

        for letra in palabra:

            letrasSeparadas += letra + "."

        print(letrasSeparadas[:-1])


def main():

    transformarNombre()


main()
