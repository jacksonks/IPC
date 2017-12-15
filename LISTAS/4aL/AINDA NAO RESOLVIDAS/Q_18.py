def vogal(char):
    
    if(char== "a") or (char== "A"):
        return True
    elif(char== "e") or (char=="E"):
        return True
    elif(char== "i") or (char =="I"):
        return True
    elif(char== "o") or (char== "O"):
        return True
    elif(char== "u") and (char== "U"):
        return True
    else:
        return False

x=input()
print(vogal("a"))
print(vogal("A"))
print(vogal("j"))
print(vogal(x))