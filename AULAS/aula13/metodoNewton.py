n = int(input("Informe um numero: "))

p = n/2

while (abs(p**2 - n) > 0.0001):
    p = (p + (n/p))/2
    
print("A estimativa para a raiz quadrada eh",p)