## tomamos la cadena que el ejercicio indica

texto = "Python2026"

if texto.isalnum():
    texto = texto.lower()
    texto = texto.replace("2026", "")
    print("El texto Si es alfanumérico:", texto)
else:
    print("El texto no es alfanumérico")
