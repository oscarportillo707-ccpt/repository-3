def retomarPositivos(numeros):
    positivos = []

    for numero in numeros:
        if numero > 0:
            positivos.append(numero)

    return positivos


numeros = []

cantidad = int(input("¿Cuántos números ingresará?: "))

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

positivos = retomarPositivos(numeros)

print("Números positivos:", positivos)
