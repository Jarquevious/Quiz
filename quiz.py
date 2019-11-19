# The Simpson's Quiz; 1 =True and 0m = False
answer_list = []
def question_1():
    response = input("1. Homer has 4 Kids: ")
    correct_answer = ("0")
    # answer_list.append()
    if response == correct_answer:
        return 0
        print("Correct")
    elif response != correct_answer:
        print("wrong answer")
 
question_1()