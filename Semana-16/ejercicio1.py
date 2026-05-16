# agregar una lista de estudiantes
# definicion de una tupla
# las tuplas son elementos que nos permiten guardar valores
# sin importar el tipo dentro de ellas

# frutas = ("manzana", "pera", "uva")
# print(frutas)

# datos = ("mayo", 10)0
# print(datos)

# dato.append(2)
# dato.append("Hola mundo")
# print(dato)

# tomar los alumnos
# asinarles una nota
# matricula1 = ( 1, "Jose Alfredo")
# matricula2= ( 2, "Jose Manuel")

# dato = []
# alumno1 = (1, "Manuel Jose", 7)
# alumno2 = (2, "Maurinho ricardo", 9)
# alumno3 = (1, "Manuel Del Sagrado corazon de Jesus", 9)
# dato.append(alumno1)
# dato.append(alumno2)
# dato.append(alumno3)

# print(dato[0][1])

# Agregar estudiantes y sus notas.
alumno1 = (1, "Rouse Jackson", 8, "Ingles", "registrado")
alumno2 = (2, "Jackson Dousen", 4, "Natacion", "sin matricula")
Alumno3 = (3, "Maide Icerber", 10, "boxeo", "registrado")
alumno4 = (4, "Jhonatan Wick", 9, "Danza moderna", "sin matricula")
alumno5 = (5, "Neimar del nombre de Jesus ", 10, "Actuacion", "Expulsado")
Alumno6 = (6, "Nicolas Tesla", 10, "electricidad", "registrado")


TercerGrado = [alumno1, alumno2, Alumno3, alumno4, alumno5, Alumno6]
i = 0
nombres = []
matriculados = []

for grado in TercerGrado:
    nombres.append(TercerGrado[i][1])
    i += 1
print(nombres)


def estudiantesMatriculados(ListaDeEstudiantes):
    # una variable de una funcion es la variable que esta limitada
    # a usarse dentro de una funcion
    # SOLID -> que las clases deben de estar abiertas al aregar  nuevas funciones
    # pero deben de estar cerradas a la modificacion
    j = 0
    matricula = []
    for revision in TercerGrado:
        if revision[j][4] == "registrado":
            matricula.append(revision[j][4])
        else:
            pass  # un comodin para que la funcion no falle apesar de no tener logica de ejecucion

        j += 1


print(nombres)


# for i=0; len(ingredientes):
# este for especifico nos va a dar la opcionde controlar los pasos
# nosotros vamos a decidir cuando termina

# foreach
# For variabletemporal in Lista a iterar
# For  va hacer la listade metal del 2025   in el valor de lalista que recorre
# Foreach se usa cuando lo que se va a iterar es un objeto
# iterable  len() -> cantidad de elementos
# si no tiene nada o esta en el ultimo item del ejemplo devolvera -1
