import string

def contaLetras(palavra):    
    letras = list(string.ascii_lowercase)
    cont = [0]*26
    
    
    for l in palavra:
        for i in range(26):
            if (l == letras[i]):
                cont[i] += 1
                
    
    for i in range(26):
        if (cont[i] != 0):
            print(letras[i],cont[i])
    
    

contaLetras("the quick brown fox jumps over the lazy dog")
