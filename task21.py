pincode="0427"
pin= input()
if pin == "":
    print("pin is required")
elif len(pin) != 4:
    print("pin must have 4 digits")
elif not(pin.isascii() and pin.isdecimal()):
    print("digits only")
else:
    if pincode == pin:
        print("access granted")
    else:
        print("incorrect pin")

