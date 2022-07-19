def checkStr():
    userStr=str(input("Enter a string: "))
    lttr=str(input("Enter letter: "))
    count=0
    for i in userStr:
        if i==lttr:
            print("The index of the letter is ", count)
            break
        count+=1
checkStr()