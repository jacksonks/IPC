import random

matriz = []

for i in range(10):
    sublista = []
    for j in range(10):
        n = random.randint(1,100)
        sublista.append(n)
    matriz.append(sublista)
    
traco= 0
for i in range(10):
    traco += matriz[i][i]
    
for i in matriz:
    print(i)
            
print(traco)