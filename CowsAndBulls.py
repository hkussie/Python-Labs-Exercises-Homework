#This program requires that a user enter a four digit number
#The program then evaluates a randomly generated number and looks to see if there
#are any similar digits, in the same place, between the user generated number and the one entered in by the user.
#If there are are any similarities, the program lets the user know.


import random

randNum = str(random.randint(1000,9999))
n = input("Enter a 4 digit number here: ")
str(randNum)
str(n)

def figure_out():
    if (n[0] == randNum[0]):
        print("The first digit is the same.")
    elif(n[1] == randNum[1]):
        print("The second digit is the same.")
    elif(n[2] == randNum[2]):
        print("The third digit is the same.")
    elif(n[3] == randNum[3]):
        print("The fourth digit is the same.")
    elif(n[0],n[1],n[2],n[3] == randNum[0],randNum[1],randNum[2],randNum[3]):
        print("All of the digits are the same, wow.")
    else:
        print("There are no digits in common.")

        
