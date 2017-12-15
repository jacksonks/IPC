lista = []
cont = 0

for i in range(0,4):
    x = int(input("Informe um valor: "))
    lista.append(x)
    
print(lista)


for i in range(0,4):
    if (lista[i] % 6 == 0):
        cont += 1
        print("Numero divisivel por 6 na posicao ",i)
        print("numero:",lista[i])

print("Total de numeros divisiveis por 6:",cont)