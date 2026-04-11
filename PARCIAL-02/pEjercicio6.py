# Texto inicial
texto = "Oscar Javier Portillo"

# Normalización fuerte
texto_normalizado = texto.casefold()

# Eliminar espacios
texto_limpio = texto_normalizado.replace(" ", "")

# Verificar si contiene solo letras
es_alfabetico = texto_limpio.isalpha()

print("Texto normalizado:", texto_normalizado)
print("Texto sin espacios:", texto_limpio)
print("¿Contiene solo letras?:", es_alfabetico)
