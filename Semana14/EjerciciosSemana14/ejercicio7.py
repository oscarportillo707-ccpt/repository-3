def mayoresDeEdad(edad):

    mayores = []

    while edad > 0:

        edad = int(input("Ingrese su edad: "))
        if edad >= 18:
            mayores.append(edad)

    return mayores


mayores = mayoresDeEdad(0)
print("Personas mayores de edad:", mayores)
