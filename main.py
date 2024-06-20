import random

#lists
NAME1 = ["Crystal", "Tranquil", "Gloomy", "Luminous", "Somber", "Crimson", "Jagged", "Dilapidated"]
NAME2 = ["River", "Pond", "Forest", "Clearing", "Pathway", "Cave", "Grave", "Statue"]
LOCT = ["store", "item", "enemy"]
ENE = ["bat", "chamois", "lynx", "wolf"]
#end of lists
#-----FUNCTIONS-----
def wares():
    print(f"An elixer of health, for {random.randint(5,20)} coins.")
    print(f"I can sharpen your weapon {random.randint(5,20)} coins.")
    print(f"A patch for your garments {random.randint(5,20)} coins.")
#-----MAIN CODE-----
enc = 8
moon = 0
print("WARNING: This game includes descriptions of graphic violence, and animal cruelty so it is not suitable for children below the age of 13")
print("Also none of the actions depicted in this game should actually be done")
play=input("do you still wish to play this game?").lower()

if play == "yes":
    print("You were on a path through the woods, a cool breeze carried the scent of pine needles through the air,")
    print("you continued walking for a while until you ralised that you had got lost without noticing,")
    print("after panicking for a moment, you managed to gather your thoughts and decide that you should first find a place to stay,")
    print("and so you set out into the woods, with nothing but your trusty knife in hand & the clothes on your back,")
    
    while enc>=8:
        print(f"You enter the {random.choice(NAME1)} {random.choice(NAME2)}.")
        location = random.choice(LOCT)
        if location == "store":
            #store stuff
            print("you come across store")
            opt = input("Enter store or Continue down path\n").lower()
            if opt == "enter" or opt == "enter store":
                print("Blah blah blah I have wares and services, for a price of course. But you may only have one, must leave some for others you know")
                wares()
                buy = input("Would you like to purchase any of my items?\n").lower()
                if buy == "elixer":
                    print("You drink his elixer, as you do you feel QWERTY")
                    health =+ random.randint(30,50)
            if opt == "continue" or opt == "continue down" or opt == "continue down path":
                print("You decide not to enter store you condtinue down the path")
        elif location == "item":
            #item stuff
            print("slay")
        elif location == "enemy":
            #enemy stuff
            print("slay")
        #   Enemy 
        print("As you walk there appeasrs an enemtny")

else:
    print("Sorry you dont wanna play the game I guess")

