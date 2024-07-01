from easygui import *

fahrenheit = integerbox ("Enter the degress in Fahrenheit to be converted to Celsius", upperbound= 300)

celsius = (fahrenheit - 32) / 1.8

msgbox(str(fahrenheit) + "F is the same as " + str(celsius) + "C")

