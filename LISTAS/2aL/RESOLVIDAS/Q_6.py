#4,5,3=trianguloretangulo#
a=float(input())
b=float(input())
c=float(input())

if(a**2)==(b**2)+(c**2) or (a**2)==(c**2)+(b**2):
    print("eh triangulo")
elif(b**2)==(c**2)+(a**2) or (b**2)==(b**2)+(c**2):
    print("eh triangulo")
elif(c**2)==(a**2)+(b**2) or (c**2)==(a**2)+(b**2):
    print("eh triangulo")
else:
    print("nao faz triangulo")

