v1 = float(input())
v2 = float(input())
op = input()


if (op == "+"):
    resultado = v1 + v2
    print(resultado)
elif (op == "-"):
    resultado = v1 - v2
    print(resultado)
elif (op == "*"):
    resultado = v1 * v2
    print(resultado)
elif (op == "/"):
    if (v2 == 0):
        print("Divisao por zero nao permitida")
    else:
        resultado = v1/v2
        print(resultado)
else:
    print("Operacao Invalida")