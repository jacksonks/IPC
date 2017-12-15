par = 0
impar = 0

senha = input()
tamanho=len(senha)

for i in range(len(senha)):
    
    if(senha[i]%2 == 0 and (senha[i+1])%2 != 0):
        par+=1
        impar+=1
        print("senha segura")
        print(par+impar)
    elif(senha[i]%2 != 0 and (senha[i+1])%2 == 0):
        impar+=1
        par+=1
        print("senha segura")
        print(impar+par)
    else:
        print("senha insegura")
""""        
if(par+impar == tamanho):
    print("senha segura")
else:
    print("senha insegura")
"""