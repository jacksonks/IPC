lista = []
x = int(input("Informe um valor: "))

while (x > 0):
    lista.append(x)
    print(lista)
    x = int(input("Informe um valor: "))
    
print("Estado final da lista")
print(lista)

for i in range(0,len(lista)):
    print(i,lista[i])