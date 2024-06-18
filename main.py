import random

#lists
NAME1 = ["Crystal", "Tranquil", "Gloomy", "Luminous", "Somber", "Crimson", "Jagged", "Dilapidated"]
NAME2 = ["River", "Pond", "Forest", "Clearing", "Pathway", "Cave", "Grave", "Statue"]
#end of lists
#-----FUNCTIONS-----

#-----MAIN CODE-----
print("WARNING: This game includes descriptions of graphic violence, & animal cruelty & is not suitable for children below the age of 13")
play=input("do you still wish to play this game?").lower()
if play =="yes".lower():
    print("You were on a path through the woods, a cool breeze carried the scent of pine needles through the air")
    print("you continued walking for a while until you ralised that you had got lost without noticing")
    print("after panicking for a moment, you managed to gather your thoughts and decide that you should first find a place to stay")
    print("& so you set out into the woods, with nothing but your trusty knife in hand & the clothes on your back ")
else:
    print("Sorry you dont wanna play the game I guess")

while True:
    print(f"you enter {random.choice(NAME1)} {random.choice(NAME2)}")
    input("slauy")
#   Safe space (1)
#   if store = true: options to use stuff
#   keep track of money and health

#   Enemy 