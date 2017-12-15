lista = []
listapar = []

b=str(input())
while(b > "0"):
    lista.append(b)
    b=str(input())
    
for i in range(len(lista)):
    if(i % 2==0):
        listapar.append(lista[i])
        
print(lista)
print(listapar)  
#outro programa para verificar e adiconar a outras listas os elementos pares e impares se tratando de numeros.
"""
lista = []
listapar = []
listaimpar = []
for i in range(0,6):
    x = int(input("Informe um valor a ser adicionado a lista: "))
    lista.append(x)
    
for i in range(0,6):
    if(lista[i] % 2==0):
        listapar.append(lista[i])
    else:
        listaimpar.append(lista[i])
        
print(lista)
print(listapar)
print(listaimpar)
"""