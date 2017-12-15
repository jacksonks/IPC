d1 = []
d2 = []
d3 = []
d4 = []
d5 = []

for i in range(5):
    x = float(input())
    y = float(input())
    z = float(input())
    a = float(input())
    b = float(input())
    d1.append(x)
    d2.append(y)
    d3.append(z)
    d4.append(a)
    d5.append(b)

print(d1)
print(d2)
print(d3)
print(d4)
print(d5)

"""
print(max(d1))
print(max(d2))
print(max(d3))
print(max(d4))
print(max(d5))
"""

maior = d1[0]

for i in range(5):
    if(d1[i] > maior):
        maior = d1[i]
print(maior)

maior = d2[0]

for i in range(5):
    if(d2[i] > maior):
        maior = d2[i]
print(maior)

maior = d3[0]

for i in range(5):
    if(d3[i] > maior):
        maior = d3[i]
print(maior)

maior = d4[0]

for i in range(5):
    if(d4[i] > maior):
        maior = d4[i]
print(maior)

maior = d5[0]

for i in range(5):
    if(d5[i] > maior):
        maior = d5[i]
print(maior)
