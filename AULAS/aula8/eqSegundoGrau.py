a = float(input())
b = float(input())
c = float(input())
delta = 0.0

if (a != 0):
    delta = (b**2) - (4*a*c)
    if (delta > 0):
        x1 = (-b + (delta**(0.5)))/(2*a)
        x2 = (-b - (delta**(0.5)))/(2*a)
        print(x1,x2)
    elif (delta == 0):
        x1 = (-b)/(2*a)
        print(x1)
    else:
        print("Nao possui raizes reais")
else:
    print("A equacao nao eh de segundo grau")