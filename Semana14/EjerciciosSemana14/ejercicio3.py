def calcular_promedio(notas):
    suma = 0

    for nota in notas:
        suma += nota

    return suma / len(notas)


notas = []

cantidad = int(input("¿Cuántas notas ingresará?: "))

for i in range(cantidad):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)

promedio = calcular_promedio(notas)

print("Promedio:", promedio)

if promedio >= 6:
    print("El grupo APRUEBA")
else:
    print("El grupo REPRUEBA")
