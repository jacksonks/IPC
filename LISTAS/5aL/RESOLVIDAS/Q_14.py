compra=[]
venda=[]

m10=0
m20=0
me=0

for i in range(5):
    pc=float(input())
    pv=float(input())
    compra.append(pc)
    venda.append(pv)

for i in range(5):
    lucro1=compra[i] + (compra[i]*0.10)
    dif=abs(compra [i] - venda [i])
    lucro2=compra[i] + (compra[i]*0.20)
    if(dif < lucro1):
        m10+=1
    elif(dif >= lucro1 or dif <= lucro2):
        me+=1
    else:
        m20+=1

print(compra)
print(venda)
print("menores que 10%:",m10,"maiores que 20 %:",m20,"entre 10 e 20 %:",me)
