phonenumber=input()
if phonenumber == "":
    print("empty number")
elif len(phonenumber)!=10:
    print("only 10 digits")
elif not(phonenumber.isascii() and phonenumber.isdecimal()):
    print("only ascii digits")
elif phonenumber[0]!="0":
    print("does not start with 0")
else:
    first3digits=phonenumber[:3]
    match first3digits:
        case "050":
            print("accepted")
        case "051":
            print("accepted")
        case "055":
            print("accepted")
        case "070":
            print("accepted")
        case "077":
            print("accepted")
        case "099":
            print("accepted")
        case _:
            print("not accepted")