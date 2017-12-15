lista =[]
esc = []

for i in range (6):
    n=int(input())
    lista.append(n)
    
escalar=int(input())

for i in lista:
    a=i*escalar
    print(i,"x",escalar,"=",a)
    esc.append(a)
    
print(lista)
print(esc)