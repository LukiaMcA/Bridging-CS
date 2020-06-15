import random
score = 0
print("Welcome To my fill in the blanks game!")
print("Enter the missing word for a point!")
file = open("Blank_words.txt", "r")
#Opens the file for the text data
for line in file:
    line = line.strip()
    pos1 = line.find("<")
    pos2 = line.find(">")
    word = line[pos1+1:pos2]
#If there is an < and > it will get both the letters and the word inside it and combine it into one
    sentence = line[0:pos1] + ("-" * len(word)) + line[pos2+1:]
#This will make the text replace the word with ----
    print(sentence)
#Displays the sentences with the ----
    guess = input("Enter Guess: ")
#Inputs a guess
    if guess.lower() == word.lower():
#if their guess is equal to the value before the ---- it will pass as correct
        print("Correct")
        score += 1
#Adds a point onto their score and prints it out
        print(score)
    else:
        print("incorrect The answer was "+word)
#this will tell them they got it wrong and shows the answer
