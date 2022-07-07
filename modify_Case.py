def modify_Case(word):
    ans=""
    word=input("Enter a word: ")
    for i in range(len(word)):
        if word[i].isupper():
            ans+=word[i].lower()
        elif word[i].islower():
            ans+=word[i].upper()
        else:
            ans+=word[i]
    print(ans)
modify_Case('')