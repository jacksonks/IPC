def expoente(base,expo):
    if (expo == 0):
        return 1
    else:
        return base * expoente(base,expo - 1)
    
    
print(expoente(2,0))
print(expoente(3,9))