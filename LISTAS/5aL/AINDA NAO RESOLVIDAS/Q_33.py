def lxl(lista1,lista2):
    for i in range(len(lista1)):
        print(lista2[i]*lista1[i])

lista1 = []
lista2 = []

for i in range(5):
    x=int(input())
    y=int(input())
    lista1.append(x)
    lista2.append(y)

print(lista1)
print(lista2)

lxl(lista1,lista2)
