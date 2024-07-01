from easygui import *
age = 18
player_age = integerbox("How old are you?")
if player_age > 18:
    msgbox("Welcome to The Phoenix Odyssey!")
elif player_age >= 14:
    msgbox("Ask a parent to watch you play this game.")
else:
    msgbox("You’re not old enough to play this game.")


