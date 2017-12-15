n = int(input())

i = 1
cont = 0
soma = 0
while (i < n):
    if (n % i == 0):
        cont += 1
        soma += i
    i+= 1

print(cont)
print(soma)


if (soma == n):
    print("Perfeito!")
elif (soma > n):
    print("Abundante!")
else:
    print("Defectivo!")