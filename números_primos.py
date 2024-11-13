# Dado un número que un usuario introduzca por teclado y que a través de un for, se compruebe si es primo


numero = int(input("Introduce un número: \n"))
es_primo = True
for i in range(2,numero):
    print(i)
    if (numero % i==0):
        es_primo = False
if (es_primo):
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")