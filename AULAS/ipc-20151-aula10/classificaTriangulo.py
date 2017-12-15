def ehTriangulo(a, b, c):
    if ((abs(b-c) < a) and (a < (b + c))):
        return True
    else:
        return False

def classificaTriangulo(a,b,c):
    if (ehTriangulo(a,b,c)):
        if ((a ==b) and (a ==c)):
            return "Equilatero"
        elif ((a == b) or (a == c) or (b == c)):
            return "Isoceles"
        else:
            # Escaleno
            if ((a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or
                (c**2 == a**2  + b**2)):
                return "Retangulo"
            else:
                return "Escaleno"
    else:
        return "Nao eh Triangulo"
    
assert classificaTriangulo(3,4,5) == "Retangulo"
assert classificaTriangulo(3,3,3) == "Equilatero"
assert classificaTriangulo(3,4,6) == "Escaleno"
assert classificaTriangulo(2,2,1) == "Isoceles"
assert classificaTriangulo(-1,4,0) == "Nao eh Triangulo"