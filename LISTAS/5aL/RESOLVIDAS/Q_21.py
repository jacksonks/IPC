lista = []

for i in range(12):
    valor=int(input())
    lista.append(valor)

print(lista)

x=int(input("p:"))
y=int(input("s:"))

#soma de dois elementos no indice
soma1 = lista[x]+lista[y]
#soma dos elementos entre os indices
soma2 =(sum(lista[x:y])-lista[x])

print(soma1)
print(soma2)

    

