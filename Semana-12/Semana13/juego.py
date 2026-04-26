def solicitarPalabra():
    palabra = input("Ingrese una palabra: ")
    transformandoPalabra = list(palabra.lower())
    return transformandoPalabra


def ListaACompletar(listaString):
    listaCompletar = [None] * len(listaString)
    return listaCompletar


def solicitarLetra():
    letra = input("Ingrese una letra: ").lower()
    return letra


def CompararListas(listaString, listaCompletar):
    letra = solicitarLetra()
    for i, PalabraTemporal in enumerate(listaString):
        if letra in PalabraTemporal:
            listaCompletar[i] = letra
    return listaCompletar


def DefinirIntentos(palabraAEncontrar):
    intentos = int(input("Ingrese la cantidad de intentos: "))
    return intentos + len(palabraAEncontrar)


def AplicarBucle():

    contador = 0
    palabraParaAdivinar = solicitarPalabra()
    listaCompletar = ListaACompletar(palabraParaAdivinar)
    intentos = DefinirIntentos(palabraParaAdivinar)
    while contador < intentos:
        lista = CompararListas(palabraParaAdivinar, listaCompletar)
        print(
            "".join(
                [sustituir if sustituir is not None else "_" for sustituir in lista]
            )
        )
        contador += 1
        print(f"Intentos restantes: {intentos - contador}")


AplicarBucle()
