def auditarRegistros():

    for numero in range(1, 51):

        if numero == 42:
            print("\nAlerta de seguridad detectada.")
            break

        if numero % 3 == 0:
            continue

        print(f"Procesando registro ID: {numero}")


def main():

    auditarRegistros()


main()
