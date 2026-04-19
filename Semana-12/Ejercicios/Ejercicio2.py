edad = int(input("Ingrese su edad: "))

if edad < 18:
    print("Eres menor de edad.")
elif edad >= 18 and edad <= 30:
    print("Eres mayor de edad.")
elif edad > 30 and edad < 60:
    print("Eres un adulto.")
elif edad >= 60 and edad < 80:
    print("Eres un adulto mayor.")
else:
    print("Eres un anciano.")
