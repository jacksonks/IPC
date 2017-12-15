datainicial=input()
dia=int(datainicial[:2])
mes=int(datainicial[3:5])
ano=int(datainicial[6:])
if ano>0 and ano<9999:
  if ((ano%100==0) and (ano%400==0)) or ((ano%4)==0):
         if mes>12 or mes<0:
            print ("False")
         else:
             if mes==2:
                if dia>29 or dia<0:
                    print ("False")
                else:
                    print ("True")
             if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
                 if dia<0 or dia>31:
                     print ("False")
                 else:
                     print ("True")
             if mes==4 or mes==6 or mes==9 or mes==11:
                 if dia<0 or dia>30:
                     print ("False")
                 else:
                   print ("True")
  else:
      if mes>12 or mes<0:
            print ("False")
      else:
           if mes==2:
             if dia>28 or dia<0:
                    print ("False")
             else:
                    print ("True")
           if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
                 if dia<0 or dia>31:
                     print ("False")
                 else:
                     print ("True")
           if mes==4 or mes==6 or mes==9 or mes==11:
                 if dia<0 or dia>30:
                     print ("False")
                 else:
                   print("True")
else:
    print ("False")
