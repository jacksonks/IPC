fibonacci = []

i=0
anterior=0
atual=1

while(i < 100):
    anterior=atual
    atual=proximo
    proximo=anterior+atual
    fibonacci.append(anterior)
    i+=1
    
print(fibonacci)
print(len(fibonacci))
