archivo = "OscarPortillo.txt"

textoSinSufijo = archivo.removesuffix(".txt")

# Paso 2: quitar el prefijo "ING. "
# en este caso no se encuentra este prefijo,
# pero se muestra el método para quitarlo,
# porque asi se pide en el ejercicio.

textoSinPrefijo = textoSinSufijo.removeprefix("ING. ")

archivo = textoSinPrefijo.lower()

## tambien en el ejercicio NO lo pide
# pero en la rubrica dice que se evaluara
# el uso de split, dividiendo por espacios, por eso lo implementé.

divTexto = archivo.split()

print("El texto final es:", archivo)
print("El texto dividido es:", divTexto)
