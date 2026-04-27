while True:
    numero = int(input("Ingresa un número (0 para salir): "))

    if numero == 0:
        break

    for i in range(1, numero + 1):
        if i % 2 != 0:
            print("*" * i)
