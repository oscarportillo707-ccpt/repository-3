def Lista(listaPalabras, opcion):
    resultado = []

    for palabra in listaPalabras:
        if opcion == 1:
            resultado.append(palabra.upper())
        elif opcion == 2:
            resultado.append(palabra.lower())
        elif opcion == 3:
            resultado.append(palabra.capitalize())
        elif opcion == 4:
            resultado.append(palabra.count("a"))
        elif opcion == 5:
            resultado.append(palabra.join())
        elif opcion == 6:
            resultado.append(palabra.replace("Python", "Java"))
        else:
            return "Opción no válida"

    return resultado


# Programa principal
texto = input("Ingresa varias palabras: ")
lista = texto.split()  # separa en palabras

opcion = int(input("Elige una opción (1, 2, 3, 4, 5 o 6): "))

resultado = Lista(lista, opcion)
for palabra in resultado:
    print(palabra)
