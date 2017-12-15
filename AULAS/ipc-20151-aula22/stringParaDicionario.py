def stringParaDicionario(palavra):
    d = {}
    for c in palavra:
        if c in d.keys():
            d[c] = d[c] + 1
        else:
            d[c] = 1
    
    return d

print(stringParaDicionario("asdfg"))
print(stringParaDicionario("the quick brown fox jumps over the lazy dog"))
    