animais = {'a':'arara', 'b':'bodo','e':'enguia','c':'cobra','j':'jacare','t':'tracaja','p':'pirarucu'}
print(animais)
print(type(animais))
print(len(animais))
print(animais['j'])
print(animais.keys())

for key in animais.keys():
    print(animais[key])
    
n = input("Informe a chave que voce quer procurar: ")
if n in animais.keys():
    print(animais[n])
else:
    print("Chave nao existente")
