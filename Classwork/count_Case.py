a=input("Please enter the string: ")
countU=0
countL=0
for i in a:
    if (i.isupper()):
        countU=countU+1
    elif (i.islower()):
        countL=countL+1
print("The total number of uppercase letters are: ", countU)
print("The total number of lowercase letters are:", countL)