def circulo(r):
    r = (3.14 * (r**2))
    return r

def triangulo(b,h):
    r = ((b*h)/2)
    return r

def quadrado(l,l2):
    r = (l*l2)
    return r

def trapezio(b2,b3,a):
    r = (((b2+b3) * a)/2)
    return r

def retangulo(l3,al):
    r = (l3*al)
    return r

x=input("qual fitura geometrica desejas calcular:")

if(x=="circulo"):
    r = int(input())
    print(circulo(r))

elif(x=="triangulo"):
    b = int(input())
    h = int(input())
    print(triangulo(b,h))

elif(x=="quadrado"):
    l = int(input())
    l2 = int(input())
    print(quadrado(l,l2))

elif(x=="trapezio"):
    b2 = int(input())
    b3 = int(input())
    a = int(input())
    print(trapezio(b2,b3,a))

elif(x=="retangulo"):
    l3 = int(input())
    al = int(input())
    print(retangulo(l3,al))
else:
    ("entrada invalida!,entradas valdas sao circulo,triangulo,quadrado,trapezio e retangulo")