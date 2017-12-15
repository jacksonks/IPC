def ehTriangulo(a, b, c):
    if ((abs(b-c) < a) and (a < (b + c))):
        return True
    else:
        return False

def classificaTriangulo(a,b,c):
    if (ehTriangulo(a,b,c)):
        if ((a ==b) and (a ==c)):
            return "Equil�tero"
        elif ((a == b) or (a == c) or (b == c)):
            return "Is�celes"
        else:
            # Escaleno
            if ((a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == a**2  + b**2)):
                return "Ret�ngulo"
            else:
                return "Escaleno"
    else:
        return "Nao eh Triangulo"
    
a = float(input())
b = float(input())
c = float(input())
print(classicaTriangulo(a,b,c))