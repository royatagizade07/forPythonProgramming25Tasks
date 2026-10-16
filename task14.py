side1=int(input("Enter the first side of the triangle: "))
side2=int(input("Enter the second side of the triangle: "))
side3=int(input("Enter the third side of the triangle: "))
if side1<=0 or side2<=0 or side3<=0:
    print("Invalid side lengths. All sides must be positive.")
else:
    if side1+side2>side3:
        if side1+side3>side2:
            if side2+side3>side1:
                 if side1==side2:
                    if side2==side3:
                        print("The triangle is equilateral.")
                    else:
                        if side1==side2 or side1==side3 or side2==side3:
                            print("The triangle is isosceles.")
                        else:
                            print("The triangle is scalene.")
            else:
                print("The triangle cannot be created.")
        else:
            print("The triangle cannot be created.")
    else:
        print("The triangle cannot be created.")