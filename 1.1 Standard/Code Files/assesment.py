from easygui import * 

msgbox("Welcome to this Quiz, this is designed for people inbetween the ages of 8 - 13, if you are 14 or over you should try out the Cybersmart Youth Quiz!", title = "Welcome New User!")

name = enterbox("What is your name?", "Welcome to the Cybersmart Start Quiz")
age = integerbox("How old are you?", "Welcome to the Cybersmart Start Quiz")
total = 0

while age < 8 or age > 13:
    age = integerbox("Please enter an age from 8 to 13", "Welcome to the Cybersmart Start Quiz")
    
msgbox("Hi "  + name + "!" + "\n\n The rules are simple. You will be given 3 questions to see if your Cyber Smart, If you get a question right the first try. you will get 1 point. If not, you will get two more tries. If you still get it wrong, you will be given the correct answer.", "Welcome to the Cybersmart Start Quiz", "Start now!")

a = buttonbox(str(name) + " , you want to join an online gaming site. Which of the following information is okay to post online? \n\n A. A nickname\n B. Your name\n C. Your email address", choices='a' 'b' 'c')
if a == "a":
        total = (total+1)
        msgbox(str(name) + " , you got your question right the first time")
while a != "a":
        msgbox(str(name) + " , you got your question wrong!")
        a = buttonbox(str(name) + " , you want to join an online gaming site. which of the following information is okay to post online? \n\n A. A nickname\n B. Your name\n C. Your email address", choices='a' 'b' 'c')
        if a == "a":
            total = (total)

c = buttonbox(str(name) + " , Someone in your class has posted their first video on YouTube and has asked you to comment on it. You don't think the video is good because the editing is very choppy. What could you comment? \n\n A. Your video is rubbish!\n B. Man, this is awful! Stick to playing sport or something.\n C. Congrats on your first video! Let me know if you'd like any help editing for your next video.", choices='a' 'b' 'c')
if c == "c":
        total = (total+1)
        msgbox(str(name) + " , you got your question right the first time")
while c != "c":
        msgbox(str(name) + ", you got your question wrong!")
        c = buttonbox(str(name) + " , Someone sends you a text that is hurtful and makes you feel bad about yourself. What should you do? \n\n A. Delete the message and try forget about it\n B. Keep the text and show an adult you trust\n C. Text the person back saying something mean to them", choices='a' 'b' 'c')
        if c == "c":
            total = (total)

b = buttonbox(str(name) + " , Someone sends you a text that is hurtful and makes you feel bad about yourself. What should you do? \n\n A. Delete the message and try forget about it\n B. Keep the text and show an adult you trust\n C. Text the person back saying something mean to them", choices='a' 'b' 'c')
if b == "b":
        total = (total+1)
        msgbox(str(name) + " , you got your question right the first time")
while b != "b":
        msgbox(str(name) + " , you got your question wrong!")
        b = buttonbox(str(name) + " , Someone sends you a text that is hurtful and makes you feel bad about yourself. What should you do? \n\n A. Delete the message and try forget about it\n B. Keep the text and show an adult you trust\n C. Text the person back saying something mean to them", choices='a' 'b' 'c')
        if b == "b":
            total = (total)

msgbox(str(name) + " well done! You've finished the quiz, you got " + str(total) + "/3 correct! If you want to you can retry this quiz, or move onto the next quiz for 14+ Cybersmart Youth Quiz.")