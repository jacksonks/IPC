def bolha(lista):
    fim = len(lista)
    continuar = True
    while (fim > 1) and (continuar):
        trocou = False
        x = 0
        while (x < fim - 1):
            if (lista[x] > lista[x + 1]):
                trocou = True
                aux = lista[x]
                lista[x] = lista[x+1]
                lista[x+1] = aux
            x += 1
        if not trocou:
            continuar = False
        fim -= 1
        
lista = [ 20, 49, 99, 3, 0, 87, -1]
lista.sort()
print(lista)