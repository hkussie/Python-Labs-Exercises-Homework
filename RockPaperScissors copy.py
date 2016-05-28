import random
 
paper = random.randrange(0,3, 1)
scissors = random.randrange(3, 6, 1)
rock = random.randrange(6, 9, 1)

option1 = input("Enter either rock, paper, or scissors here: ")
option2 = random.randrange(0,10,1)

def lets_play():
    if (option1 > option2):
        print("YOU WIN")
    elif(option1 < option2):
        print("YOU LOOSE")
    elif(option1 == option2):
        print("You tied, you fuck")
    else:
        print("You done fucked up")
    
