import random

matriz = []
lista = []

for i in range(10):
    sublista = []
    for j in range(10):
        n = random.randint(1,100)
        sublista.append(n)
    matriz.append(sublista)
    

for i in range(10):
    for j in range(10):
        if (i % 2 == 0) and (matriz[i][j] % 5 == 0):
            lista.append(matriz[i][j])
            
for i in matriz:
    print(i)
            
print(lista)