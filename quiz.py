# The Simpson's Quiz

correct_answers_list = []
incorrect_answers_list = []

# True or False Questions 1-2
def question_1():
    print("Pick 0 for False or 1 for True")
    response = input("1. Homer has 4 Kids: ")
    correct_answer = ("0")
    if response == correct_answer:
        print("Superb")
        correct_answers_list.append('Question 1 is Correct')
        return 1    
    elif response != correct_answer:
        print("That's incorrect. The correct answer is 0")
        incorrect_answers_list.append('Question 1 is Incorrect')
        return 0
       
def question_2():
    print("\nPick 0 for False or 1 for True")
    response = input("2. Marge is Homer's wife: ")
    correct_answer = ("1")
    if response == correct_answer:
        print("Correct")
        correct_answers_list.append('Question 2 is Correct')
        return 1    
    elif response != correct_answer:
        print("That's incorrect. The correct answer is 1")
        incorrect_answers_list.append('Question 2 is Incorrect')
        return 0
      
# Multiple Choice Questions 3-4
def question_3():
    print("\nChoose a letter a-e")
    response = input("3. How does Homer discipline Bart?: \n a. Extra Chores \n b. Whooping \n c. Choke \n d. No TV \n e. None of the Above")
    correct_answer = ("c")
    if response == correct_answer:
        print("Correct! Great Job!")
        correct_answers_list.append('Question 3 is Correct')
        return 1
    elif response != correct_answer:
        print("That's incorrect. The correct answer is c")
        incorrect_answers_list.append('Question 3 is Incorrect')
        return 0

def question_4():
    print("\nChoose a letter a-e")
    response = input("4. What is Bart's sister name?: \n a. Rachel \n b. Lisa \n c. Elyse \n d. Ashley \n e. None of the Above")
    correct_answer = ("b")
    if response == correct_answer:
        print("Correct! Awesome!")
        correct_answers_list.append('Question 4 is Correct')
        return 1
    elif response != correct_answer:
        print("The answer is b!")
        incorrect_answers_list.append('Question 4 is Incorrect')
        return 0

#Numeric Response Questions 5-6
def question_5():
    print("\nEnter a number")
    response = input("5. Marge has how many sisters?  ")
    correct_answer = ("2")
    if response == correct_answer:
        print("Correct!")
        correct_answers_list.append('Question 5 is Correct')
        return 1
    elif response != correct_answer:
        print("That answer is incorrect. Marge has 2 sisters")
        incorrect_answers_list.append('Question 5 is Incorrect')
        return 0

def question_6():
    print("\nEnter a number for question 6")
    response = input("6. How many pets do the Simpson's have?")
    correct_answer = ("2")
    if response == correct_answer:
        print("Correct! You did it!")
        correct_answers_list.append('Question 6 is Correct')
        return 1
    elif response != correct_answer:
        print("That answer is in correct. They have a cat and a dog")
        incorrect_answers_list.append('Question 6 is Incorrect')
        return 0
        print("\n")

# Result Logic
result = question_1() + question_2() + question_3() + question_4() + question_5() + question_6()
print("\n")

# Both Lists printed
print("Your Results:")
for i in correct_answers_list:
    print(i)
print("\n")
for i in incorrect_answers_list:
    print(i)
print("\n")

#Final Message Options
if result <= 1:
    print(f"You scored {result} out of 6. The Simpsons come on every night, watch it for a year then retake the quiz!")

elif result == 3 or 4:
    print(f"You scored {result} out of 6. This test is for real simpsons fans!")

elif result == 5:
    print(f"You scored {result} out of 6. Try again after two weeks.")

else:
    print("You are the biggest simpson fan on EARTH!!!")



