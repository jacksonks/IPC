matriz = []
somacp = []
somali = []

for i in range(3):
    subLista = []
    for j in range(3):
        a = int(input())
        subLista.append(a)
    matriz.append(subLista)

for i in range(3):
    j = 0
    while j < 3:
        print(matriz[i][j])
        j += 1
    
for i in matriz:
    print(i)
    
print(somacp)

