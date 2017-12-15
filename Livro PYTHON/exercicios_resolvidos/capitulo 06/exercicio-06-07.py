##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2014
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Primeira reimpressão - Outubro/2011
# Segunda reimpressão - Novembro/1012
# Terceira reimpressão - Agosto/2013
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Site: http://python.nilo.pro.br/
# 
# Arquivo: exercicios_resolvidos\capitulo 06\exercicio-06-07.py
##############################################################################
expressão = input("Digite a sequência de parênteses a validar:")
x=0
pilha = []
while x<len(expressão):
    if(expressão[x] == "("):
        pilha.append("(")
    if(expressão[x] == ")"):
        if(len(pilha)>0):
            topo = pilha.pop(-1)
        else:
            pilha.append(")")  # Força a mensagem de erro
            break
    x=x+1
if(len(pilha)==0):
    print("OK")
else:
    print("Erro")
