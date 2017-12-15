#sem função, apenas com if,else,elif
par=int(input())
nj=int(input())

if(par > 0 and nj > 0):
    
    if(par==nj):
        print("par")
    elif(nj==1):
        print("hole-in-one")          
    elif(nj==par-1):
        print("birdie")  
    elif(nj==par-2):
        print("eagle")
    elif(nj<=par-3):
        print("double eagle")
    elif(nj==par +1):
        print("bogey")
    elif(nj >= par +2):
        print("double bogey")
else:
    
    print("erro")
#com função
def golf(par,nj):
    if(par > 0 and nj > 0):
        if(par==nj):
            return("par")
        elif(nj==1):
            return("hole-in-one")          
        elif(nj==par-1):
            return("birdie")  
        elif(nj==par-2):
            return("eagle")
        elif(nj<=par-3):
            return("double eagle")
        elif(nj==par +1):
            return("bogey")
        elif(nj >= par +2):
            return("double bogey")
    else:
        return ("erro")

par=int(input())
nj=int(input())
print(golf(par,nj))



