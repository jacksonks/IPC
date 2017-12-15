vetor1 = []
vetor2 = []
vetor3 = []
vetorT = []

for i in range(9):
    a = int(input())
    vetor1.append(a)

for i in range(9):
    b = int(input())
    vetor2.append(b)

for i in range(9):
    c = int(input())
    vetor3.append(c)


vetorT.extend(vetor1[0:3])
vetorT.extend(vetor2[3:6])
vetorT.extend(vetor3[6:9])

print(vetor1)
print(vetor2)
print(vetor3)
print(vetorT)
