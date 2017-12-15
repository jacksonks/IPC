def comparar(l1,l2):
    cont=0
    for i in l1:
        if(i in l2):
            cont+=1
    if(cont==len(l1) and cont==len(l2)):
        return True
    else:
        return False

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 1, 2] 
c = [2, 5, 4, 1, 3]

print(comparar(a,b))
print(comparar(a,c))
