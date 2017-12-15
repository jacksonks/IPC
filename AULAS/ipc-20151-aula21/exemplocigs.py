cigs = {}

continuar = True

while (continuar):
    resposta = input("Deseja continuar? S ou N ")
    if (resposta == 'N'):
        continuar = False
    else:
        animal = input("Informe um animal: ")
        chave = animal[0]
        if chave in cigs.keys():
            lista = cigs[chave]
            lista.append(animal)
        else:
            cigs[chave] = [animal]
        print(cigs)
        
        
chave = input("Informe uma chave: ")
erro = "Chave nao encontrada"
print(cigs.get(chave,erro))