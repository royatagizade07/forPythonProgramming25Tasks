userage=int(input("Enter your age: "))
if userage>0 and userage<=12:
    print("child")
elif userage>13 and userage<=17:
    print("teenager")
elif userage>18 and userage<=64:
    print("adult")
elif userage>65:
    print("senior")
elif userage<0:
    print("Invalid age")