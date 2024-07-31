from easygui import * # Imports easy gui so I can use msgbox and other python extensions

# Welcomes user to this quiz in a msgbox

msgbox("Welcome to this Quiz, this is designed for people inbetween the ages of 8 - 13, if you are 14 or over you should try out the Cybersmart Youth Quiz!", title = "Welcome New User!")

name = enterbox("What is your name?", "Welcome to the Cybersmart Start Quiz") # Asks/Grabs the users name
age = integerbox("How old are you?", "Welcome to the Cybersmart Start Quiz") # Asks/Grabs the users age
total = 0 # Sets total to 0, resets when everyone ones the program 

# Checks if the user is inbetween age gaps provided

while age < 8 or age > 13:
    age = integerbox("Please enter an age from 8 to 13", "Welcome to the Cybersmart Start Quiz")

# Welcomes the user to the quiz, gives them a breif ruleset and explains what the quiz provides
    
msgbox("Hi "  + name + "!" + "\n\n The rules are simple. You will be given 3 questions to see if your Cyber Smart, If you get a question right the first try. you will get 1 point. If not, you will get two more tries. If you still get it wrong, you will be given the correct answer.", "Welcome to the Cybersmart Start Quiz", "Start now!")

# First Question to the quiz

a = buttonbox(str(name) + " , you want to join an online gaming site. Which of the following information is okay to post online? \n\n A. A nickname\n B. Your name\n C. Your email address", choices='a' 'b' 'c') # Provides the user with the question and three choices
if a == "a": # If the user gets the answer on the first try they following will run;
        total =(0+1) # Gives user a point for getting the question right on the first time
        msgbox(str(name) + " , you got your question right the first time") # Provides the user with the information that they got the question right on the first time
else :  # Repeats the question until they get it right or it repeats twice
        (total) # Sets total to be the same
        msgbox(str(name) + ", you got your question wrong!")  # If the user gets it wrong they'll be presented with this
        a = buttonbox(str(name) + " , Somone sends you a text that is hurtful and makes you feel bad about yourself. What should you do?", choices=["Delete the message and try to forget about it","Keep the text and show an adult you trust","Text the person back saying something mean to them"]) # Repeated Question
        if a == "a": # If they get it right within two goes they'll be presented with this
            total = (0) # Sets the total to neutral/adds no points since they got the question right but not on the first time
            msgbox(str(name) + ", you got your question right in this amount of trys\n\n" + str(2))

# Second Question of the quiz

c = buttonbox(str(name) + " , Someone in your class has posted their first video on YouTube and has asked you to comment on it. You don't think the video is good because the editing is very choppy. What could you comment? \n\n A. Your video is rubbish!\n B. Man, this is awful! Stick to playing sport or something.\n C. Congrats on your first video! Let me know if you'd like any help editing for your next video.", choices='a' 'b' 'c') # Provides the user with the question and three choices
if c == "c": # If the user gets the answer on the first try they following will run;
        total = (total+1) # Gives user a point for getting the question right on the first time
        msgbox(str(name) + ", you got your question right the first time") # Provides the user with the information that they got the question right on the first time
else :  # Repeats the question until they get it right or it repeats twice
        (total) # Sets total to be the same
        msgbox(str(name) + ", you got your question wrong!")  # If the user gets it wrong they'll be presented with this
        c = buttonbox(str(name) + " , Someone sends you a text that is hurtful and makes you feel bad about yourself. What should you do? \n\n A. Delete the message and try forget about it\n B. Keep the text and show an adult you trust\n C. Text the person back saying something mean to them", choices='a' 'b' 'c') # Repeated Question
        if c == "c":
         total = (total) # Sets the total to neutral/adds no points since they got the question right but not on the first time
         msgbox(str(name) + ", you got your question right in this amount of trys\n\n" + str(2))

# Third Question of the quiz

b = buttonbox(str(name) + " , Someone sends you a text that is hurtful and makes you feel bad about yourself. What should you do? \n\n A. Delete the message and try forget about it\n B. Keep the text and show an adult you trust\n C. Text the person back saying something mean to them", choices='a' 'b' 'c') # Provides the user with the question and three choices
if b == "b": # If the user gets the answer on the first try they following will run;
        total = (total+1)  # Gives user a point for getting the question right on the first time
        msgbox(str(name) + " , you got your question right the first time") # Provides the user with the information that they got the question right on the first time
else :
        (total) # Sets total to be the same
        msgbox(str(name) + ", you got your question wrong!")   # If the user gets it wrong they'll be presented with this
        b = buttonbox(str(name) + " , Someone sends you a text that is hurtful and makes you feel bad about yourself. What should you do? \n\n A. Delete the message and try forget about it\n B. Keep the text and show an adult you trust\n C. Text the person back saying something mean to them", choices='a' 'b' 'c') # Repeated Question
        if b == "b":
            total = (total) # Sets the total to neutral/adds no points since they got the question right but not on the first time
            msgbox(str(name) + ", you got your question right in this amount of trys\n\n" + str(2))

# Ends the quiz with the following msgbox, also presents the user with the total that they got

msgbox(str(name) + " well done! You've finished the quiz, you got " + str(total) + "/3 correct! If you want to you can retry this quiz, or move onto the next quiz for 14+ Cybersmart Youth Quiz, you can!.")