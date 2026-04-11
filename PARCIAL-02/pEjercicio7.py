# Texto numérico
textNumber = "42"

# Rellenar con ceros a la izquierda hasta longitud 5
texto_relleno = textNumber.zfill(5)

# Verificar si termina en "2"
termina2 = texto_relleno.endswith("2")

print("Texto relleno:", texto_relleno)
print("¿Termina en '2'?:", termina2)
