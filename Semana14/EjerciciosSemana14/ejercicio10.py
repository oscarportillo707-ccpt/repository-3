def ordenarMenorAMayor(numeros):
    for i in range(len(numeros)):
        for j in range(i + 1, len(numeros)):
            if numeros[i] > numeros[j]:
                auxiliar = numeros[i]
                numeros[i] = numeros[j]
                numeros[j] = auxiliar

    return numeros


numeros = []

for i in range(6):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

ordenados = ordenarMenorAMayor(numeros)

print("Números ordenados:", ordenados)
