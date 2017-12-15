def inverte(lista):
    b = lista[::-1]
    return b
lista = []
n=int(input())
for i in range(n):
    n=int(input())
    lista.append(n)

print(inverte(lista))
              
