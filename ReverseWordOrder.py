#This program takes a string from the user and reverses
#the word order of the string

def reverse_string(word):
    word = word.split(" ")
    print(' '.join(word[::-1]))


reverse_string(input("Enter a sentence here: "))
