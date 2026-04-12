texto = "  el nido matinal  "

textoLimpio = texto.strip()
textoProcesado = textoLimpio.title()
textoFinal = textoProcesado.center(30, "-")

print("Texto sin espacios:", textoLimpio)
print("Texto con iniciales en mayúscula:", textoProcesado)
print("Texto final:", textoFinal)
