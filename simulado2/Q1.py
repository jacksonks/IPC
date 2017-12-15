""""
def rr(lista,chave):
    for i in len(lista):
        if (chave == lista[i]):
            return True
        else:
            return False
"""        
def pesq(chave,lista):
    falso = False
    for i in range(len(lista)):
        if(chave == lista[i]):
            falso=True
    return falso

def uni(a,b):
    c = a[:]
    for i in range(len(b)):
        x=b[i]
        if(not pesq (x,c)):
            c.append(x)
    return c       

def inter(a,b):
    c = []
    for i in range(len(a)):
        x=a[i]
        if(pesq (x,b)):
            c.append(x)
    return c
    
def dif(a,b):
    c = []
    for i in range(len(a)):
        x=a[i]
        if((pesq (x,b)) == False):
            c.append(x)
    return c 

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 1, 2]
print(uni(a,b))
print(inter(a,b))
print(dif(a,b))
