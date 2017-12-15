def fatorial(n):
    fat=1
    x=1
    while (x<=n):
        fat*=x
        x+=1
    return fat

def soma(n):
    soma=0
    x=1
    while(x<=n):
        soma+=x
        x+=1
    return soma
    
def python(n):
    if(n%2!=0) and (n<=10):
        print(fatorial(n))
    elif(n%2==0) and (n>=10):
        print(soma(n))
    else:
        print("nao esta dentro dos condicoes desejads para este programa")

x=int(input())
print(python(x))
        
    
    
    
    
    
    
    
x=int(input())
print(python(x))