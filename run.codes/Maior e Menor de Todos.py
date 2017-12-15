org=True
maior=0
menor=0
cond=1
while(org):
    a=float(input())
    if(a<0):
        org=False
    elif (cond==1):
        maior= a
        menor= a
    else:
        if(a > maior):
            maior=a
        elif(a < menor):
            menor=a
    cond=cond+1
   #cond+=1
print(('"%0.2f %0.2f"') % (menor,maior))
"""
n=int(input())

while(n>0):
if(n>0):
maior=n
n=int(input())
"""
        
        
        
        
        

        
        

        
    

    
    
    
    
    
