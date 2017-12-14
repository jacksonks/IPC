def coord(a,b):
    c = []
    for i in range(linhas):
        lista = []
        for j in range(colunas):
            zero=0
            if(a[i][j]==b[i][j]):
                lista.append(a[i][j])
            else:
                lista.append(zero)
        c.append(lista)
    return c

a = []
b = []
linhas = int(input("linhas: "))
colunas = int(input("colunas: "))

for i in range(linhas):
    lista1 = []
    for j in range(colunas):
        n = int(input("valores da matriz 1: "))
        lista1.append(n)
    a.append(lista1)

for i in range(linhas):
    lista2 = []
    for j in range(colunas):
        x = int(input("valores da matriz 2: "))
        lista2.append(x)
    b.append(lista2)
print("-------------------")
for i in range(linhas):
    print(a[i])
print("-------------------")
for i in range(linhas):
    print(b[i])
print(coord(a,b))
