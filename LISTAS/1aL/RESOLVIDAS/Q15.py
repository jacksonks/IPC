kw = float(input("KW consumido? "))
#vc = kw*0.34
vc = kw*0.35
#vc = kw*0.36
#vc = kw*0.37
#vc = kw*0.38
vd = vc - (vc*0.15)

print("valor consumo = %.2f" %vc)
print("valor de desconto = %.2f" %vd)
