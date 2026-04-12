def transformarTexto(texto, opcion):
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    else:
        return None


# Programa principal
texto = input("Ingresa un texto: ")

## se agrega un while el programa se detendra hasta que el usuario lo desee

while True:
    print("\nOpciones:")
    print("1. MAYÚSCULAS")
    print("2. minúsculas")
    print("3. Primera letra mayúscula")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "4":
        print("Programa finalizado")
        break

    if opcion.isdigit():
        resultado = transformarTexto(texto, int(opcion))

        if resultado is not None:
            print("Resultado:", resultado)
        else:
            print("Opción no válida")
    else:
        print("Por favor ingresa un número válido")
