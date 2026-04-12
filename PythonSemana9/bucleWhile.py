clima = "soleado"
## entrada = input("¿Cómo está el clima? ")

## print("El clima es: ", entrada)

numeroComparar = 21

if numeroComparar >= 21:
    print("debes trabajar en la oficina")
else:
    print("puedes trabajar desde casa")

numer = 20

if numer > 21:
    print("su numero es mayor a 21")
elif numer == 21:
    print("su numero es igual a 21")
elif numer < 21:
    print("su numero es menor a 21")
else:
    print("no se ha podido comparar el numero")


edad = int(input("¿Cuál es tu edad? "))
edadNumber = int(edad)

if edadNumber >= 18 and edadNumber < 25:
    print("Eres mayor de edad, pero no puedes votar")
elif edadNumber >= 25 and edadNumber < 65:
    print("Eres mayor de edad, puedes votar y trabajar")
elif edadNumber >= 65:
    print("Eres mayor de edad, puedes votar, trabajar y jubilarte")
else:
    print("Eres menor de edad, no puedes votar ni trabajar")
