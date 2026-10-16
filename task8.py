useramount = float(input("Enter your amount: "))
if useramount<=100:
    discount=0
elif useramount>100 and useramount<=299.99:
    discount=10
elif useramount>300 and useramount<=499.99:
    discount=15
elif useramount>=500:
    discount=20
discountamount=useramount*discount/100
finalprice =useramount-discountamount
print(discount, discountamount, finalprice)