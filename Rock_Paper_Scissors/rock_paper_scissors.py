import random
print("what is your name?")
name = input()    

print("Welcome {}, we will be playing rock(r) paper(p) scissors(s)".format(name))
   
print("Choose r, p, or s")

player_input_s = input()

computer_input = random.randint(1, 3)
def letter_to_number(player_input_s):
    if player_input_s == 'R' or player_input_s == 'r':
        return 1
    if player_input_s == 'S' or player_input_s == 's':
        return 2
    if player_input_s == 'P' or player_input_s == 'p':
        return 3

player_input = letter_to_number(player_input_s)

if  player_input < 0:
    print("oops, you said {}, which was not r, p or s".format(player_input_s))

if player_input == 1 and computer_input == 3:
    print("Rock vs Scissors, you won")
elif player_input == 2 and computer_input == 1:
    print("Paper vs Rock, you won")
elif player_input == 3 and computer_input == 2:
    print("Paper vs Scissors, you won")
elif player_input == 3 and computer_input == 1:
    print("Rock vs Scissors, you lost")
elif player_input == 1 and computer_input == 2:
    print("Rock vs Paper, you lost")
elif player_input == 2 and computer_input == 3:
    print("Paper vs Scissors, you lost")
elif player_input == computer_input:
    print("It was a tie")



