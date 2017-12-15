def estaOrdenado(lista):
    ordenado = True
    for i in range(len(lista)-1):
        if (lista[i] > lista[i+1]):
            ordenado = False
    
    return ordenado

print(estaOrdenado([1,2,3,4]))
print(estaOrdenado([1,2,9,4]))
print(estaOrdenado([1,1,1,1]))