from easygui import *
msgbox("Welcome to this Quiz, this is designed for people inbetween the ages of 5 - 11, we have two different styled quizs depending on your age group. All questions are relating to New Zealand, have fun!", title = "Welcome New User!")

# Setting a name/username to be displayed throughout the program and verifying the age group of a user
name = ""
while name == "":
    name = enterbox ("Hey there! Please enter your name to continue!")


mini_age = 5
maxi_age = 11
age = integerbox (str(name) + ", enter an age from 5 - 11 (your age):", title="Verifying your age group.")

if age > mini_age or age < maxi_age:
    msgbox (str(name) + ", you are not in the age group required, please try again when your in the correct age group.")

elif age < mini_age or age > maxi_age:
    msgbox ("test")
