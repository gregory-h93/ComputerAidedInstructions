import random

def toFixed(value, digits):
    return "%.*f" % (digits, value)

def addition(num1, num2):
    sum = num1 + num2
    print("What is the sum of " + str(num1) + " + " + str(num2) + "?")
    ans = int(input())
    if ans == sum:
        res = int(random.random() * 3)
        if res == 1:
            print("Very Good!")
        else:
            if res == 2:
                print("Nice Work!")
            else:
                print("Keep up the good work!")
    else:
        res = int(random.random() * 3)
        if res == 1:
            print("No. Please try again!")
        else:
            if res == 2:
                print("Wrong. Try once more.")
            else:
                print("No. Keep trying!")

def division(num1, num2):
    quo = float(num1) / num2
    fQuo = toFixed(quo,2)
    print("What is the quotient of " + str(num1) + " / " + str(num2) + "? (answer formatted to 2 decimal places)")
    ans = float(input())
    fAns = toFixed(ans,2)
    if fAns == fQuo:
        res = int(random.random() * 3)
        if res == 1:
            print("Very Good!")
        else:
            if res == 2:
                print("Nice Work!")
            else:
                print("Keep up the good work!")
    else:
        res = int(random.random() * 3)
        if res == 1:
            print("No. Please try again!")
        else:
            if res == 2:
                print("Wrong. Try once more.")
            else:
                print("No. Keep trying!")

def easy():
    print("You have selected easy arithmetic.")
    while True:    #This simulates a Do Loop
        choice = ""
        print("Please select the type of easy arithmetic: ")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Main menu")
        choice = input()
        iChoice = ord(choice)
        while iChoice <= 48 or iChoice > 53:
            print("Invalid input! Please select the type of easy arithmetic (1 for addition | 2 for subtraction | 3 for multiplication | 4 for division | 5 for the Main menu): ")
            choice = input()
            iChoice = ord(choice)
        cChoice = chr(iChoice)
        intChoice = int(cChoice)
        if intChoice == 1:
            num1 = int(random.random() * 10)
            num2 = int(random.random() * 10)
            addition(num1, num2)
        else:
            if intChoice == 2:
                num1 = int(random.random() * 10)
                num2 = int(random.random() * 10)
                subtraction(num1, num2)
            else:
                if intChoice == 3:
                    num1 = int(random.random() * 10)
                    num2 = int(random.random() * 10)
                    multiplication(num1, num2)
                else:
                    if intChoice == 4:
                        num1 = int(random.random() * 10)
                        if num1 == 0:
                            num1 = num1 + 1
                        num2 = int(random.random() * 10)
                        if num2 == 0:
                            num2 = num2 + 1
                        while num1 % num2 != 0:
                            num1 = int(random.random() * 10)
                            num2 = int(random.random() * 10)
                        division(num1, num2)
        if not(intChoice != 5): break   #Exit loop
    
    return intChoice

def hard():
    print("You have selected hard arithmetic.")
    while True:    #This simulates a Do Loop
        choice = ""
        print("Please select the type of arithmetic: ")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Main menu")
        choice = input()
        iChoice = ord(choice)
        while iChoice <= 48 or iChoice > 53:
            print("Invalid input! Please select the type of easy arithmetic (1 for addition | 2 for subtraction | 3 for multiplication | 4 for division | 5 for the Main menu): ")
            choice = input()
            iChoice = ord(choice)
        cChoice = chr(iChoice)
        intChoice = int(cChoice)
        if intChoice == 1:
            num1 = int(random.random() * 100)
            num2 = int(random.random() * 100)
            addition(num1, num2)
        else:
            if intChoice == 2:
                num1 = int(random.random() * 100)
                num2 = int(random.random() * 100)
                subtraction(num1, num2)
            else:
                if intChoice == 3:
                    num1 = int(random.random() * 100)
                    num2 = int(random.random() * 100)
                    multiplication(num1, num2)
                else:
                    if intChoice == 4:
                        num1 = int(random.random() * 100)
                        if num1 == 0:
                            num1 = num1 + 1
                        num2 = int(random.random() * 100)
                        if num2 == 0:
                            num2 = num2 + 1
                        while num1 % num2 != 0:
                            num1 = int(random.random() * 100)
                            if num1 == 0:
                                num1 = num1 + 1
                            num2 = int(random.random() * 100)
                            if num2 == 0:
                                num2 = num2 + 1
                        division(num1, num2)
        if not(intChoice != 5): break   #Exit loop
    
    return intChoice

def multiplication(num1, num2):
    pro = num1 * num2
    print("What is the product of " + str(num1) + " x " + str(num2) + "?")
    ans = int(input())
    if ans == pro:
        res = int(random.random() * 3)
        if res == 1:
            print("Very Good!")
        else:
            if res == 2:
                print("Nice Work!")
            else:
                print("Keep up the good work!")
    else:
        res = int(random.random() * 3)
        if res == 1:
            print("No. Please try again!")
        else:
            if res == 2:
                print("Wrong. Try once more.")
            else:
                print("No. Keep trying!")

def subtraction(num1, num2):
    diff = num1 - num2
    print("What is the difference of " + str(num1) + " - " + str(num2) + "?")
    ans = int(input())
    if ans == diff:
        res = int(random.random() * 3)
        if res == 1:
            print("Very Good!")
        else:
            if res == 2:
                print("Nice Work!")
            else:
                print("Keep up the good work!")
    else:
        res = int(random.random() * 3)
        if res == 1:
            print("No. Please try again!")
        else:
            if res == 2:
                print("Wrong. Try once more.")
            else:
                print("No. Keep trying!")

# Main
while True:    #This simulates a Do Loop
    choice = 0
    print("This is a study program to help you learn addition, subtraction, multiplication, or division")
    print("Please select your difficulty level: ")
    print("1. Easy (single-digit numbers)")
    print("2. Hard (double-digit numbers)")
    print("3. Exit the program")
    diff = input()
    iDiff = ord(diff)
    while iDiff <= 48 or iDiff > 51:
        print("Invalid input! Please select your difficulty level (1 for easy | 2 for hard | 3 to exit): ")
        print("1. Easy (single-digit numbers)")
        print("2. Hard (double-digit numbers)")
        print("3. Exit the program")
        diff = input()
        iDiff = ord(diff)
    cDiff = chr(iDiff)
    intDiff = int(cDiff)
    if intDiff == 1:
        easy()
        if choice == 5:
            choice = 3
        else:
            choice = 2
    else:
        if intDiff == 2:
            hard()
            if choice == 5:
                choice = 3
            else:
                choice = 2
        else:
            intDiff = 3
            choice = intDiff
    if not(choice != 3): break   #Exit loop
print("You have chosen to end the program! Goodbye!")
