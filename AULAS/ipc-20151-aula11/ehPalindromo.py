def ehPalindromo(a):
    if (str(a) == str(a)[::-1]):
        return True
    else:
        return False
    
assert ehPalindromo(1221)
assert not ehPalindromo(1234)


i = 1000

while (i <= 9999):
   # Olhar se i é palindromo
    if (ehPalindromo(i)):
        print(i)
    i += 1