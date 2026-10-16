id = input()
if len(id)==0:
    print("id is empty")
elif len(id) == 8:
    if id.isascii():
        if id.isdecimal(): 
            print("student id is accepted")
        else:
            print("id's ekements are not only numbers ")
    else:
        print("id's elements are not in ascii")
else:
    print("id is not accepted")