poema = """Es porque un pajarito de la montaña ha hecho
en el hueco de un árbol, su nido matinal,
que el árbol amanece con música en el pecho,
como que si tuviera corazón musical."""

contarletra = poema.count("a")

## en este espacio se usa este metodo para
# dividir el texto en líneas,
# creando una lista de oraciones

saltosLineas = poema.splitlines()

print("Número de veces que aparece la letra 'a':", contarletra)
print("Lista de oraciones:", saltosLineas)
