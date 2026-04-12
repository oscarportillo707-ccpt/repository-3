## declaramos la palabra
# como una variable de tipo string

texto = "CANTANDO"

texMinuscula = texto.lower()

texto_sin_sufijo = texMinuscula.removesuffix("ando")

indice_t = texto_sin_sufijo.find("t")

print("Texto en minuscula:", texMinuscula)
print("Texto sin sufijo:", texto_sin_sufijo)
print("Índice de 't':", indice_t)
