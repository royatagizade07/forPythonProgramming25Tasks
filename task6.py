number1=int(input("Enter first number: "))
number2=int(input("Enter second number: "))
add="+"
sub="-"
mult="*"
div="/"
modulus="%"
exponent="**"
floor="//"
operation=input("Enter operation: ")
if operation==add:
    print(number1+number2)
elif operation==sub:   
    print(number1-number2)
elif operation==mult:
    print(number1*number2)
elif operation==div and number2!=0:
    print(number1/number2)
elif operation==modulus:
    print(number1%number2)
elif operation==exponent:
    print(number1**number2)
elif operation==floor:
    print(number1//number2)
else:
    print("Invalid operation")