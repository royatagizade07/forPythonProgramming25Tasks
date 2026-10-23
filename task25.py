studentid=input()
workshop_code=input()
age=input()
payment=input()
if len(studentid)!=9 or not(studentid.isascii() and studentid.isdecimal()):
    print("invalid student id")
elif age=="" or not(age.isascii() and age.isdecimal() ):
    print("invalid age")
else:
    if age<16 or age>65:
        print("wrong age range")
    elif workshop_code!="PY" and workshop_code!="WEB" and workshop_code!="CY":
        print("invalid workshop code")
    else:
        match workshop_code:
            case "PY":
                salary=30
                minage=16
            case "WEB":
                salary=40
                minage=16
            case "CY":
                salary=50
                minage=18
        if age<minage:
            print("age need to be atleast minimum")
        elif payment=="" or not(payment.isascii() and payment.isdecimal()):
            print("wrong payment format")
        else:
            payment=int(payment)
            discount=20  if age>=16 and age<=18 else 0
            paymentdiscounted=payment*discount
            finalpayment=payment-paymentdiscounted
            if payment<finalpayment:
                missingamount=finalpayment-payment
                print("not sufficient payment:", missingamount)
            else:
                change=payment-finalpayment
                print("Registration confirmed")
                print("studentid:", studentid)
                print("worksop:", workshop_code)
                print("discount:",discount)
                print("finaltotal:",finalpayment)
                print("change:" ,change)
            
            
        
        