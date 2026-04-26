while True:
    n = int(input("Ingresa un número (0 para salir): "))

    if n == 0:
        print("Programa finalizado.")
        break

    print("Números pares del 1 al", n, ":")

    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)
    print()
