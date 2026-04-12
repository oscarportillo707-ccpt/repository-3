Serie = "fullmetal alchemits"

### cada variable tiene un espacio de memoria asignado

## cuando una vable cambia => se pierde la inmutabilidad
## POO
## polimorfismo -> es el cambio de acciones sin que se rompa el codigo
## abstracciones ->
##      Tasa de cafe
#       cafe coscafe
##       azucar
##      agua
##      otros ingredientes
##  un objeto es el que toma un modelo y este modelo le da funciones y utiliza sus propiedades

## Leon ->
## tiene ojos  (propiedades)
## tiene boca
## Esta guapo
##################
#  corre        ( Funciones )
# salta

## Clases
## Estructura de datos.


## es arreglo es una variable que tiene adentro otra variable
## Listas.
## Arrays.-> se inia a contar desde el 0
## tuplas.
## indices.


# -------------------------------------------------------
def saludo(nombres):
    print(nombres)


# saludo(Serie) las funciones simpre van  a tener ()
# -------------------------------------------------------
## las funciones tienen un espacio
## Scope es dond reciden las variables

## Colocar el nombre de la serie como titulo
fmaTemu = Serie.title()
# saludo(Serie)
# saludo(fmaTemu)
fnaMayusculas = Serie.upper()
saludo(fnaMayusculas)
## deprogracion Lineal
FullmetalCapitalizer = fnaMayusculas.swapcase().title()
## cuando encadenamos funciones se indica que la salidad de la funcion actual
# 3 es la entrada de la siguiente funcion.

saludo(FullmetalCapitalizer)

## compara cadenas de texo
comparar1 = "Ever"
comparar2 = "Ever"

# casefold para comparar y pasar a  minusculas
variableTemporal = comparar2.casefold()
comparar = comparar1.casefold() == comparar2.casefold()
# print(comparar)
## casefold nos dara true unicamente si los elementos son identicos sino nos indcara un false

## para verificar si es nu nuemero o un caracter vamos a utilizar isalfa()
clasicas2005 = "Gasolina"
comprarisAlpha = clasicas2005.isalpha()
# print(comprarisAlpha, 2005)
# isalpha nos va a dar true si el string que se le esta enviando es unicamente letras

## si lo que quiero es que sea solo numero  isalnum

letraCancion = " Los que paso, paso, entre tu y yo."  # 3 no tengo numeor
decada = "10"

ejemplo = letraCancion.isalnum()
# print(ejemplo)
ejemplo = decada.isalnum()
# print(ejemplo)
## isalnum verifica si la cadena de texto solo tiene numeros si solo tiene numeros nos va a dar tru
# si etiene u solo espacio dara false

## varificar que solo sean digitos
comprobarDecadas = decada.isdigit()
print(comprobarDecadas)

## si la Cadena de texto tiene numeros
siTieneNumero = "2026"
## este texto tiene nunero -> True
## isnumeric -> es un espacio en la memoria
## isnumeric() -> dentro del la funcion
respuesta = siTieneNumero.isnumeric()
print(respuesta)

## isnumeric como numeros que van a estar ejecutandose desde una
## cadena de texto

isLowerCase1 = "Ella se fue, me avandono y destrozo mi corazoon"
minusculas = isLowerCase1.islower()
## isLowerCase()
## isLowerCase.isLowerCase()
## true o false
print("solo minusculas", minusculas)

## 3 minutos
## Cristiano Leo sung

## solo debe de tener mayusculas
fraseIconioca = "Soltala Erika"
respuesta = fraseIconioca.isupper()
print(respuesta)

## tener un contenido -> entrada a las funcion que inicie con el .

respuesta = Serie.upper().isupper()
## esta funcion la vamos a encadenar con la otra >:)
print(respuesta)

respuesta = fraseIconioca.title().istitle()
print(fraseIconioca, respuesta)
## cuando una funcion retorna algo ( tipo de datos)
## string ->  espacio de memoria diferentes al de un espacio numerico
## int
# Float
## Decimal
## Boolean

# string  -> E v e r  -> lista o un array
# variable :
# tiene un tipo
# nobre sea unico ->  indice
# no puede inicar con variables
# va a tomar siempre el valor de la ultima modificacion
print(Serie)
Serie = "Chapulin Colorado"
print(Serie)
controlarEspacio = Serie.isspace()
print(controlarEspacio)
## islower
# isupper
# isspace
# isalnum
# isalpha

## Metodos de busqueda
tema = "En el bosque de china la chinita se perdio  "
#  E n e l b o s q u e  d

# si la cadena de texto tiene numeros

siTieneNumeros = "2026"
respuesta = siTieneNumeros.isnumeric()
print(respuesta)

isLowerCase1 = "Ella se fueeee, me abandonoooo"
minusculas = isLowerCase1.islower()
print("solo minusculas", minusculas)

nombres = "Cristiano Leo Song"
mayusculas = nombres.isupper()
print(mayusculas)

respuesta = nombres.title().istitle()
print(nombres, respuesta)


## title verifica si la inicial de la palabra es mayuscula

serie = "tiki taka"
print(serie)

# islower
# isupper
# isspace
# isalnum
# isalpha

## metodos de busqueda primeramente esta cadena de texto va verificada desde la izquierda ha derecha

temon = "en el bosque de la china ella se perdio"

temonf = temon.find("se")
print(temonf)


## desde la derecha ha izquierda

temonf = temon.upper().rfind("BOSQUE")
print(temonf)

poema = """Ella amará a otro hombre.
Yo voy lejos, andando hacia el olvido.
Y puede suceder que alguien me nombre,
pero ella fingirá no haber oído.

Ella amará a otro hombre:
el tiempo pasa y el amor finaliza,
y es natural que lo que fue una brasa
acabe convirtiéndose en ceniza."""

contador = poema.count("")
contador = poema.startswith("Ella")
contador = poema.endswith("Ceniza")
print(contador)

poemaModificado = poema.replace("Ella", "Lupita")
print(poemaModificado)
