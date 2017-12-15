"""
salario=[]

for i in range(5):
  valor=float(input())
  novo=(valor+(valor*0.08))
  salario.append(novo)
print(salario)
"""
s = []
n = []

for i in range(5):
    x=float(input())
    s.append(x)
    
print(s)

for i in s:
    novo=(i+(i*0.08))
    n.append(novo)
    print(novo)

print(n)