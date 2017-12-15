n = int(input())

n1 = 0
n2 = 1
n3 = 1
proximo = n1+n2+n3
for i in range(n):
    print(n1)
    n1 = n2
    n2 = n3
    n3 = proximo
    proximo = n1+n2+n3