#This is a simple program that asks the user to enter their name, and the program
#then creates a file and saves the content to the file. 

text = input("Enter a name here: ")

saveFile = open('exampleFile.txt', 'w')
saveFile.write(text)
saveFile.close()

#this portion appends to the file exampleFile.txt
#appendMe is added to previous content 

appendMe = 'Appending content to the file'

appendFile = open('exampleFile.txt', 'a')
appendFile.write(appendMe)
appendFile.close()
