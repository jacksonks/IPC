num = int(input())

i= 1

while( i * (i + 1) * (i + 2) <= num ):
    i += 1
i-=1
if( i * (i + 1) * (i + 2) == num) :
    print(num,"=",i,'*',i+1,'*',i+2)
    print(num,"=",i,'.',i+1,'.',i+2)
    print(num,"=",i,i+1,i+2)
else:
    print(num,"nao e produto de tres numeros sucessiveis")