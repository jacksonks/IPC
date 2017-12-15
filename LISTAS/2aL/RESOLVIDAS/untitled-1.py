def iccanobirT(jack):
    n1=0
    n2=1
    n3=1
    n4=n1+n2+n3
    if(2 <= jack >= 0):
        return True
    else:
        while(n4 <= jack):
            n1=n2
            n2=n3
            n3=n4
            if(n4==jack):
                return True
jks=int(input())
if(iccanobirT(jks)):
    print("True")
else:
    print("False")
    
    
    
    
    
    
