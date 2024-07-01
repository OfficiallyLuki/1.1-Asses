from easygui import*

a = buttonbox("What type of assessment have you completed" , choices = ["Test", "Assesment"])
total = integerbox ("How many marks was the " + str(a) + " out of?", upperbound= 1000)
score = integerbox ("How many marks did you get in the " + str(a), upperbound = (total))
percentage = (score/total)*100
msgbox ("You persentage for the " + str(a) + " is " + str(percentage))  