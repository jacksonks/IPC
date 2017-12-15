'''
Programa que ilustra fatiamento de strings em Python

elloa - elloa.uea@gmail.com

'''

casa = "casa"
print(casa[1:3])
print(casa[0:4])
assert(casa[2:4] == 'sa')
print(casa[:3])
print(casa[:-1])
print(casa[:])
print(casa[-1:])
print(casa[0:-1])

s = "Hello world!"
print(s[3:9:2])
print(s[3:9:])

# inversão da string
print(s[::-1])

print(s[::-2])