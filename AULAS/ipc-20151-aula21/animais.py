animais = {'a':'arara', 'b':'bodo','e':'enguia','c':'cobra','j':'jacare','t':['tracaja','tambaqui'],'p':'pirarucu'}

lista = animais.items()
print("Mapeamentos do  dicionario")
for l in lista:
    print(l)
    
for chave in sorted(animais.keys()):
    print(chave," mapeia para ",animais[chave])
    
resultado = animais.pop("b")
print(animais)
print(resultado)

valor = input("Informe o valor a ser deletado")
for k in animais.keys():
    if (animais[k] == valor):
        animais.pop(k)
        break
    
print(animais)
