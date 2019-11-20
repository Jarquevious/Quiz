# The Simpson's Quiz
score = 0
correct_answers = []
incorrect_answers = []

# True or False Questions 1-2
def question_1():
    print("Pick 0 for False or 1 for True")
    response = input("1. Homer has 4 Kids: ")
    correct_answer = ("0")
    if response == correct_answer:
        print("Superb")
        return 1    
    elif response != correct_answer:
        print("That's incorrect. The correct answer is 0")
        return 0
    
       
def question_2():
    print("\nPick 0 for False or 1 for True")
    response = input("2. Marge is Homer's wife: ")
    correct_answer = ("1")
    if response == correct_answer:
        print("Correct")
        return 1    
    elif response != correct_answer:
        print("That's incorrect. The correct answer is 1")
        return 0
      
# Multiple Choice Questions 3-4
def question_3():
    print("\nChoose a letter a-e")
    response = input("3. How does Homer discipline Bart?: \n a. Extra Chores \n b. Whooping \n c. Choke \n d. No TV \n e. None of the Above")
    correct_answer = ("c")
    if response == correct_answer:
        print("Great Job!")
        return 1
    elif response != correct_answer:
        print("That's incorrect. The correct answer is c")
        return 0

def question_4():
    print("\nChoose a letter a-e")
    response = input("4. What is Bart's sister name?: \n a. Rachel \n b. Lisa \n c. Elyse \n d. Ashley \n e. None of the Above")
    correct_answer = ("b")
    if response == correct_answer:
        print("Awesome!")
        return 1
    elif response != correct_answer:
        print("The answer is b!")
        return 0

#Numeric Response Questions 5-6
def question_5():
    print("\nEnter a number")
    response = input("5. Marge has how many sisters?  ")
    correct_answer = ("2")
    if response == correct_answer:
        print("Correct")
        return 1
    elif response != correct_answer:
        print("Marge has 2 sisters")
        return 0

def question_6():
    print("\nEnter a number")
    response = input("6. How many pets do the Simpson's have?")
    correct_answer = ("2")
    if response == correct_answer:
        print("You did it!")
        return 1
    elif response != correct_answer:
        print("They have a cat and a dog")
        return 0
        print("\n")


total_score = 0
result = question_1() + question_2() + question_3() + question_4() + question_5() + question_6()
total_score += result

if total_score <= 1:
    print(f"You scored {total_score} out of 6. The Simpsons come on every night, watch it for a year then retake the quiz!")

elif total_score == 3 or 4:
    print(f"You scored {total_score} out of 6. This test is for real simpsons fans!")

elif total_score == 5:
    print(f"You scored {total_score} out of 6. Try again after two weeks.")

else:
    print("You are the biggest simpson fan on EARTH!!!")

