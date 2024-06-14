import random

#lists
NAME1 = ["Crystal", "Tranquil", "Gloomy", "Luminous", "Somber", "Crimson", "Jagged", "Dilapidated"]
NAME2 = ["River", "Pond", "Forest", "Clearing", "Pathway", "Cave", "Grave", "Statue"]
#end of lists
#-----FUNCTIONS-----

#-----MAIN CODE-----
print("WARNING: This game includes descriptions of graphic violence, & animal cruelty & is not suitable for children below the age of 13")
play=input("do you still wish to play this game?").lower()
if play =="yes":
    print("the game")
else:
    print("Sorry you dont wanna play the game I guess")

while True:
    print(f"you enter {random.choice(NAME1)} {random.choice(NAME2)}")
    input("slauy")
#   Safe space (1)
#   if store = true: options to use stuff
#   keep track of money and health

#   Enemy 