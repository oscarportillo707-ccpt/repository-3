def procesar_texto(texto, opcion):
    if opcion == 1:
        return len(texto.split())

    elif opcion == 2:
        return texto[::-1]

    elif opcion == 3:
        palabras = texto.split()
        palabras.sort()
        return " ".join(palabras)

    ## con esta condición lo que quiero es eliminar palabras

    elif opcion == 4:
        resultado = ""
        for letra in texto:
            if letra.lower() not in "aeiou":
                resultado += letra
        return resultado

    elif opcion == 5:
        resultado = ""
        for letra in texto:
            resultado += letra * 2
        return resultado

    else:
        return "Opción inválida"


# Programa principal
texto = input("Ingresa un texto: ")

print("\nOpciones:")
print("1. Contar palabras")
print("2. Invertir texto")
print("3. Ordenar palabras")
print("4. Eliminar vocales")
print("5. Duplicar letras")

opcion = int(input("Elige una opción: "))

resultado = procesar_texto(texto, opcion)
print("Resultado:", resultado)
