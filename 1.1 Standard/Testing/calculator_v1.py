from easygui import *

num1 = integerbox("Number 1:", upperbound = 1000)
operator = buttonbox(choices = ["+","-","/","*"])
num2 = integerbox("Number 2:", upperbound = 1000)

if operator == "+":
    answer = num1 + num2
elif operator == "-":
    answer = num1 - num2
elif operator == "/":
    answer = num1/num2
else:
    answer = num1*num2

msgbox("Answer = " + str(answer))
    
