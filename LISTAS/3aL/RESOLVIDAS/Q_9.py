def quadrado(l):
    return l**2
def contar(soma,num):
    soma = soma + quadrado(num)
    return soma

n=int(input())

soma=0

for i in range(n):
        soma=contar(soma,i+1)
print(soma)
