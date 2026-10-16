T=2
C=4
J=3
drinkchoice=input()
quantity=int(input("Enter the quantity : ")) 
if quantity>=1 and quantity<=10:
    match drinkchoice:
        case "T":
            price= quantity*T
        case "C":
            price= quantity*C
        case "J":
            price= quantity*J
        case _:
            price = -1
            print("Invalid drink selection")
    if price != -1:
        order="Large order" if price >= 20 else "Regular order"
        print(drinkchoice, quantity, price, order)
else:
    print("Invalid quantity")
