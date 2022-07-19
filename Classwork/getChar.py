def getChar(word, pos):
    word=input("Enter a word: ")
    pos=input("Enter a position(from 0): ")
    pos=int(pos)
    print("Character at given index is: ", word[pos])
getChar('Abc', 1)