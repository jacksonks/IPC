matriz = []
busca = False

for i in range(3):
    subL = []
    for j in range(3):
        a = int(input())
        subL.append(a)
    matriz.append(subL)

x = int(input())

for i in range(3):
    for j in range(3):
        if(x = matriz[i][j]):
            busca = True
            posicaoi = i
            posicaoj = j

if(busca):
    print("Posicao: %d%d": %(i, j))
else:
    print("Nao encontrado")
