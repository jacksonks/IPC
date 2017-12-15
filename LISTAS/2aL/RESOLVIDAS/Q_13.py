x=int(input())
y=int(input())

i=1
div1 = 0
div2 = 0
while( i <= x):
         if(x % i == 0):
                  div1 += 1
         i+=1
         while(i <= y):
                  if( y % i == 0):
                           div2 += 1
                  i+=1                  
if( div1 and div2 == 2 ) and (x-y==2):
         print("eh primo")
else:
         print("Nao eh primo")

"""
x=int(input())
y=int(input())

i=1
divisor = 0
while( i <= x) and ( i <= y):
         if( (x % i) == 0) and ( (y % i) == 0):
                  divisor += 1
         i+=1          
if( divisor == 2 ) and (x-y==2):
         print("eh primo")
else:
         print("Nao eh primo")
"""