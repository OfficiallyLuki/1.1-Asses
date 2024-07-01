from easygui import *
import random

player_name = enterbox("Hi! What is your name?")
msgbox("Hi " + player_name + "! Welcome to the Guessing Game.")

number = random.randint(0,5)
print(number)

answer = integerbox("I'm thinking of a number from 0 to 5. Guess what it is.")

if answer == number:
    msgbox("You got it right first time!")
else:
    answer = integerbox("Try again.")



    






