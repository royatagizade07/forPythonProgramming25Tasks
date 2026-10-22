productcode=input()
quantity_str=input()
cuponcode=input()
deliverycode=input()
products=input()
if products != "K" and products !="M" and products !="H":
    print("invalid product code")
elif quantity_str=="" or not (quantity_str.isascii() and quantity_str.isdecimal()):
    print("invalid quantity format")
else:
    quantity=int(quantity_str)
    if quantity <1 or quantity>5:
        print("must be between 1 and 5")
    elif cuponcode!="NONE" and cuponcode!="SAVE10":
        print("invalid cupon code")
    else:
        match productcode:
            case "K":
                price=40
            case "M":
                price=20
            case "H":
                price=60
            case _:
                print("invalid product is included")
        subtotal=price*quantity
        if subtotal<100 and cuponcode=="SAVE10":
            print("ineligible discount")
        elif deliverycode!="P" and deliverycode!="S":
            print("invalid deliverycode")
        else:
            discount=(subtotal*0.1) if cuponcode=="S" and subtotal>=100 else 0
            discountedsubtotal=subtotal-discount
            match deliverycode:
                case "P":
                    delivery=0
                case"S":
                    delivery = 0 if discountedsubtotal>=80 else 5
            final=discountedsubtotal+delivery
            print(productcode)
            print(quantity)
            print(subtotal)
            print(discount)
            print(delivery)
            print(final)