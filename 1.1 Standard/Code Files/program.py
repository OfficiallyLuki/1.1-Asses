from easygui import *

name = enterbox("What is your name?", "Welcome to the NZ TRIVIA Game")
age = integerbox("How old are you?", "Welcome to the NZ TRIVIA Game")

while age < 5 or age > 11:
    age = integerbox("Please enter an age from 5 to 11", "Welcome to the NZ TRIVIA Game")
    
msgbox("Hi "  + name + "!" + "\n\nQuiz intro/rules go here", "Welcome to the NZ TRIVIA Game", "Start")