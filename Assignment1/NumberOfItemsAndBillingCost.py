items=int(input("The number of items bought: "))
if items<10:
    print("The total cost is: $", items*12)
elif 10<=items<=99:
    print("The total cost is: $", items*10)
elif items>100:
    print("The total cost is: $", items*7)
