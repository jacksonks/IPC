lista = []
cont30=0
contmm=0
contm=0
#soma=0
for i in range(0,5):
    x = int(input())
    lista.append(x)
    
print(lista)
media=((sum(lista))/5)
print(media)

for i in lista:
    if(i==30):
        cont30+=1
    elif(i > media):
        contmm+=1
    elif(i==media):
        contm=0
"""
for i in lista:
    soma+=i
r=(soma/5)
print(r)

for i in lista:
    if(i==30):
        cont30+=1
    elif(i > r):
        contmm+=1
    elif(i==media):
        contm=0
"""        
print("%i numeros são iguais a 30, %i são maiores que a media e %i são iguais a media." % (cont30,contmm,contm))
