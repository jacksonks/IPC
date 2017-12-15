import random

def bolha(lista):
    fim = len(lista)
    continuar = True
    while ((fim > 1) and (continuar)):
        x = 0
        trocou = False
        while (x < fim - 1):
            if (lista[x] > lista[x+1]):
                trocou = True
                aux = lista[x]
                lista[x] = lista[x+1]
                lista[x+1] = aux
            x+= 1
        if not trocou:
            continuar = False
        fim -= 1
        
matriz = []
for i in range(6):
    sublista = []
    for j in range(6):
        sublista.append(random.randint(1,100))
    matriz.append(sublista)

print("Matriz antes: ")
for linha in matriz:
    print(linha)
    
m1 = matriz.copy()
for linha in m1:
    bolha(linha)

print("-------------------------------")
print("Matriz depois:")
for linha in m1:
    print(linha)

m2 = matriz.copy()
listaTotal = []
for linha in m2:
    for elemento in linha:
        listaTotal.append(elemento)
        
bolha(listaTotal)
print(listaTotal)

indAux = 0
for i in range(6):
    for j in range(6):
        m2[i][j] = listaTotal[indAux]
        indAux += 1

print("-------------------------------")
print("Matriz totalmente ordenada:")
for linha in m2:
    print(linha)
