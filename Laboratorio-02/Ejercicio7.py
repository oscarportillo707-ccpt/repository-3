def transformar_texto(texto, opciones):
    resultado = texto

    for opcion in opciones:
        if opcion == 1:
            resultado = resultado.upper()
        elif opcion == 2:
            resultado = resultado.lower()
        elif opcion == 3:
            resultado = resultado.title()
        else:
            return "Opción inválida"

    return resultado


# Programa principal
texto = input("Ingresa un texto: ")

# El usuario ingresa números separados por espacio
entrada = input("Ingresa opciones (1, 2, 3) separadas por espacio: ")
lista_opciones = [int(x) for x in entrada.split()]

resultado = transformar_texto(texto, lista_opciones)
print("Resultado final:", resultado)
