idade = int(input("Informe a idade"))

if (idade < 16):
    print("Nao eleitor")
elif (( 18 <= idade) and (idade <= 65)):
    print("Eleitor obrigat�rio")
else:
    print("Eleitor facultativo")