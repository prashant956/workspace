from random import randint
t=["rock","paper","scissors"]
computer=t[randint(0,2)]
player=False
while player==False:
    player=input("rock,paper,scissors:")
    if player==computer:
        print("tie")
    elif player=="rock":
        if computer=="paper":
            print("you lose.!")
        else:
            print("you win.!")
    elif player=="paper":
        if computer=="scissors":
            print("you lose.!")
        else:
            print("you win.!")
    elif player=="scissors":
        if computer=="rock":
            print("you lose.!")
        else:
            print("you win.!")
    else:
        print("that is not a valid player")
    player=False
    computer=t[randint(0,2)]
    
