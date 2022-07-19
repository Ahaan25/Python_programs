def checkStr():
    userStr=str(input("Enter a string: "))
    lttr=str(input("Enter letter: "))
    count=0
    for i in userStr:
        if i==lttr:
            count+=1
    print("Letter appears ",count," times")
checkStr()