import random
score = 0
print("Welecome to my fill in Maths quiz!")
#enter topic symbol to define quiz questions
PlayAgain = True
while PlayAgain == True:
    Subject = False
    while Subject == False:
        Topic = input("please enter either +, -, / or * to choose the certain topic:  ")
        if Topic == "+":
            Subject = "Addition"
        elif Topic == "-":
            Subject = "Subtraction"
        elif Topic == "*":
            Subject = "Multiplication"
        elif Topic == "/":
            Subject = "Division"
        else:
            print("Please enter a correct topic")
    Subject == True
    #choose the difficulty
    Quiz_Range = False
    while Quiz_Range == False:
        Difficulty = input("Please enter your difficulty out of easy, medium or hard: ").lower()
        if Difficulty == "easy":
            Quiz_Range = (1 < 10)
        elif Difficulty == "medium":
            Quiz_Range = (1<50)
        elif Difficulty == "hard":
            Quiz_Range = (1<100)
        else:
            print("Please enter a Difficulty")
    Quiz_Range == True
    print("You have choosen "+Subject+" on "+Difficulty+" Difficulty")
    #generating the questions-Addition
    if Difficulty == "easy":
            low = 1
            high = 10
    elif Difficulty == "medium":
        low = 1
        high = 50
    elif Difficulty == "hard":
            low = 1
            high = 100
    if Difficulty == "easy" and Subject == "Addition":
        Sum1 = random.randint(low, high)
        Sum2 = random.randint(low, high)
        Sum3 = (Sum1 + Sum2)
        Sum4 = int(input("What is " + str(Sum1) + " + " + str(Sum2) + ": "))
        if Sum4 == Sum3:
            print("Answer is correct!")
            score = score+1
            print(score)
        else:
            print("Answer is incorrect!")
            print(score)
        PlayAgain = input("Do you want to play again?: ")
        if PlayAgain == "yes":
            PlayAgain = True
        elif PlayAgain == "no":
            PlayAgain = False
        else:
            break

    if Difficulty == "medium" and Subject == "Addition":
        Sum1 = random.randint(low, high)
        Sum2 = random.randint(low, high)
        Sum3 = (Sum1 + Sum2)
        Sum4 = int(input("What is " + str(Sum1) + " + " + str(Sum2) + ": "))
        if Sum4 == Sum3:
            print("Answer is correct!")
            score = score+1
            print(score)
        else:
            print("Answer is incorrect!")
            print(score)
            PlayAgain = input("Do you want to play again?: ")
        if PlayAgain == "yes":
            PlayAgain = True
        elif PlayAgain == "no":
            PlayAgain = False
        else:
            break

    if Difficulty == "hard" and Subject == "Addition":
            Sum1 = random.randint(low, high)
            Sum2 = random.randint(low, high)
            Sum3 = (Sum1 + Sum2)
            Sum4 = int(input("What is " + str(Sum1) + " + " + str(Sum2) + ": "))
            if Sum4 == Sum3:
                print("Answer is correct!")
                score = score+1
                print(score)
            else:
                print("Answer is incorrect!")
                print(score)
            PlayAgain = input("Do you want to play again?: ")
            if PlayAgain == "yes":
                PlayAgain = True
            elif PlayAgain == "no":
                PlayAgain = False
            else:
                break

#SUBTRACTION
    if Difficulty == "easy" and Subject == "Subtraction":
                Sum1 = random.randint(low, high)
                Sum2 = random.randint(low, high)
                Sum3 = (Sum1 - Sum2)
                Sum4 = int(input("What is " + str(Sum1) + " - " + str(Sum2) + ": "))
                if Sum4 == Sum3:
                    print("Answer is correct!")
                    score = score+1
                    print(score)
                else:
                    print("Answer is incorrect!")
                    print(score)
                PlayAgain = input("Do you want to play again?: ")
                if PlayAgain == "yes":
                    PlayAgain = True
                elif PlayAgain == "no":
                    PlayAgain = False
                else:
                    break

    if Difficulty == "medium" and Subject == "Subtraction":
                Sum1 = random.randint(low, hign)
                Sum2 = random.randint(low, high)
                Sum3 = (Sum1 - Sum2)
                Sum4 = int(input("What is " + str(Sum1) + " - " + str(Sum2) + ": "))
                if Sum4 == Sum3:
                    print("Answer is correct!")
                    score = score+1
                    print(score)
                else:
                    print("Answer is incorrect!")
                    print(score)
                PlayAgain = input("Do you want to play again?: ")
                if PlayAgain == "yes":
                    PlayAgain = True
                elif PlayAgain == "no":
                    PlayAgain = False
                else:
                    break
    if Difficulty == "hard" and Subject == "Subtraction":
            Sum1 = random.randint(low, high)
            Sum2 = random.randint(low, high)
            Sum3 = (Sum1 - Sum2)
            Sum4 = int(input("What is " + str(Sum1) + " - " + str(Sum2) + ": "))
            if Sum4 == Sum3:
                print("Answer is correct!")
                score = score+1
                print(score)
            else:
                print("Answer is incorrect!")
                print(score)
            PlayAgain = input("Do you want to play again?: ")
            if PlayAgain == "yes":
                PlayAgain = True
            elif PlayAgain == "no":
                PlayAgain = False
            else:
                break
