from easygui import *
age = 18
player_age = integerbox("How old are you?")
if player_age <= 18:
    msgbox("Note: This game is intended for people over 18.")
else:
    msgbox("Yes! You're old enough to play this game!")
msgbox("Welcome to The Phoenix Odyssey!")
