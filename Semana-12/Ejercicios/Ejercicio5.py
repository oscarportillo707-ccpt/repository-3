num1 = float(input("Ingresa el primer número: "))

num2 = float(input("Ingresa el segundo número: "))

operacion = input("Ingresa la operación (+, -, *, /): ")

if operacion == "+":
    resultado = num1 + num2
    print("La operación suma es:", resultado)

elif operacion == "-":
    resultado = num1 - num2
    print("La operación resta es:", resultado)

elif operacion == "*":
    resultado = num1 * num2
    print("La operación multiplicación es:", resultado)

elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
        print("La operación división es:", resultado)
    else:
        print("Error: No se puede dividir entre cero")

else:
    print("Operación no válida")
