def inverte(x):
    if(x > 0):
        ss=str(x)
        lol=ss
        if(len("x") == 4):
            return lol[::-1] 
        else:
            print("o numero digitado nao tem 4 digitos ou nao e positivo")
    
    
x=int(input())
print(inverte(x))
#srt=str(x)
#print(srt[::-1])
