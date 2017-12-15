def crescente(a,b,c,d):
    if (a < b) and (a < c) and (a < d):
        x=a,b,c,d
        return x
    elif(a < c)  and (b < d) and (b < a):
        x=a,c,d,b
        return x
    elif(a < d) and (a < b) and (a < c):
        x=a,d,b,c
        return x


a=int(input())
b=int(input())
c=int(input())
d=int(input())
print(crescente(x))
