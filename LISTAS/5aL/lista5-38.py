matriz = []
maior = 0

for i in range(3):
    subL = []
    for j in range(3):
        a = int(input())
        subL.append(a)
    matriz.append(subL)

for i in range(3):
    for j in range(3):
        if(maior == 0):
            maior = matriz[i][j]
        if(matriz[i][j] > maior):
            maior = matriz[i][j]

print(maior)
