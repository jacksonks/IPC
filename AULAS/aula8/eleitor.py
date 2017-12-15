idade = int(input("Informe a idade"))

if (idade < 16):
    print("Nao eleitor")
elif (( 18 <= idade) and (idade <= 65)):
    print("Eleitor obrigatório")
else:
    print("Eleitor facultativo")