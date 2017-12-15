x=float(input())
maior=0
menor=0
if(x>=0):
    maior=x
    menor=x
    while(x>=0):
        if(x>maior):
            maior=x
        elif(x<menor):
            menor=x
        x=float(input())

print(('"%0.2f %0.2f"') %(menor,maior))

 
          
            
            

    


   


        
    
