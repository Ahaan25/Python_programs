credits=int(input("Enter the number of credits: "))
if credits<=23:
    print("Student is a freshman")
elif 24<=credits<=53:
    print("Student is a sophomore")
elif 54<=credits<=83:
    print("Student is a junior")
elif credits>84:
    print("Student is a senior")
