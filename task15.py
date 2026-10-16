schoolscore=int(input("Enter your score: "))
age=int(input("Enter your age: "))
examscore=int(input("Enter your exam score: "))
if age<0:
    print("Invalid age")
elif schoolscore<0:
    print("Invalid school score")
elif schoolscore>100:
    print("Invalid school score")
elif examscore<0:
    print("Invalid exam score")
elif examscore>700:
    print("Invalid exam score")
else:
    if age <16:
        print("age is below 16, rejected")
    elif examscore>=600:
        print("scholarship granted")
    elif examscore>=450:
        if examscore<=599:
            print("accepted")
    elif examscore>=300:
        if examscore<=449:
            if schoolscore>=80:
                print("accepted")
            else:
                print("rejected school score is below 80")
    else:
        print("rejected exam score is below 300")