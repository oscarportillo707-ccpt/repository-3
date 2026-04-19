## quiero que si es lunes dormir hasta las 8
## si es martes dormir hasta las 7
## si es miercoles dormir hasta las 6
## si es jueves dormir hasta las 5
## si es viernes dormir hasta las 4
## si no tengo tareas hacer ejercicio.

dia = input("Seleicione el dia de la semana ")

# Las funciones
# las funciones son constantes de codigo
# la funciones que tiene la posibilidad de introducir parametros
# def nombre():
#    print("Hola mundo") esto es lo que  realizara la funcion
dia = dia.lower().strip()
# esto es para convertir a minuscula y eliminar espacios en blanco


def selecionarDia(dia):
    if dia == "Lunes":
        print("Dormir hasta las 8")
    if dia == "Martes":
        print("Dormir hasta las 7")
    if dia == "Miercoles":
        print("Dormir hasta las 6")
    if dia == "Jueves":
        print("Dormir hasta las 5")
    if dia == "Viernes":
        print("Dormir hasta las 4")
    else:
        print("NO VOA TRABAJAR")


## las funciones logicas son las que tiene solo 2 estados
# verdadero como el amor de mama  ( true)
# falso como el para siempre que se dedican.(false)

# if una sola evaluacion
# else que por defecto del if
# elif para evaluar multiples acciones

selecionarDia(dia)


NOMBREtRAMITE = ""
## VALIDAR QUE SEA EL FORMATO QUE ESPERO
# MINUSCULA Y QUECOMPARE DOS VARIABLES

NOMBREtRAMITE = input("Ingrese el nombre del tramite: ")
nombreComparacion = input("Ingrese el nombre del tramite a comparar: ")

# 1- minuscula
NOMBREtRAMITE = (
    NOMBREtRAMITE.lower().strip().replace(" ", "")
)  ## pasa a minuscula y quito espacios
print(NOMBREtRAMITE)
# 2- comparacion
respuetaComparacionNombre = NOMBREtRAMITE.casefold() == nombreComparacion.casefold()
## compara que sea iguales
# 3- validar que no tenga numeros o espacios
print(respuetaComparacionNombre)
NombreSinnumerosOEspacios = NOMBREtRAMITE.isalnum()
print(NombreSinnumerosOEspacios)
# compara que no tengan nuemros o espacios

if respuetaComparacionNombre and NombreSinnumerosOEspacios:
    print("El nombre del tramite es correcto")


def transformar(nombre):
    nombre = nombre.lower()
    nombre = nombre.strip()
    nombre = nombre.replace(" ", "")
    return nombre


def validar(nombre, nombreComparacion):
    return nombre.casefold() == nombreComparacion.casefold() and nombre.isalnum()


nombre1 = transformar(NOMBREtRAMITE)
nombre2 = transformar(nombreComparacion)

if validar(nombre1, nombre2):
    print("El nombre del tramite es correcto")
else:
    print("El nombre del tramite es incorrecto")
