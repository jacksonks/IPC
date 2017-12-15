a=int(input())
b=int(input())
c=int(input())

print(a,b,c)
print("oq vc quer e isso")

if(a>b) and (a<c) or (a<b) and (a>c):
    print(a)
elif(b>c) and (b<a) or (b<c) and (b>a):
    print(b)
else:
    print(c)