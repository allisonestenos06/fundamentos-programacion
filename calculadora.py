# Realizar una calculadora
# Condicionales = if
# Casteos = str() int()
# Entradas = input()
# Operaciones = *, /, +, -
# Primer y segundo operador = castear por qué entra como string
# Sacar resultado

operador = input("Introduce un operador de los siguientes: *, /, +, - \n")
primer_operando = int(input("Introduce el primer número \n"))
segundo_operando = int(input("Introduce el segundo número \n"))

if operador == "*":
    print(primer_operando * segundo_operando)
elif operador == "/":
    print(int(primer_operando) / int(segundo_operando))
elif operador == "+":
    print(int (primer_operando) + int(segundo_operando))
elif operador == "-":
    print(int (primer_operando) - int(segundo_operando))