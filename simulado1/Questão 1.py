peso=float(input())
altura=float(input())

imc=(peso/(altura**2))

print("imc = %.2f" % imc)


if(imc< 18.5):
    print("adulto baixo peso")
elif(imc >= 18.5) and (imc < 25.0):
    print("adulto com peso adequado")
elif(imc >=25.0) and (imc < 30.0):
    print("adulto sobrepeso")
else:
    print("adulto com obsidade")