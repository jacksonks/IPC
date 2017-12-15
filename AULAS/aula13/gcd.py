def gcd(a,b):
    if (b == 0):
        return a
    else:
        return gcd(b,a%b)
    
    
assert gcd(17,12) == 1
assert gcd(9,12) == 3
assert gcd(12,6) == 6