def mostrar_nombres_largos(nombres):
    print("Nombres con más de 5 caracteres:")

    for nombre in nombres:
        if len(nombre) > 5:
            print(nombre)


nombres = []

for i in range(10):
    nombre = input(f"Ingrese el nombre {i+1}: ")
    nombres.append(nombre)

mostrar_nombres_largos(nombres)
