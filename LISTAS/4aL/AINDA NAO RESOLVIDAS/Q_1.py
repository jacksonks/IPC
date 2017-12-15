def div(x,y):
    if(x==y):
        return 0
    elif(x<y):
        return x
    else:
        return div((x-y),y)

print(div(3,3))
