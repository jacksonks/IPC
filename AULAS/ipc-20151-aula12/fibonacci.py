ant = 0
atual = 1
cont = 0

while (cont < 50):
    print(ant)
    prox = atual + ant
    ant = atual
    atual = prox
    cont += 1
