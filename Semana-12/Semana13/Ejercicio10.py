numeros = []
suma = 0

while suma <= 100:
    numero = int(input("Ingresa un número: "))

    if numero < 0:
        print("Número ignorado.")
    else:
        numeros.append(numero)
        suma += numero

print("Números válidos ingresados:")
for numero in numeros:
    print(numero)
