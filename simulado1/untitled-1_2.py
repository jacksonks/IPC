digito=input()
par=0
impar=0
for i in range(len(digito)):
    if(int(digito[i])%2!=0) and (int(digito[i+1])%2==0):
        impar+=1
        par+=1
    elif(int(digito[i])%2==0) and (int(digito[i+1])%2!=0):
        par+=1
        impar+=1


if(impar + par == len(digito)):
    print(True)
    print(impar+par)
else:
    print(False)
    print(impar+par)
