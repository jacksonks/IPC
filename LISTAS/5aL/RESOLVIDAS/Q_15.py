L1 = []
L2 = []
L3 = []

for i in range(0,5):
    n = int(input())
    L1.append(n)
    
for j in range(0,5):
    n = int(input())
    L2.append(n) 
    
for i in L1:
    if i in L2:
        L3.append(i)
""""
for i in range(0,5):
    for j in range(0,5):
        if (L1[i]==L2[j]):
            L3.append(L2[j])
            print(L2[j])
"""
print(L1)
print(L2)
print(L3)