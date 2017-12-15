def media(x1,x2):
    '''
    Calcula a media de dois numeros fornecidos como entrada
    x1 : int or float
    x2 :  int or float
    media: float
    '''
    return (x1 + x2)/2

assert media(6.0,8.0) == 7.0 
assert media(3.5,5.5) == 4.5
assert media(7,6) == 6.5

x = float(input())
y = float(input())
assert media(x,y) == (x+y)/2.0
