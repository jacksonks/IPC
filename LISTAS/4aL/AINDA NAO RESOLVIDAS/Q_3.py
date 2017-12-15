def expoente(base,expo):
    if(expo==0):
        return 1
    else:
        return base * expoente(base,expo-1)
    
print(expoente(2,2))
print(expoente(2,3))
print(expoente(4,3))