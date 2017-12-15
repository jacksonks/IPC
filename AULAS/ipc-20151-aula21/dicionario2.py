dic = dict(nome = "paulo",idade = 18,curso = "SI") 
print(dic)

informacao = input("Informacao sobre Paulo: ")
resposta = input("Resposta: ")

dic[informacao] = resposta
print(dic)

print(sorted(dic))
