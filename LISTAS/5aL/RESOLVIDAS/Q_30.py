lista = []

n=int(input())

lista.append(n)
print(lista)

for i in range(10-1):
    n = int(input())
    for j in range(len(lista)):
        if(n > lista[j]):
            aux=lista[j]
            lista[j]=n
            n=aux
    lista.append(n)
    print(lista)
    print(len(lista))
            
    
    
