p1 = []
p2 = []
media = []

for i in range(0,5):
    nota1 = float(input())
    nota2 = float(input())
    p1.append(nota1)
    p2.append(nota2)
    media.append((nota1 + nota2)/2)
    
for i in media:
    if (i >= 8):
        print(i)

mediaturma = (sum(media) / 5)

print(mediaturma)
print(p1)
print(p2)
print(media)
