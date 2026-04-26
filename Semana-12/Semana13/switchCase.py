semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]


def pedirNumero():
    numero = input("Ingresa un número del 0 al 6: ")
    return numero


def ValidarNumero(numero):
    validarNumero = numero.isdigit()
    return validarNumero


def ValidarRangoDelNumero(numero):
    validarRangoDelNumero = int(numero) >= 0 and int(numero) <= 6
    return validarRangoDelNumero


def mostrarDiaDeLSemana(numero):
    match numero:
        case 0:
            print(semana[0])
        case 1:
            print(semana[1])
        case 2:
            print(semana[2])
        case 3:
            print(semana[3])
        case 4:
            print(semana[4])
        case 5:
            print(semana[5])
        case 6:
            print(semana[6])


def armarFuncion():
    dia = pedirNumero()
    validarDia = ValidarNumero(dia)
    validarRango = ValidarRangoDelNumero(dia)
    if validarDia and validarRango:
        mostrarDiaDeLSemana(int(dia))
    else:
        print("el numero ingresado no es valido")


armarFuncion()
