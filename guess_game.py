while True:
    from random import randint
    comguess=randint(1,50)
    while True:
        userguess=int(input("your guess (1-50):"))
        if userguess>=1 and userguess<=50:
            if userguess>comguess:
                print("think lower print in limit:")
            elif userguess<comguess:
                print("think big be big")
            else:
                    print("yaa..! your guess is correct")
                    break
        else:
             print("Donot over smart")
             print("Do say i only 1-50")
        ch=input("Do you play again?y/n:").strip()
        ch.lower()
    if ch=='y' or ch=='yes':
        continue
    else:
      break
                        

    
