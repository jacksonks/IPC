#http://pt.wikipedia.org/wiki/Megabyte
#1 megabyte = 8 Megabits
#Mb = megabit e MB = megabyte (abreviatura de byte é com letra maiúscula).
# 60s - 1 min
# 12s - x
# 12/60 = 0,2 min


T=float(input("tamanho do arquivo? "))
V=float(input("velocidade do link? "))
T=T*8
V=T/V
x=V/60
print("%.2f minutos" % x)