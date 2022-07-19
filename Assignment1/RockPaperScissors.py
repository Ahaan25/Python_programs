import random
computerinp=''
userwin=0
computerwin=0
count=0
while count<5:
    userinp = input("Enter your choice: Rock Paper or Scissors! ")
    computerchoice = random.randint(1, 3)
    if computerchoice==1:
            computerinp='Rock'
    elif computerchoice==2:
            computerinp='Paper'
    elif computerchoice==3  :
            computerinp='Scissors'
    print("You chose ", userinp, " and the computer chose ", computerinp)
    if computerinp==userinp:
        print("It is a tie, both players selected ", computerinp)
        count+=1
    elif userinp=='Rock':
        if computerinp=='Scissors':
            print("User wins")
            userwin+=1
            count+=1
        else:
            print("User lost")
            computerwin+=1
            count+=1
    elif userinp=='Scissors':
        if computerinp=='Paper':
            print("User wins")
            userwin+=1
            count+=1
        else:
            print("User lost")
            computerwin+=1
            count+=1
    elif userinp=='Paper':
        if computerinp=='Rock':
            print("User wins")
            userwin+=1
            count+=1
        else:
            print("User lost")
            computerwin+=1
            count+=1
if userwin>computerwin:
    print("Your score is ", userwin, "User wins")
elif userwin<computerwin:
    print("Your score is ", userwin, "User Lost")
elif userwin==computerwin:
    print("Your score is ", userwin, "It is a tie")