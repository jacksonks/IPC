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
# Arquivo: exercicios_resolvidos\capitulo 09\exercicio-09-29.py
##############################################################################
filmes = {
     "drama": ["Cidadão Kane","O Poderoso Chefão"],
     "comédia": ["Tempos Modernos","American Pie","Dr. Dolittle"],
     "policial": ["Chuva Negra","Desejo de Matar","Difícil de Matar"],
     "guerra": ["Rambo","Platoon","Tora!Tora!Tora!"]}

pagina = open("filmes.html","w", encoding = "utf-8")
pagina.write("""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Filmes</title>
</head>
<body>
""")
for c, v in filmes.items():
     pagina.write("<h1>%s</h1>" % c)
     for e in v:
         pagina.write("<p>%s</p>" % e)
pagina.write("""
</body>
</html>
""")
pagina.close()
