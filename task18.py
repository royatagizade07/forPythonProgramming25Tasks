daynumber = int(input("Enter a number (1-7) representing the day of the week: "))
weekday = "studyday"
weekend = "weekend"
match daynumber:
    case 1:
        print("Monday and ", weekday)
    case 2:
        print("Tuesday and ", weekday)
    case 3:
        print("Wednesday and ", weekday)
    case 4:
        print("Thursday and ", weekday)
    case 5:
        print("Friday and ", weekday)
    case 6:
        print("Saturday and ", weekend)
    case 7:
        print("Sunday and ", weekend)
    case _:
        print("Invalid day number.")