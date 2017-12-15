num=int(input())

i=1
divisor = 0
while( i <= num):
         if( num % i == 0):
                  divisor += 1
         i+=1
if( divisor == 2 ):
         print("eh primo")
else:
         print("Nao eh primo")
