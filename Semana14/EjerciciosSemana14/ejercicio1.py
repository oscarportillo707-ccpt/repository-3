def contar_pares_impares(lista):
    pares = 0
    impares = 0

    for numero in lista:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    return pares, impares


entrada = input("Ingresa números separados por espacios: ")
numeros = [int(num) for num in entrada.split()]

pares, impares = contar_pares_impares(numeros)

print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)
