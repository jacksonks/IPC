def nxc(intpos,carac):
    for i in range(len(intpos)):
        print(carac[i]*intpos[i])

intpos = []
carac = []

n = int(input("numero: "))
for i in range(n):
    x = int(input("numeros: "))
    intpos.append(x)
    
for i in range(n):
    y=input("caracteres: ")
    carac.append(y)

nxc(intpos,carac)
