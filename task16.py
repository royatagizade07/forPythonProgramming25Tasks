score = int(input("Enter your score: "))
if score < 0:
    print("Invalid score")
if score > 100:
    print("Invalid score")
scoreresult = "passed" if score >= 51 else "failed"