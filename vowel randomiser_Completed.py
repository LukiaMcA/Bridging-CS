import random
print("Welcome to my vowel randomiser!")
file = open("RandomVowels.txt","r")
#reads the text file
for line in file:
    line = line.strip()
    pos1 = line.find("[")
    pos2 = line.find("]")
    word = line[pos1+1:pos2]
#seperates the text file into a variable
vowels_lst = ['a', 'e', 'i', 'o', 'u']
#states the vowels that change
for i in range(len(word)):
    if word[i] in vowels_lst:
#if any of the vowels stated are in the variable, it will randomly selecte one and replace it
        rand_let = random.choice(vowels_lst)
        new_word = word.replace(word[i], rand_let)
#creates the new word variable by replacing word with the random vowels
print(new_word)
#shows the string to the user
file =  open("RandomVowels_New.txt","r")
#reads the file
file = open("RandomVowels_New.txt","w")
#writes to the file
file = file.write(new_word)
#finishes the file and closes


