a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())

print(a,b,c,d,e)
print("o maior numero eh :")

if((a > b) and (a > c) and (a > d) and (a > e)):
    print(a)
elif((b > a) and (b > c) and (b > d) and (b > e)):
    print(b)
elif((c > a) and (c > b) and (c > d) and (c > e)):
    print(c)    
elif(d > a) and (d > b) and (d > c) and (d > e):
    print(d)    
else:
    print(e)