c = []

for i in range(3):
    lista3 = []
    for j in range(3):
        x = int(input("append: "))
        lista3.append(x)
    c.append(lista3)
print("-------------------")
for i in range(3):
    print(c[i])
    
print("diferença")
for i in range(3):
    for j in range(3):
        dif = 0
        dif+ = c[i][i] - c[i]+[j][3-i]
        print(dif)
