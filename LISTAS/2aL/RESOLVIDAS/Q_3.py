a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())

print(a,b,c,d,e)
print("o menor numero eh :")

if((a < b) and (a < c) and (a < d) and (a < e)):
    print(a)
    print("p.conj. 1")
elif((b < a) and (b < c) and (b < d) and (b < e)):
    print(b)
    print("p.conj. 2")
elif((c < a) and (c < b) and (c < d) and (c < e)):
    print(c)
    print("p.conj. 3")
elif(d < a) and (d < b) and (d < c) and (d < e):
    print(d)
    print("p.conj. 4")
else:
    print(e)
    print("p.conj. 5")
