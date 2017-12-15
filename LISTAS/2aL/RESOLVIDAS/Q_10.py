#Indique a saída dos seguintes programas em Python#
(a)
num = 0
while (num <= 5):
    print (num)
    num += 1
print (" Outside of loop ")
print (num)

(b)
numberOfLoops = 0
numberOfApples = 2
while ( numberOfLoops < 10):
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print (" Number of apples : " + str( numberOfApples ))

(c)
num = 10
while (num > 3):
    num -= 1
print (num )

(d)
num = 10
while ( True ):
    if (num < 7):
        print ('Breaking out of loop ')
        break
    print (num)
    num -= 1
print ('Outside of loop ')

(e)
num = 100
while (not False ):
    if (num < 0):
        break
print ('num is: ' + str( num))

(f)
myStr = 'Esta eh uma string !'
for char in myStr :
    print ( char )
print ('done ')

(g)
greeting = 'Hello !'
count = 0
for letter in greeting :
    count += 1
    if ( count \% 2 == 0):
        print letter
    print letter
print ('done ')

(h)
school = 'Escola Superior de Tecnologia'
numVowels = 0
numCons = 0
for char in school :
   if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
      numVowels += 1
   elif char == 'i' or char == 'T':
      print (char)
   else :
      numCons -= 1
print ('numVowels is: ' + str(numVowels))
print ('numCons is: ' + str(numCons))

(i)
num = 10
for num in range (5):
    print (num)
print (num)

(j)
divisor = 2
for num in range (0, 10, 2):
    print (num/ divisor)

(k)
for variable in range (20):
    if ( variable \% 4 == 0):
        print ( variable )
    if ( variable \% 16 == 0):
        print ('Foo!')

(l)
for letter in 'Alô Mundo ':
    print ( letter )