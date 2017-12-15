lista = []

while(len(lista) < 10):
    x=int(input())
    if(x % 2!=0):
        lista.append(x)
        
print(lista)
print(len(lista))