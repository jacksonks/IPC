idade=int(input())

if(idade <=0):
    print("idade invalida!\npor favor digite uma idade valida!")
elif(idade >=18) and (idade <=65):
    print("eleitor obrigatorio")
elif(idade <16):
    print("nao eleitor")
else:
    print("eleitor facultativo")