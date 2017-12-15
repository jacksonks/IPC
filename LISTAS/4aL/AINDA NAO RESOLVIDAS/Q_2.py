def div(x,y):
    if(x==y):
        return 0
    elif(x<y):
        return x
    else:
        return 1+div((x-y),y)

print(div(5,3))