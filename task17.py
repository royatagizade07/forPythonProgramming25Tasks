order = int(input("Enter the order amount: "))
if order < 0:
    print("Invalid order amount")
membership = input("Are you a member? (yes/no): ")
if membership == "yes" or membership == "no":
    fee = 0 if membership == "yes" or order >= 50 else 5
    delivery_fee = order + fee
    print("Total delivery cost: ", delivery_fee)
    print("Fee: ", fee)
else:
    print("Invalid membership status")