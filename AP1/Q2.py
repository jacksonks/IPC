#v1
senha=input()
i=0
aux=0

while(aux < len(senha)):
    if(int(senha[i])%2!=0 and (int(senha[i+1])%2==0)):
        aux+=2
        i+=2
    else:
        print("senha insegura")     
print("senha segura")
print(len(senha))

#v2
digito=input()

par=0
impar=0

tamanho=len(digito)

for i in range(tamanho):
    if(int(tamanho[i])%2!=0 and (int(tamanho[i+1])%2==0)):
        impar+=1
    elif(int(tamanho[i])%2==0 and (int(tamanho[i+1])%2!=0)):
        par+=1

if(impar + par == tamanho):
    print(True)
    print(impar+par)
else:
    print(False)
    print(impar+par)
    
