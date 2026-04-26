def pedirNumero():
    numero = int(input("Ingresa un número (0 para salir): "))
    return numero


def esPrimo(numero):
    if numero <= 1:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True


def mostrarPrimos(n):
    print("Números primos del 1 al", n, ":")

    for i in range(1, n + 1):
        if esPrimo(i):
            print(i)


def ejecutarPrograma():
    while True:
        numero = pedirNumero()

        if numero == 0:
            print("Programa finalizado.")
            break

        mostrarPrimos(numero)


ejecutarPrograma()
