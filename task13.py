age = int(input("Enter your age: "))
monthlysalary = int(input("Enter your monthly salary: "))
requstedloanamount = int(input("Enter the requested loan amount: "))
if age < 0:
    print("Invalid age")
else:
    if monthlysalary < 0:
        print("Invalid salary")
    else:
        if requstedloanamount <= 0:
            print("Invalid loan amount")
        else:
            if age < 18:
                print("age is below 18, you cannot take a loan")
            else:
                if monthlysalary <500:
                    print("salary is below 500, you cannot take a loan")
                else:
                    if requstedloanamount > 10 * monthlysalary:
                        print("loan amount is higher than 10 times your salary, you cannot take a loan")
                    else:
                        print("You can take a loan")