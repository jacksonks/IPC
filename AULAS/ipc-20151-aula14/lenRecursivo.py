def meuLen(s):
    if (s == ""):
        return 0
    else:
        return 1 + meuLen(s[1:])
    
    
print(meuLen("abracadabra"))
print(len("abracadabra"))