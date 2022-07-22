def alternatecase(inp):
    inp = input("Enter string to convert to AlTeRnAtE cAsE: ")
    i=j=0
    temp=""
    result=""
    for i in range(len(inp)):
        if inp[i].isupper():
            temp+=inp[i].lower()
        elif inp[i].islower():
            temp+=inp[i].lower()
        else:
            temp+=inp[i]
    for j in range(len(temp)):
        if not j%2:
            result+=temp[j].upper()
        else:
            result+=temp[j].lower()
    print(result)
alternatecase('')