x = int(input("Informe um numero: "))
y = int(input("Informe outro numero: "))
resultado = 0.0

if (y != 0):
    resultado = x/y
    print(resultado)
    
if (y == 0):
    print("Nao eh possivel dividir por zero")