age=input("enter your age")
if age.isdigit():
    age=int(age)
    print("you are" + str(age) +" years old")
else:
    print("invalid input! please enter a number")