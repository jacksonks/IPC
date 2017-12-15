matricula = []
media = []
def ordenar (media,matricula):
    for i in range(len(matricula)):
        for j in range(len(media)):
            if(matricula[i] >= media[j]):
                aux = matricula[i]
                matricula[i] = matricula[j]
                matricula[j] = aux
                
                aux1 = media[i]
                media[i] = media[j]
                media[j] = aux1
                
for i in range(4):
    valor=int(input())
    matricula.append(valor)
    nota=float(input())
    media.append(nota)

print(media)
print(matricula)
ordenar(media,matricula)
print(media)
print(matricula)
