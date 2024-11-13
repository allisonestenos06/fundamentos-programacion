# Pidan una entrada de texto al usuario y que en un bucle for se imprima cada una de sus letras


nombre = input("Introduce tu nombre: \n")
longitud_nombre = len(nombre)

for i in range(longitud_nombre):
    print(nombre[i])