positivos = 0
negativos = 0

while True:
    num = int(input("Ingresa un número (0 para terminar): "))

    if num == 0:
        break
    elif num > 0:
        positivos += 1
    else:
        negativos += 1

print("\nResumen de resultados:")

datos = [("Positivos", positivos), ("Negativos", negativos)]

for tipo, cantidad in datos:
    print(tipo + ":", cantidad)
