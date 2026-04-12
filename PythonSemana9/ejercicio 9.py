# Solicitar una frase
frase = input("Ingresa una frase: ")

# Verificar si empieza con "Hola"
# para esto utilizaremos startswitch que sirve para verificar si las palabras o
# las frases empiezan por alguna letra o determinado simbolo

if frase.startswith("Hola"):
    print("La frase empieza con 'Hola'")
else:
    print("La frase no empieza con 'Hola'")
