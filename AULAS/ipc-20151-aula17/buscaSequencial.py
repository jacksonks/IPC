def buscaSequencial(lista,chave):
    for i in lista:
        if (i == chave):
            return True
        
    return False
        
l = [25, 34, 67, 99, 12 , -1, 25]
chave = int(input("Informe um número"))

print(buscaSequencial(l,chave))