km = int(input("Enter distance in kilometers: "))
startingfee = 2.00
if km < 0:
    print("Invalid distance")
else:
    if km >=0 and km <= 5:
        fee = 0.70
    elif km>5 and km <= 15:
        fee = 0.60
    elif km>15 :
        fee = 0.50
    distancefee = startingfee + (km * fee)
    totalfee = startingfee + distancefee
    print(startingfee, distancefee, totalfee)