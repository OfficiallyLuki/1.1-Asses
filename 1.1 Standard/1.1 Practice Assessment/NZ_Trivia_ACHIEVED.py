from easygui import *

name = enterbox("What is your name?", "Welcome to the NZ TRIVIA Game")
age = integerbox("How old are you?", "Welcome to the NZ TRIVIA Game")

while age < 5 or age > 11:
    age = integerbox("Please enter an age from 5 to 11", "Welcome to the NZ TRIVIA Game")
    
msgbox("Hi "  + name + "!" + "\n\nQuiz intro/rules go here", "Welcome to the NZ TRIVIA Game", "Start")

# Sets questions and answers for players 7-years and under
questions_a = ["What is the capital city of New Zealand?\n\nA: Auckland\nB: Wellington\nC: Christchurch\nD: Hamilton\n", "Which city is known as 'The Garden City'?\n\nA: Wellington\nB: Christchurch\nC: Paeroa\nD: Auckland\n", "Where did L&P soda orginally come from?\n\nA: Putaruru\nB: Waihi\nC: Paeroa\nD: Auckland\n", "In what month is Matariki celebrated?\n\nA: April\nB: May\nC: June\nD: July\n", "What colour is Kakariki?\n\nA: Green\nB: Blue\nC: Black\nD: Grey\n"]
answers_a = ["B", "B", "C", "C", "A"] #these are the answers to the multi-choice questions (in a list)

# Sets questions and answers for players over 7 years old
questions_b = ["What is the name of the stretch of water that separates the North and South Islands?\n\nA: Wellington Strait\nB: Tasman Channel\nC: Cook Strait\nD: Kaikoura Strait\n", "Which New Zealand city houses the Beehive?\n\nA: Wellington\nB: Christchurch\nC: Paeroa\nD: Auckland\n", "Which town has a giant carrot as a landmark?\n\nA: Taihape\nB: Waihi\nC: Paeroa\nD: Ohakune\n", "Where is 90 mile beach?\n\nA: Top of the North Island\nB: Bottom of the South Island\nC: Bottom of the North Island\nD: Top of the South Island\n", "When was the Treaty of Waitangi signed?\n\nA: 1815\nB: 1840\nC: 1855\nD: 1875\n"]
answers_b = ["C", "A", "D", "A", "B"]

q_score = 0  #q_score set to zero. This is done so that can start program with no score

if age <= 7: 
    # Question 1
    player_quiz = buttonbox(questions_a[0], "Question 1", choices=["A", "B", "C", "D"])
    if player_quiz == answers_a[0]:
        msgbox("Well done, "  + name + "! " + "You got it right!")
        q_score = q_score + 1
    else:
        q_response = msgbox("Sorry, "  + name + "! That's not right.\nThe correct answer is " + answers_a[0])
            
    # Question 2
    player_quiz = buttonbox(questions_a[1], "Question 2", choices=["A", "B", "C", "D"])
    if player_quiz == answers_a[1]:
        msgbox("Well done, "  + name + "! " + "You got it right!")
        q_score = q_score + 1
    else:
        q_response = msgbox("Sorry, "  + name + "! That's not right.\nThe correct answer is " + answers_a[1])

    # Question 3
    player_quiz = buttonbox(questions_a[2], "Question 3", choices=["A", "B", "C", "D"])
    if player_quiz == answers_a[2]:
        msgbox("Well done, "  + name + "! " + "You got it right!")
        q_score = q_score + 1
    else:
        q_response = msgbox("Sorry, "  + name + "! That's not right.\nThe correct answer is " + answers_a[2])

else:
   # Question 1
    player_quiz = buttonbox(questions_b[0], "Question 1", choices=["A", "B", "C", "D"])
    if player_quiz == answers_b[0]:
        msgbox("Well done, "  + name + "! " + "You got it right!")
        q_score = q_score + 1
    else:
        q_response = msgbox("Sorry, "  + name + "! That's not right.\nThe correct answer is " + answers_b[0])
            
    # Question 2
    player_quiz = buttonbox(questions_b[1], "Question 2", choices=["A", "B", "C", "D"])
    if player_quiz == answers_b[1]:
        msgbox("Well done, "  + name + "! " + "You got it right!")
        q_score = q_score + 1
    else:
        q_response = msgbox("Sorry, "  + name + "! That's not right.\nThe correct answer is " + answers_b[1])

    # Question 3
    player_quiz = buttonbox(questions_b[2], "Question 3", choices=["A", "B", "C", "D"])
    if player_quiz == answers_b[2]:
        msgbox("Well done, "  + name + "! " + "You got it right!")
        q_score = q_score + 1
    else:
        q_response = msgbox("Sorry, "  + name + "! That's not right.\nThe correct answer is " + answers_b[2])
msgbox(str(name) + ", you got " + str(q_score) + " questions right.\nYour score: " + str(q_score) + "/3", "NZ TRIVIA Game")

msgbox("Thanks for playing the NZ TRIVIA Game!") 
