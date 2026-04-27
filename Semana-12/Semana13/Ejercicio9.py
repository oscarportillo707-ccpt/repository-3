import random

numeroSecreto = random.randint(1, 30)
intentos = []

while True:
    intento = int(input("Adivina el número (1-30): "))
    intentos.append(intento)

    if intento == numeroSecreto:
        print("¡Correcto!")
        break
    elif intento < numeroSecreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")

print("Intentos realizados:")

for intento in intentos:
    print(intento)
