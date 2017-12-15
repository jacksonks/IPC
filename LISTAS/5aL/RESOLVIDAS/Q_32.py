def ordenar(lista):
    trocar = True
    while(trocar):
        trocar = False
        for i in range(len(lista)-1):
            if(lista[i] > lista[i+1]):
                trocar = True
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux

m = []

linhas = int(input("linhas: "))
colunas = int(input("colunas: "))

for i in range(linhas):
    lista = []
    for j in range(colunas):
        n = int(input("valores da matriz: "))
        lista.append(n)
    m.append(lista)
print("-------------------")
for i in range(linhas):
    ordenar(m[i])
    print(m[i])
