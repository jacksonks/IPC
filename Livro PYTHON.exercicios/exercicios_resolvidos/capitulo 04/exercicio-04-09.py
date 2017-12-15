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
# Arquivo: exercicios_resolvidos\capitulo 04\exercicio-04-09.py
##############################################################################
valor=float(input("Digite o valor da casa:"))
salário=float(input("Digite o salário:"))
anos=int(input("Quantos anos para pagar:"))
meses = anos * 12
prestacao = valor / meses
if prestacao > salário * 0.3:
    print("Infelizmente você não pode obter o empréstimo")
else:
    print("Valor da prestação: R$ %7.2f Empréstimo OK" % prestacao)

