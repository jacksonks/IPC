senha=input()
i=0
aux=0

while(aux<len(senha)):
    if(int(senha[i])%2!=0 and (int(senha[i+1])%2==0)):
        aux+=2
        i+=2
    else:
        print("senha insegura")
print("senha segura")