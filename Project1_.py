name=input("enter the name:> ")
number=int(input("enter the no: "))
if(number==1):
    print(name.upper())
elif(number==2):
    print(name.lower())
elif(number==3):
    print(name.strip())
elif(number==4):
    print(name.rstrip())
elif(number==5):
    if(name=="madhav"):
        print(name.replace("madhav","sharma"))
    else:
        print("Kindly check your code once :")
elif(number==6):
    print(name.capitalize())
elif(number==7):
    print(name.center())
elif(number==8):  
    print(name.count("s"))
elif(number==9):
    print(name.endswith("a"))
elif(number==10):
    print(name.isalnum())
elif(number==11):
    print(name.isalpha())
elif(number==12):
    print(name.islower())
elif(number==13):
    print(name.issapace())
elif(number==14):
    print(name.title())
    
