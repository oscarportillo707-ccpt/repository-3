sumaImpar = 0
impares = []

while True:
    num = int(input("Ingresa un número o (0 para salir): "))

    if num == 0:
        print("Programa finalizado.")
        break

    if num % 2 != 0:
        sumaImpar += num
        impares.append(num)

print("Suma de números impares:", sumaImpar)

print("Números impares ingresados:")
for impar in impares:
    print(impar)
