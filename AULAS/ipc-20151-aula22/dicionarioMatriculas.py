d = {'joao': 12345, 'maria': 4567, 'carlos' : 9823, 'cesar' :876421}

nome = input("Informe o nome do aluno: ")
print(d.get(nome,"Nao ha no dicionario"))

nome = input("Informe o nome do aluno: ")
if nome in d.keys():
    matricula = d.pop(nome)
    print(matricula)
else:
    print("Este aluno nao existe")
    
    
matricula = int(input("Informe a matricula"))
for chave in d.keys():
    if (d[chave] == matricula):
        print("A chave eh ",chave)
