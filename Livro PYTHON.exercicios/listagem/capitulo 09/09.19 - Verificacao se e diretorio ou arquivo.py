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
# Arquivo: capitulo 09\09.19 - Verificacao se e diretorio ou arquivo.py
##############################################################################






import os
import os.path
for a in os.listdir("."):
     if os.path.isdir(a):
         print("%s/" % a)
     elif os.path.isfile(a):
         print("%s" % a)
