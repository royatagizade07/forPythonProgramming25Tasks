userscore=input("Enter your score: ")
numberstring="0123456789"
if userscore in numberstring:
    userscore=int(userscore)
    if userscore>=91:
        if userscore<=100:
            print("Your grade is A")
    elif userscore>=81:
        if userscore<=90:
            print("Your grade is B")
    elif userscore>=71:
        if userscore<=80:
            print("Your grade is C")
    elif userscore>=61:
        if userscore<=70:
            print("Your grade is D")
    elif userscore>=51:
        if userscore<=60:
            print("Your grade is E")
    elif userscore>=0:
        if userscore<=50:
            print("Your grade is F")
    else:
        print("Invalid score")
else:
    print("any other character is not allowed")