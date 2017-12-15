lista = []

while(len(lista) < 10):
    x=int(input())
    lista.append(x)
        
print(lista)
print(len(lista))

ordernar = True
while(ordernar):
    ordernar= False
    for i in range(len(lista)-1):
        if(lista[i] < lista[i+1]):
            ordernar = True
            aux = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = aux
print(lista)
