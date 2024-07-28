from easygui import * 

msgbox("Welcome to this Quiz, this is designed for people inbetween the ages of 8 - 13, if you are 14 or over you should try out the Cybersmart Youth Quiz!", title = "Welcome New User!")

name = enterbox("What is your name?", "Welcome to the Cybersmart Start Quiz")
age = integerbox("How old are you?", "Welcome to the Cybersmart Start Quiz")
total = 0

while age < 8 or age > 13:
    age = integerbox("Please enter an age from 8 to 13", "Welcome to the Cybersmart Start Quiz")
    
msgbox("Hi "  + name + "!" + "\n\n The rules are simple. You will be given 3 questions to see if your Cyber Smart, If you get a question right the first try. you will get 1 point. If not, you will get two more tries. If you still get it wrong, you will be given the correct answer.", "Welcome to the Cybersmart Start Quiz", "Start now!")

a = buttonbox(str(name) + " , you want to join an online gaming site. which of the following information is okay to post online? \n\n A. A nickname\n B. Your name\n C. Your email address", choices='a' 'b' 'c')
if a == "a":
        total = (total+1)
        msgbox("you got your question right the first time")
while a != "a":
        msgbox("you got your question wrong!")
        a = buttonbox(str(name) + " , you want to join an online gaming site. which of the following information is okay to post online? \n\n A. A nickname\n B. Your name\n C. Your email address", choices='a' 'b' 'c')
        if a == "a":
            total = (total)

b = buttonbox(str(name) + " , you want to join an online gaming site. which of the following information is okay to post online? \n\n A. A nickname\n B. Your name\n C. Your email address", choices='a' 'b' 'c')
if b == "b":
        total = (total+1)
        msgbox("you got your question right the first time")
while b != "b":
        msgbox("you got your question wrong!")
        b = buttonbox(str(name) + " , you want to join an online gaming site. which of the following information is okay to post online? \n\n A. A nickname\n B. Your name\n C. Your email address", choices='a' 'b' 'c')
        if b == "b":
            total = (total)

