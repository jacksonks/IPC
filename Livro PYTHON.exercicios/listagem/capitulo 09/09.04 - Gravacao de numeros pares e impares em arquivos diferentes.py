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
# Arquivo: capitulo 09\09.04 - Gravacao de numeros pares e impares em arquivos diferentes.py
##############################################################################






ímpares = open("ímpares.txt","w")
pares = open("pares.txt","w")
for n in range(0,1000):
     if n % 2 == 0:
         pares.write("%d\n" % n)
     else:
         ímpares.write("%d\n" % n)
ímpares.close()
pares.close()
