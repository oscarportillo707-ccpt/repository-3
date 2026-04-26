while True:
    num = int(input("Ingresa un número o (-1 para salir): "))

    if num == -1:
        print("Programa finalizado.")
        break

    print("Tabla de multiplicar filtrada:")

    for i in range(1, 11):
        resultado = num * i

        if resultado > 20:
            print(num, "x", i, "=", resultado)
