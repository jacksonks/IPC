def bbrr(jks,elemento):
    f=len(jks)-1
    i=0
    while(i <= f):
        m = ((i+f)//2)
        l=jks[m]
        if(elemento == l):
            return True
        if(elemento < l):
            f=m-1
        else:
            i=m+1
    return False

jks =[]

e=input()
while(e.replace('"',"").lower() != "fim"):
    jks.append(e.replace('"',"").lower())
    e=input()

ordenar = True
while(ordenar):
    ordenar= False
    for i in range(len(jks)-1):
        if(jks[i] > jks[i+1]):
            ordenar = True
            aux = jks[i]
            jks[i] = jks[i+1]
            jks[i+1] = aux

elemento=input()
print((jks),bbrr(jks,elemento.replace('"',"").lower()))
    
    


