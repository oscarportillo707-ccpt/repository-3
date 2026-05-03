# select case
# comparar elementos para poder ejectar una decicion.
Dias = ["Lunes", "Martes", "miercoles", "jueves", "viernes", "Sabado", "Domingo"]
# el santo grial de los  arreglos
#  inician en 0
# 0,1 = 2
# len(arreglo) un numero entero de elementos que tiene en su interior
Dias.append("Dia de las madres")  # agregar un elemento al final del arreglo
Dias.insert(4, "Dia del padre")  # agregar un elemento en una posicion especifica
saludos = "Hola desde"
for temporal in Dias:
    print(saludos + temporal)
