wordlist = input("Please input the word you want breaking down: ")
text = wordlist

word_list = []

for i in range(0, len(text)):
    word_list.append(text[i])
    i+=1

count = {}
for wordlist in text:
  if wordlist in count:
    count[wordlist] += 1
  else:
    count[wordlist] = 1
print("There are : ")
print (count)
print("In this string")