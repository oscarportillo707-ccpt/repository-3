def transformarContar(texto, opcion):
    if opcion == 1:
        resultado = texto.upper()

    elif opcion == 2:
        resultado = texto.swapcase()

    elif opcion == 3:
        palabras = texto.split()
        resultado = "-".join(palabras)  # unir con guiones

    elif opcion == 4:
        resultado = ""
        for letra in texto:
            if letra.isalpha():  # solo letras
                resultado += letra

    else:
        return "Opción inválida", 0

    # aquí se hace la segunda parte
    cantidad = len(resultado)

    return resultado, cantidad


# Programa principal
texto = input("Ingresa un texto: ")

print("\nOpciones:")
print("1. MAYÚSCULAS")
print("2. Invertir mayúsculas y minusculas")
print("3. Unir palabras con guiones")
print("4. Dejar solo letras, sin espacios")

opcion = int(input("Elige una opción: "))

resultado, cantidad = transformarContar(texto, opcion)

print("Texto transformado:", resultado)
print("Cantidad de caracteres:", cantidad)
