def ehPrimo(n):
  cont = 0
  for i in range(2,n):
    if (n % i == 0):
      cont += 1
      
  if (cont == 0):
    return True
  else:
    return False
  
lista = []
listaPrimos  = []

n = int(input("Informe um valor: "))
while (n > 0):
  lista.append(n)
  n = int(input("Informe um valor: "))
  

for i in range(0,len(lista)):
  if (ehPrimo(lista[i])):
      listaPrimos.append(lista[i])
      
print(listaPrimos)