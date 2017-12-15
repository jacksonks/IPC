a = []
b = []
c = []
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

for i in range(linhas):
    lista3 = []
    for j in range(colunas):
        sub = a[i][j] +((b[i][j])*(-1))
        lista3.append(sub)
    c.append(lista3)
print("-------------------")
for i in range(linhas):
    print(a[i])
print("-------------------")
for i in range(linhas):
    print(b[i])
print("-------------------")
for i in range(linhas):
    print(c[i])
