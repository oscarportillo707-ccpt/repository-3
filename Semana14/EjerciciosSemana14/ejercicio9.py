def sumarPares(numeros):
    suma = 0

    for numero in numeros:
        if numero % 2 == 0:
            suma += numero

    return suma


numeros = []

cantidad = int(input("¿Cuántos números desea ingresar?: "))

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

print("Suma de números pares:", sumarPares(numeros))
