import random

matriz = []
linhas = int(input("Informe o numero de linhas: "))
colunas = int(input("Informe o numero de colunas: "))

for i in range(linhas):
    sublista = []
    for j in range(colunas):
        n = random.randint(1,100)
        sublista.append(n)
    matriz.append(sublista)

for i in range(linhas):
    print(matriz[i])