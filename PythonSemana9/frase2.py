# necesitamos solicitar una frase para ello

frase = input("Ingresa una frase: ")

# Eliminar los espacios
frase_sin_espacios = frase.replace(" ", "")

# Contar las letras
cantidad = len(frase_sin_espacios)

# Mostrar el resultado
print("Cantidad de letras (sin espacios):", cantidad)
