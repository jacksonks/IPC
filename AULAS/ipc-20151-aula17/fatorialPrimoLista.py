def fatorial(n):
    fat = 0
    for i in range(1,n+1):
        fat *= i
    return fat

def primo(n):
    cont = 0
    for i in range(2,n):
        if (n%i == 0):
            cont += 1
    
    if (cont == 0):
        return True
    else:
        return False
    
    
li = []
lf = []

for i in range(0,100):
    n = int(input())
    li.append(n)
    
for i in li:
    lf.append(fatorial(i))
    
cont = 0
for i in li:
    if (ehPrimo(i)):
        cont += 1

print(cont)
print(lf)