jackson = []

b=str(input())
while(str(b) > "0"):
    jackson.append(b)
    b=str(input())
    
ordenar = True
while(ordenar):
    ordenar= False
    for i in range(len(jackson)-1):
        if( str(jackson[i]) > str(jackson[i+1]) ):
            ordenar = True
            aux = jackson[i]
            jackson[i] = jackson[i+1]
            jackson[i+1] = aux
a=("")
for j in jackson:
    a+= ", "+ j

print(jackson)
print(a)
c=(a.replace(", ","[",1)+"]")
print(c)
