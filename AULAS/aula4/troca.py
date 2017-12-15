variavel1 = 17
variavel2 = 19
aux = 0

aux = variavel1
variavel1 = variavel2
variavel2 = aux

print(variavel1,variavel2)
print("O valor da variavel auxiliar eh %d" % aux)