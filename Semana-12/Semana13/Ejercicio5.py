contraseñaCorrecta = "python123"
intentos_fallidos = 0

while True:
    contraseña = input("Ingresa la contraseña: ")

    if contraseña == contraseñaCorrecta:
        print("Acceso concedido.")
        break
    else:
        print("Contraseña incorrecta.")
        intentos_fallidos += 1

print("Intentos fallidos:")
for i in range(1, intentos_fallidos + 1):
    print(i)
