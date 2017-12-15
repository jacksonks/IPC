#v1
def a(m,n):
    if(m==0):
        return n+1
    elif(m!=0) and (n==0):
        return a(m-1,1)
    elif(m!=0) and (n!=0):
        return a(m-1,a(m,n))
    
m=int(input())
n=int(input())
print(a(m,n))
#v2
def a(m,n):
    if(m==0):
        x=n+1
        return x
    elif(m!=0) and (n==0):
        y=a(m-1,1)
        return y
    elif(m!=0) and (n!=0):
        z=a(m-1,a(m,n))
        return z
    
m=int(input())
n=int(input())
print(a(m,n))
