def ipva(listas):
    dic = {}
    l12=[]
    l34=[]
    l5=[]
    l6=[]
    l7=[]
    l8=[]
    l9=[]
    l0=[]
    for i in range(len(listas)):
        a=listas[i]
        if(a[-1]=='1' or a[-1]=='2'):
            l12.append(a)
            dic[1]=l12
        elif(a[-1]=='3' or a[-1]=='4'):
            l34.append(a)
            dic[2]=l34
        elif(a[-1]=='5'):
            l5.append(a)
            dic[3]=l5
        elif(a[-1]=='6'):
            l6.append(a)
            dic[4]=l6
        elif(a[-1]=='7'):
            l7.append(a)
            dic[5]=l7
        elif(a[-1]=='8'):
            l8.append(a)
            dic[6]=l8
        elif(a[-1]=='9'):
            l9.append(a)
            dic[7]=l9
        elif(a[-1]=='0'):
            l0.append(a)
            dic[8]=l0

    return dic

listas = ['mxv1234','zxc4321','qwe8062','mao5677']

print(ipva(listas))

#assert ipva(['mxv1234','zxc4321','qwe8062','mao5677'])=={'5': ['mao5677'], '2': ['mxv1234'], '1': ['zxc4321', 'qwe8062']}
