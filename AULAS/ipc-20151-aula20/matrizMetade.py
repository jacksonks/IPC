import random

matriz = []

for i in range(4):
    sublista = []
    for j in range(5):
        n = random.randint(1,100)
        sublista.append(n)
    matriz.append(sublista)

for i in matriz:
    print(i)

metade = matriz[:]
for i in range(4):
    for j in range(5):
        metade[i][j] = matriz[i][j] /2
        

for i in metade:
    print(i)