#Multiplication
    if Difficulty == "easy" and Subject == "Multiplication":
            Sum1 = random.randint(low, high)
            Sum2 = random.randint(low, high)
            Sum3 = (Sum1 * Sum2)
            Sum4 = int(input("What is " + str(Sum1) + " X " + str(Sum2) + ": "))
            if Sum4 == Sum3:
                print("Answer is correct!")
                score = score+1
                print(score)
            else:
                print("Answer is incorrect!")
                print(score)
            PlayAgain = input("Do you want to play again?: ")
            if PlayAgain == "yes":
                PlayAgain = True
            elif PlayAgain == "no":
                PlayAgain = False
            else:
                break
    if Difficulty == "medium" and Subject == "Multiplication":
                Sum1 = random.randint(low, high)
                Sum2 = random.randint(low, high)
                Sum3 = (Sum1 * Sum2)
                Sum4 = int(input("What is " + str(Sum1) + " X " + str(Sum2) + ": "))
                if Sum4 == Sum3:
                    print("Answer is correct!")
                    score = score+1
                    print(score)
                else:
                    print("Answer is incorrect!")
                    print(score)
                    PlayAgain = input("Do you want to play again?: ")
                if PlayAgain == "yes":
                    PlayAgain = True
                elif PlayAgain == "no":
                    PlayAgain = False
                else:
                    break
    if Difficulty == "hard" and Subject == "Multiplication":
                Sum1 = random.randint(low, high)
                Sum2 = random.randint(low, high)
                Sum3 = (Sum1 * Sum2)
                Sum4 = int(input("What is " + str(Sum1) + " X " + str(Sum2) + ": "))
                if Sum4 == Sum3:
                    print("Answer is correct!")
                    score = score+1
                    print(score)
                else:
                    print("Answer is incorrect!")
                    print(score)
                PlayAgain = input("Do you want to play again?: ")
                if PlayAgain == "yes":
                    PlayAgain = True
                elif PlayAgain == "no":
                    PlayAgain = False
                else:
                    break 
#Division
    if Difficulty == "medium" and Subject == "Multiplication":
                Sum1 = random.randint(low, high)
                Sum2 = random.randint(low, high)
                Sum3 = (Sum1 * Sum2)
                Sum4 = int(input("What is " + str(Sum1) + " X " + str(Sum2) + ": "))
                if Sum4 == Sum3:
                    print("Answer is correct!")
                    score = score+1
                    print(score)
                else:
                    print("Answer is incorrect!")
                    print(score)
                PlayAgain = input("Do you want to play again?: ")
                if PlayAgain == "yes":
                    PlayAgain = True
                elif PlayAgain == "no":
                    PlayAgain = False
                else:
                    break
    if Difficulty == "easy" and Subject == "Division":
                Sum1 = random.randint(low, high)
                Sum2 = random.randint(low, high)
                Sum3 = (Sum1 / Sum2)
                Sum4 = int(input("What is " + str(Sum1) + " Divided by " + str(Sum2) + ": "))
                if Sum4 == Sum3:
                    print("Answer is correct!")
                    score = score+1
                    print(score)
                else:
                    print("Answer is incorrect!")
                    print(score)
                    PlayAgain = input("Do you want to play again?: ")
                if PlayAgain == "yes":
                    PlayAgain = True
                elif PlayAgain == "no":
                    PlayAgain = False
                else:
                    break 
    if Difficulty == "medium" and Subject == "Division":
                Sum1 = random.randint(low, high)
                Sum2 = random.randint(low, high)
                Sum3 = (Sum1 / Sum2)
                Sum4 = int(input("What is " + str(Sum1) + " Divided by " + str(Sum2) + ": "))
                if Sum4 == Sum3:
                    print("Answer is correct!")
                    score = score+1
                    print(score)
                else:
                    print("Answer is incorrect!")
                    print(score)
                PlayAgain = input("Do you want to play again?: ")
                if PlayAgain == "yes":
                    PlayAgain = True
                elif PlayAgain == "no":
                    PlayAgain = False
                else:
                    break
    if Difficulty == "hard" and Subject == "Division":
                Sum1 = random.randint(low, high)
                Sum2 = random.randint(low, high)
                Sum3 = (Sum1 / Sum2)
                Sum4 = int(input("What is " + str(Sum1) + " Divided by " + str(Sum2) + ": "))
                if Sum4 == Sum3:
                    print("Answer is correct!")
                    score = score+1
                    print(score)
                else:
                    print("Answer is incorrect!")
                    print(score)
                PlayAgain = input("Do you want to play again?: ")
                if PlayAgain == "yes":
                    PlayAgain = True
                elif PlayAgain == "no":
                    PlayAgain = False
                else:
                    break

