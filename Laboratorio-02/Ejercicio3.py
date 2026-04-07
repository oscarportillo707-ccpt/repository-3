def transformTexto(texto, opcion):
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    elif opcion == 4:
        return texto.title()
    elif opcion == 5:
        return texto.replace(" ", "")
    elif opcion == 6:
        return texto.swapcase()
    elif opcion == 7:
        return texto.split()
    elif opcion == 8:
        return str(len(texto))
    elif opcion == 9:
        return texto.join()
    elif opcion == 10:
        return len(texto.replace(" ", ""))
    else:
        return "Opción no válida"


# Programa principal
texto = input("Ingresa un texto: ")

print("\nOpciones:")
print("1. MAYÚSCULAS")
print("2. minúsculas")
print("3. Primer letra mayúsculas")
print("4. La primer letra de cada palabra en mayúscula")
print("5. Quitar espacios")
print("6. Invertir mayúsculas y minusculas")
print("7. Dividir la oración en palabras")
print("8. Contar caracteres")
print("9. Unir texto")
print("10. Contar caracteres (Sin espacios)")

opcion = int(input("Elige una opción: "))

resultado = transformTexto(texto, opcion)
print("Resultado:", resultado)
