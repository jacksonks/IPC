def dic(d):
    a = {}
    for i in d.keys():
        a[d.get(i)] = i
    return a

d = {"jackson" : 12345, "kelvin" : 13579, "souza" : 2468}
print(d)

print(dic(d))
    
