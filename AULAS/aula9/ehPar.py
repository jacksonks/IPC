def ehPar(x):
    if (x % 2 == 0):
        return True
    else:
        return False
    
assert ehPar(2)
assert not ehPar(5)
assert ehPar(0) == True
assert ehPar(-1) == False
assert ehPar(100) == True

tres = 3
print(hex(id(tres))[:-2])
tres = 5
print(hex(id(tres))[:-2])
outraVariavel = "Exemplo"
print(hex(id(outraVariavel))[:-2])