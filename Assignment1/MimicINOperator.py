def checkStr():
    userStr=str(input("Enter a string: "))
    lttr=str(input("Enter letter: "))
    for i in userStr:
        if i==lttr:
            print("Letter appears")
            return
    print("Letter does not appear")
checkStr()