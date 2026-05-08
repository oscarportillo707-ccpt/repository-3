# if condicio Logica :
#   si es verdad
# else
#    si es falsa

# el operador arlerno es la asignacion de un resultado a una variable

mayor = 45
menor = 900
intermedo = 6

if mayor > menor and mayor > intermedo:
    print("numeor mayor", mayor)
elif menor > mayor and menor > intermedo:
    print("Numero ", menor)
elif intermedo > mayor and intermedo > menor:
    print("numero", intermedo)


# el operador alterno
# variable =  valor que quiero
# que retorne si es verdadero if concion logica : else lo que manda cuando es false

resultado = mayor if mayor > intermedo else intermedo
resultado = intermedo if intermedo > menor else menor
resultado = menor if menor > intermedo else intermedo
print(resultado)


menu = []
menu.append("Pollo a la planchita")
menu.append("Camarones empanizado")
menu.append("Casamiento")
menu.append("Tortas de 1,50 con licuado")


def saberMenu(menu):
    respuesta = menu if len(menu) > 0 else "Ya se nos termino"
    return respuesta


##  len() -> juan carlos -> 400 - 1  iiterable


def selecionarComida():
    comidaSeleccionada = []
    menu1 = saberMenu(menu)
    count = 0
    for i in menu1:
        print(f"  Selecionar con el numero {count}")
        print(f"{menu1[count]} , seleccionar con el número {count}")
        if len(comidaSeleccionada) <= 0:
            comidaSeleccionada.append(menu1[count])
        else:
            continue
        count += count


def pediarComida():
    selecionarComida()


pediarComida()


# un objero es la forma en que las plantillas
# ( como clase ) urtilizan las definiciones ( modelo)
