#Sylvia's Game
# Requirements
#  1. Will prompt the user for a random arithmetic problem
#     (addition or subtraction) involving numbers between 0 and 20.
#  2. If the user responds correctly, then the program will print "Success!"
#  3. If the user responds incorrectly, then the user will 
#     print "Sorry, try again!"
#  4. The program will loop until the user inputs the text "quit"

import random

operations = [ '+', '-' ]

def get_random_op():
  return operations[ get_random_number(1) ]

def get_random_number(r):
  return random.randint(0, r)

def get_correct_ans(foo1, foo2, op):
  if op == '+':
    return foo1 + foo2
  else:
    return foo1 - foo2 
while True:
    r1 = get_random_number(20)
    r2 = get_random_number(20)
    op = get_random_op()
    if r1 < r2:
        num1 = r2
        num2 = r1
    else:
        num1 = r1
        num2 = r2
    user_input = input(f"{num1} {op} {num2} = ")
    start = time.time()   
    correct_ans = get_correct_ans(num1, num2, op)
    if user_input == 'quit':
        break
    try:
        user_ans = int(user_input)
        is_correct = False
        if user_ans == correct_ans:
            is_correct = True
        else:
            is_correct = False
    except ValueError:
        is_correct = False        
    if is_correct == True:
        end = time.time()
        print("Success, it took you (end-start) seconds to answer.")
    else:
        print(f"Sorry, should be {correct_ans} try again")
