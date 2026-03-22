# las comillas triples son las que se encargan de hacer
# Cadenas de texto largas sin mdoficar el formato.
# texto corto
poema2 = (" Es porque un pajarito de la montaña ha hecho",)
"en el hueco de un árbol, su nido matinal"
"que el árbol amanece con música en el pecho",
"como que si tuviera corazón musical"


# textos largos ''' o """
poema = """Es porque un pajarito de la montaña ha hecho,
en el hueco de un árbol, su nido matinal,
que el árbol amanece con música en el pecho,
como que si tuviera corazón musical.

Si el dulce pajarito por entre el hueco asoma,
para beber rocío, para beber aroma,
el árbol de la sierra me da la sensación
de que se le ha salido, cantando, el corazón. """

## print(poema)

## computadora -> que variable queres imprimir
## print() =>
# void -> no devuelve nada
# objeto -> devuelve un tipo de dato

## realizar una wiki tambien pueder darle doble clic docuemtno y se les
## despligar el editor de texto

## MAYUSCULAS
## multabilidad  -> siempre debemos evitar transformar objeto original
## clases -> estereotipo (como un molde)
## propiedades ->
## color
#  tipo de motor ( electricos o de gas)
# Ojos
# color de pelo

# funciones -> string ( cadenas de texto) es un objeto
# moverse
# frenar
# cargarse
# descargarse

# poema es un espacio de memoria  para string
# se va a llenar con el contenido de  poema alterar con la accion Upper ( mayusculas)
poema_Mayusculas = poema.upper()
##print(poema_Mayusculas)

# convertir en minusculas
## string .lower

poema_minuscula = poema.lower()
##print(poema_minuscula)

## tiene que ingresar 100 nombres en mayuscula
mensaje = "hOlA kACe progRMando o qUe HaCe"
## Capitalize a que la primera letra de cada palabra sea mayuscula
mensajeCorrecto = mensaje.capitalize()
print(mensajeCorrecto)
## Las flipantess aventuras de el gato con bolson magico y alfredo
titulo = "Las flipantess aventuras de el gato con bolson magico y alfredo"
tituloCorrecto = titulo.title()
# print(tituloCorrecto)

## swapCase() permite cambiar entre mayusculas y minusculas
swapCaseTitulo = tituloCorrecto.swapcase()
print(swapCaseTitulo)
## numeros y letras
print("numeros y letras")
numeros_letras = nombre + numero
evaluarTexto = numeros_letras.isalnum()
print(evaluarTexto)
## verificar que solo sean numeros
print("verificar que solo sean numeros")
solo_numeros = numero.isdigit()
print(solo_numeros)
