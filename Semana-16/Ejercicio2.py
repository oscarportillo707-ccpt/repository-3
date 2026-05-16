# Sistema de gestión de estudiantes y notas

# Arrays (listas)
nombres = []
notas = []


# Función para clasificar la nota
def clasificar_nota(nota):
    if nota >= 9 and nota <= 10:
        return "Excelente"
    elif nota >= 7:
        return "Aprobado"
    elif nota >= 6:
        return "Regular"
    else:
        return "Reprobado"


# Bucle while para mantener el menú activo
while True:

    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Agregar estudiante y nota")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Mostrar promedio general")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    # Estructura match-case
    match opcion:

        case "1":
            nombre = input("Ingrese el nombre del estudiante: ")

            try:
                nota = float(input("Ingrese la nota del estudiante: "))

                if nota < 0 or nota > 10:
                    print("La nota debe estar entre 0 y 10.")
                else:
                    nombres.append(nombre)
                    notas.append(nota)

                    estado = clasificar_nota(nota)

                    print("Estudiante agregado correctamente.")
                    print(f"Estado: {estado}")

            except ValueError:
                print("Ingrese una nota válida.")

        case "2":
            if len(nombres) == 0:
                print("No hay estudiantes registrados.")
            else:
                print("\n===== LISTA DE ESTUDIANTES =====")

                # Bucle for
                for i in range(len(nombres)):
                    estado = clasificar_nota(notas[i])

                    print(
                        f"{i+1}. {nombres[i]} - "
                        f"Nota: {notas[i]} - "
                        f"Estado: {estado}"
                    )

        case "3":
            buscar = input("Ingrese el nombre a buscar: ")

            encontrado = False

            # Bucle for
            for i in range(len(nombres)):
                if nombres[i].lower() == buscar.lower():

                    estado = clasificar_nota(notas[i])

                    print("\nEstudiante encontrado:")
                    print(f"Nombre: {nombres[i]}")
                    print(f"Nota: {notas[i]}")
                    print(f"Estado: {estado}")

                    encontrado = True
                    break

            if not encontrado:
                print("Estudiante no encontrado.")

        case "4":
            if len(notas) == 0:
                print("No hay notas registradas.")
            else:
                suma = 0

                # Bucle for
                for nota in notas:
                    suma += nota

                promedio = suma / len(notas)

                print(f"Promedio general: {promedio:.2f}")

        case "5":
            print("Saliendo del programa...")
            break

        case _:
            print("Opción inválida. Intente nuevamente.")
