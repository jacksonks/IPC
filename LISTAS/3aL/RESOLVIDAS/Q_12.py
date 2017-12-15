
def triangulo (a,b,c):
    if((abs(b-c) <a and (a< (b+c))):
       return True
    else:
       return False
   
def classificatriangulo(a,b,c):
    if(triangulo (a,b,c)):
        if((a==b) and (a==c)):
            return "equilatero"
        elif((a==b) and (a==c) or (b==c)):
            return "isoceles"
        elif((a!= b)  and (b!=c) and (a!=c)))
        return "escaleno"
    #escaleno
    if((a**2==b**2+c**2))
    else:
        return "retangulo"
    else:
        return "nao e triangulo"

    
a=float(input())
b=float(input())
c=float(input())

print(triangulo)

assert classificatriangulo (3,4,5) == "retangulo"