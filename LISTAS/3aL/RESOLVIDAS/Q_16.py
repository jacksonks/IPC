def a(x,y,z):
    if(x):
        return y
    else:
        return z

def b (q,r):
    return (a(q>r,q,r))

print(a(False,2,3))
print(b(2,3))
#3
#3