año = int(input("Ingresa el año: "))

if año <= 0:
    print("Ingresa un año válido")
else:
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print("El año es bisiesto.")
    else:
        print("El año no es bisiesto.")
