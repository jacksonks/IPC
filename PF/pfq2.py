soma=0
i=0
c=0.0
d=0.0
a=float(input())
b=float(input())
while(a < 200 and b < 200):
    dif=((a-c)**2+(b-d)**2)**0.5
    soma+=dif
    i+=1
    print(dif)
    a=float(input())
    b=float(input())
print("jogadas: ",i)
print("distancia : ",(soma/i))
