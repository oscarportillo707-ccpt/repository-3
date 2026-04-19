print("El while siempre lleva una orden logica")
# > <  !=  and or not

i = 0
# dia del mes 27 de abril

while i < 27:
    print(f"Mes abril fecha {i}")
    i += 1
## i += 1
## i = i + 1


## quiero hacer un juego de adivinar el nuemro
##  el bucle tendra una variable en true
## El numero de intetos debe ser 10
## y cuando atiene el numero  me imprima lo lograste
detener = True
numeroSecreto = 15
intentos = 0

while detener:

    if intentos > 10:
        break
    numero = int(input("Adivina el numero del 1 al 20: "))
    if numero < 0 and numero > 20:
        print("Numero no valido")
    elif numero == numeroSecreto:
        print("Lo lograste")
        detener = False
    intentos += 1
