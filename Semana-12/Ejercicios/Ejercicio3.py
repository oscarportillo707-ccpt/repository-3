nota = int(input("Ingresa una nota del 0 al 10: "))

if nota > 8 and nota <= 10:
    print("Excelente")
elif nota > 6 and nota <= 8:
    print("Bueno")
elif nota == 6:
    print("Aprobado")
elif nota >= 0 and nota < 6:
    print("Reprobado")
else:
    print("Nota inválida")
