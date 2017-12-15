conj1 = []
conj2 = []
conjI = []

for i in range(0,10):
    n = int(input())
    conj1.append(n)
    
for i in range(0,20):
    n = int(input())
    conj2.append(n) 
    
for i in conj1:
    if i in conj2:
        conjI.append(i)
        
print(conjI)
