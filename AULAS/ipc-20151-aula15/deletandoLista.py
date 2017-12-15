lista = []
x = int(input("Informe um valor: "))

while (x > 0):
    lista.append(x)
    print(lista)
    x = int(input("Informe um valor: "))
    
print("Estado final da lista")
print(lista)

i = int(input("Informe a posicao a ser deletada: "))
del(lista[i])
print(lista)
