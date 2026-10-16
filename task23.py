assumebalance=1000
storedpin="0427"
pin=input()
balance=input()
if pin=="":
    print("empty pin")
elif len(pin)!=4:
    print("only 4 digits")
elif not(pin.isascii() and pin.isdecimal()):
    print("only ascii digits")
elif pin!=storedpin:
    print("does not match")
elif balance=="" or not (balance.isascii() and balance.isdecimal()):
    print("is empty and only ascii digits")
else:
    balance=int(balance)
    if balance<10 or balance>500:
        print ("balance range error")
    elif balance%10!=0:
        print("need to be divisible by 10")
    else:
        fee = 0 if balance<=200 else 2
        if balance+fee>assumebalance:
            print("exceed the asssumebalance")
        else:
            newbalance=assumebalance-(balance +fee)
            print(balance,fee,newbalance)