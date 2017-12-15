lista = []

for i in range(0,10):
    x = int(input("Informe um valor: "))
    lista.append(x)
    
print(lista)
print(min(lista))
print(max(lista))

menor = lista[0]

for i in range(0,10):
    if(lista[i] < menor):
        menor = lista[i]
        a = i
        
print("o menor numero eh: %i e sua posição eh: %i." % (menor,a))
