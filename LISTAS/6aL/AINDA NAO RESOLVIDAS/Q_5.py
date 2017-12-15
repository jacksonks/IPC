animals = { 'a': ['aardvark '], 'b': ['baboon '], 'c': ['coati ']}
animals ['d'] = ['donkey ']
animals ['d']. append ('dog ')
animals ['d']. append ('dingo ')
animals ['d']. append ('cat ')

def quantos(dic):
    cont=0
    for i in dic.values():
        for j in i:
            cont+=1
    return cont

print(quantos(animals))
print(animals)
