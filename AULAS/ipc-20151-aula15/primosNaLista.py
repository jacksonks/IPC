x = int(input("Informe um numero: "))
lista = []

for i in range(2,x):
    if (x % i == 0):
        lista.append(i)
    

if (len(lista) == 0):
    print("Eh primo")
else:
    print("Nao eh primo")