import random
a = random.randint(1,9)

def guessing_game():
    n = input("Enter a number here: ")
    if(n > a):
        print("You need to guess lower")
    elif(n < a):
        print("You need to guess HIGHER")
    elif(n == a):
        print("HOLY SHIT")
    else:
        return 0 
