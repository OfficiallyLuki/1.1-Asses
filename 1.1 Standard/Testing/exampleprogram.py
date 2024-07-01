from easygui import *

birth_year = integerbox ("Enter your year of birth (eg 2004):", upperbound= 2100)

year_65 = birth_year + 65

msgbox (year_65)