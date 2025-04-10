account={}
def craete():
    ac={}
    PH=int(input(" phone number : "))
    NA=input("name : ")
    AM=int(input("amount : "))
    if PH not in account:
            ac["phone"]=PH
            ac["name"]=NA
            ac["amount"]=AM
            account[PH]=ac
    else:
            print("phone number already exist")
def update():
       ac={}
    
       PH=int(input("enter the number : "))
       if PH in account:
        NA=input("enter your name : ")
        AM=int(input("enter the amount :"))
        ac["name"]=NA
        ac["amount"]=AM
        account[PH]=ac
       else:
            print("not found")
def delete():
     PH=int(input("enter the number : "))
     if PH in account:
          del account[PH]
          print("successfully deleted")
def deposit():
     PH=int(input("enter phone number : "))
     if PH in account:
        DE=int(input("enter the deposit amount"))
        account[PH]["amount"]+=DE
        print(account)
        print("successfully deposited")
        print("new balance",account[PH]["amount"])
def withdraw():
      PH=int(input("enter phone number : "))
      if PH in account:
        WD=int(input("enter the withdrawal amount"))
        if WD<+account[PH]["amount"]:
             account[PH]["amount"]-=WD
             print(account)
             print("transaction successfully compeleted")
             print("balance",account[PH]["amount"])
        else:
             print("insufficient fund","\nre-enter")
    
      else:
           print("accont not found")
           
     

    
        


while True:
    print("1.create ""\n2.update""\n3.delete""\n4.deposit""\n5.withdraw")
    a=input("choose your option : ")
    if a=="1":
        f=craete()
        print(f)
    elif a=="2":
          f=update()
          print(f)
    elif a=="3":
         f=delete()
         print(f)
    elif a=="4":
         f=deposit()
    elif a=="5":
         f=withdraw()
         

