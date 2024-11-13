# Programa que me dice si un número es par e impar
# Función que devuelve un booleano (true) si el número que le llega como argumento es par
# El usario introduce un número, se llama a la función, se comprueba el booleano y se imprime el resultado


def es_Par(numero):
    return numero % 2 == 0
numeroUsuario = int(input("Introduce un número\n"))
if es_Par(numeroUsuario):
    print("Es par")
else:
    print("No es par")