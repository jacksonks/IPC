def imprime(n):
    if (n == 0):
        print(0)
    else:
        imprime(n-1)
        print(n)
        
        
imprime(9)