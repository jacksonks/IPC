continuar = True

while (continuar):
    n = int(input("Informe um valor: "))
    if (n < 0):
        continuar = False
    else:
        fat = 1
        i = 1
        while (i<= n):
            fat *=i
            i+= 1
        
        print("O fatorial de ",n,"eh",fat)
        
        
        
    