wordlist = input("Please input the word you want breaking down: ")
#inputs the word they want to split up into letters
text = wordlist

word_list = []
#gathers a list variable to give it a value
for i in range(0, len(text)):
    word_list.append(text[i])
    i+=1
#if a word is present it will split it up into seperate letters from a list
count = {}
for wordlist in text:
#once it has been split, it will see if the string is in text
  if wordlist in count:
    count[wordlist] += 1
#if a letter is present then it will add 1 onto the count and print each letter out
  else:
    count[wordlist] = 1
#if the letter is only in it once then it will keep it 1
count = str(count)
#i converted the dict type of the variable 'count' into a string to allow it to be printed with the print
print(str("There are " + (count) + " In this string"))
#i add the count variable into the print statement which is then printed with the letters and their count
