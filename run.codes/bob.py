string = input()

tamanho = len(string)

cont = 0

for i in range(tamanho):
    if(string[i:i+3] == "bob"):
        cont = cont + 1

print(cont)
