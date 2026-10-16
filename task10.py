drawingamount = int(input("Enter the amount to withdraw: "))
balance = 1000
if drawingamount <= 0:
    print("Invalid amount")
elif drawingamount > balance:
    print("Insufficient balance")
else:  
    balance = balance - drawingamount
    print("Withdrawal successful. Remaining balance:", balance)