matriz = []

for i in range(3):
    subLista = []
    for j in range(3):
        x = int(input())
        subLista.append(x)
    matriz.append(subLista)

for i in matriz:
    print(i)
    
for i in range(3):
    for j in range(3):
        if(i + j == 3):
            sub = matriz[i][i] - matriz[i][j]
            print(sub)


