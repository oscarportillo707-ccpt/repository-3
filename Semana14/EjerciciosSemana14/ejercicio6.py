import random


def numerosMayoresQue50(numeros):
    contador = 0

    for numero in numeros:
        if numero > 50:
            contador += 1

    return contador


numeros = []

for i in range(10):
    numero = random.randint(1, 100)
    numeros.append(numero)

print("Números generados:", numeros)

cantidad = numerosMayoresQue50(numeros)

print("Números mayores que 50:", cantidad)
