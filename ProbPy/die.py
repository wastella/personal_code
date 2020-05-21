import random as rand

def roll(sides):
    try:
        return rand.randrange(sides)
    except ValueError: 
        print("That is not a valid type")

 
