entrada=input()

a=""
for i in entrada:
    if (i!=" "):
        a+=i

if(a[0]==a[2] or a[1]==a[3]):
    print("V")
elif(a[2]==a[0] or a[3]==a[1]):
    print("V")
else:
    print("F")

