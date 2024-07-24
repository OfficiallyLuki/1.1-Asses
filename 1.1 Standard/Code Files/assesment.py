from easygui import * 

msgbox("Welcome to this Quiz, this is designed for people inbetween the ages of 8 - 13, if you are 14 or over you should try out the Cybersmart Youth Quiz!", title = "Welcome New User!")

name = enterbox("What is your name?", "Welcome to the NZ TRIVIA Game")
age = integerbox("How old are you?", "Welcome to the NZ TRIVIA Game")

while age < 8 or age > 13:
    age = integerbox("Please enter an age from 8 to 13", "Welcome to the NZ TRIVIA Game")
    
msgbox("Hi "  + name + "!" + "\n\nQuiz intro/rules go here", "Welcome to the NZ TRIVIA Game", "Start")