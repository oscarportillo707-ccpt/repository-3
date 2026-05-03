# simular un juego
# ingresar una cantidad par de numeros
# debo emparejarlas con un texto
# debo dar un numero de intentos definido para el usuario
# prepara el buble y el select case

import random
from unittest import case  # esto es para generar numeros aleatorios

# Salvar el numero random en una variable
numero = random.randint(1, 6)
# print(numero)


def definirTargetas(numero):
    if numero % 2 == 0 and numero > 4:
        return numero
    else:
        return numero + 1


def optenerTargetas(_definirTargetas):
    tarjetas = []
    for i in range(_definirTargetas):
        tarjetas.append(input("Ingrese el texto para la propuesta "))
    return tarjetas


def validarTargetas(propuestaDelUsuario, llenarTargetas):
    # definir el numero de targetas
    i = 0
    for i in range(len(llenarTargetas)):
        match i:
            case 1:
                if llenarTargetas[1] == propuestaDelUsuario[1]:
                    print("Ganaste")
            case 2:
                if llenarTargetas[2] == propuestaDelUsuario[2]:
                    print("Ganaste")
            case 3:
                if llenarTargetas[3] == propuestaDelUsuario[3]:
                    print("Ganaste")
            case 4:
                if llenarTargetas[4] == propuestaDelUsuario[4]:
                    print("Ganaste")
            case 5:
                if llenarTargetas[5] == propuestaDelUsuario[5]:
                    print("Ganaste")
            case 6:
                if llenarTargetas[6] == propuestaDelUsuario[6]:
                    print("Ganaste")
            case 7:
                if llenarTargetas[7] == propuestaDelUsuario[7]:
                    print("Ganaste")
            case 8:
                if llenarTargetas[8] == propuestaDelUsuario[8]:
                    print("Ganaste")
            case 9:
                if llenarTargetas[9] == propuestaDelUsuario[9]:
                    print("Ganaste")
            case 10:
                if llenarTargetas[10] == propuestaDelUsuario[10]:
                    print("Ganaste")
            case _:
                print("Perdiste")
        i += 1


def inciar():
    numeroNovalidado = definirTargetas(numero)
    tarjetasParaAdivinar = optenerTargetas(numeroNovalidado)
    print("ahora van tus respuestas")
    AdivinandoTargetas = optenerTargetas(numeroNovalidado)
    validarTargetas(tarjetasParaAdivinar, AdivinandoTargetas)


inciar()

## Metodos http
## GET: obtener informacion
## POST: enviar informacion  Json,  Objeto js  claver : valor
## PUT: actualizar informacion
## DELETE: eliminar informacion
