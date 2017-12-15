matriz = []

def ehSuperior(matriz):
    result = True
    for i in range(3):
        for j in range(3):
            if(i > j):
                if(matriz[i][j]!=0):
                    result = False
    return result

def ehInferior(matriz):
    result = True
    for i in range(3):
        for j in range(3):
            if(i < j):
                if(matriz[i][j]!=0):
                    result = False
    return result

def ehIdentidade(matriz):
    result = True
    for i in range(3):
        for j in range(3):
            if(i != j):
                if(matriz[i][j]!=0):
                    result = False
            if(i == j):
                if(matriz[i][j]!=1):
                    result = False
    return result

for i in range(3):
    subLista = []
    for j in range(3):
        x = int(input())
        subLista.append(x)
    matriz.append(subLista)

for i in matriz:
    print(i)

print(ehIdentidade(matriz))

for i in range(3):
    for j in  range(3):
        if((i + j) > 2):
            print(matriz[i][j])
            
