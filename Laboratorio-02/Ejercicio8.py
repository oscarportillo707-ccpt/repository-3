def procesar_texto(texto, opcion):
    texto = texto.strip()

    if opcion == 1:
        return texto.isalnum()

    elif opcion == 2:
        return texto.isnumeric()

    elif opcion == 3:
        return texto.rfind("a")

    else:
        return "Opción inválida"


# Programa principal
while True:
    texto = input("\nIngresa un texto: ")

    print("\nMenú:")
    print("1. Verificar si es alfanumérico")
    print("2. Verificar si es numérico")
    print("3. Buscar desde el final")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    ## Validar que sea número
    if not opcion.isdigit():
        print("Debes ingresar un número")
        continue

    opcion = int(opcion)

    if opcion == 4:
        print("Programa finalizado")
        break

    resultado = procesar_texto(texto, opcion)
    print("Resultado:", resultado)
