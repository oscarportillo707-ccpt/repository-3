notas = []

while True:
    nota = float(input("Ingresa una nota (-1 para terminar): "))

    if nota == -1:
        break

    if nota < 0 or nota > 10:
        print("Nota inválida.")
    else:
        notas.append(nota)

suma = 0

for nota in notas:
    suma += nota

if len(notas) > 0:
    promedio = suma / len(notas)
    print("Promedio:", promedio)
else:
    print("No se ingresaron notas válidas.")
