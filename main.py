import random

#lists
NAME1 = ["Crystal", "Tranquil", "Gloomy", "Luminous", "Somber", "Crimson", "Jagged", "Dilapidated"]
NAME2 = ["River", "Pond", "Forest", "Clearing", "Pathway", "Cave", "Grave", "Statue"]
LOCT = ["store", "item", "enemy"]
LOCD = []
#end of lists
#-----FUNCTIONS-----

#-----MAIN CODE-----
enc = 8
moon = 0
print("WARNING: This game includes descriptions of graphic violence, and animal cruelty so it is not suitable for children below the age of 13")
print("Also none of the actions depicted in this game should actually be done")
play=input("do you still wish to play this game?").lower()

if play == "yes":
    print("You were on a path through the woods, a cool breeze carried the scent of pine needles through the air,")
    print("you continued walking for a while until you realised that you had got lost without noticing,")
    print("after panicking for a moment, you managed to gather your thoughts before realising that you have to escape before nightfall")
    print("& so you set out into the woods, with nothing but your trusty knife in hand & the clothes on your back,")
    while enc>=8:
        print(f"You enter the {random.choice(NAME1)} {random.choice(NAME2)}.")
        location = random.choice(LOCT)
        if location == "store":
            #store stuff
            print("you come across store")
            opt = input("Enter store or Continue down path").lower()
            if opt == "enter":
                print("slauy")
        elif location == "item":
            #item stuff
            print("slay")
        elif location == "enemy":
            #enemy stuff
            print("slay")
#   Safe space (1)
#   if store = true: options to use stuff
#   keep track of money and health

#   Enemy 
else:
    print("Sorry you don't wanna play the game I guess")

