## primeramente planteamos la condición para ejecutar el programa


def transformaPalabra(palabra, opcion):
    if opcion == 1:
        print(palabra.upper())
    elif opcion == 2:
        print(palabra.lower())
    elif opcion == 3:
        print(palabra.capitalize())
    elif opcion == 4:
        print(palabra.title())
    elif opcion == 5:
        print(palabra.swapcase())
    else:
        print("Opción no válida")


# Programa principal

palabra = input("Ingresa una palabra: ")
numero = int(input("Ingresa una opción (1, 2, 3, 4 o 5): "))

transformaPalabra(palabra, numero)
