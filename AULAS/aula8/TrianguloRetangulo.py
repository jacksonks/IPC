a = int(input())
b = int(input())
c = int(input())

if ((a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == b**2 + a**2)):
        print(True)
else:
        print(False)