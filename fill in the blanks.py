score = 0
words = [('<Scared>', '________'), ('<Words>', '_______'), ('<False>', '_______'), ('<Whole>', '_______')]
print("Welcome To my fill in the blanks game!")
print("Enter the missing word for a point!")

Missing_words = open("Blank_words.txt","r")

while True:
    for k, v in words:
        Question = Missing_words.readline()
        Question = Question.replace(k, v)
        Answer = input(Question)
        if Answer in k:
            print("You are Correct!")
            score = score+1
            print(score)
        else:
            print("Im afraid you are incorrect")
            print("The correct answer is"+k)
