import random

#------lists--------
NAME1 = ["Crystal", "Tranquil", "Gloomy", "Luminous", "Somber", "Crimson", "Jagged", "Dilapidated"]
NAME2 = ["River", "Pond", "Forest", "Clearing", "Pathway", "Cave", "Grave", "Statue"]
LOCT = ["store", "item"]
ENE = ["Bat", "Chamois", "Lynx", "Gray Wolf"]
DES = ["an imposing", "a threatening", "a concerning", "a worrisome"]
#------end of lists------
#-----FUNCTIONS-----
def getenemy():
    return random.choice(ENE)
#-----MAIN CODE-----
enc = 8
moon = 0
health = 100
print("WARNING: This game includes descriptions of graphic violence, and animal cruelty so it is not suitable for children below the age of 13")
print("Also none of the actions depicted in this game should actually be done")
play=input("do you still wish to play this game?").lower()

if play == "yes":
    print("You were on a path through the woods, a cool breeze carried the scent of pine needles through the air,")
    print("you continued walking for a while until you ralised that you had got lost without noticing,")
    print("after panicking for a moment, you managed to gather your thoughts and decide that you should first find a place to stay,")
    print("and so you set out into the woods, with nothing but your trusty knife in hand & the clothes on your back,")
    
    while enc>=8:
        print(f"You approach the {random.choice(NAME1)} {random.choice(NAME2)}.")
        location = random.choice(LOCT)
        while location == "store":
            print("As you walk down the path, you come across a store.")
            opt = input("Enter store or Continue down path\n").lower()
            if "continue" in opt or "path" in opt:
                print("You decide not to enter store you condtinue down the path")
                break
            if "enter" in opt or "store" in opt:
                sto = "yes"
                print("Blah blah blah I have wares and services, for a price of course. But you may only have one, must leave some for others you know")
                print(f"An elixer of health, for {random.randint(5,20)} coins.")
                print(f"I can sharpen your weapon {random.randint(5,20)} coins.")
                print(f"A patch for your garments {random.randint(5,20)} coins.")
                while sto == "yes":
                    buy = input("Would you like to purchase any of my items? Or just leave without buying anything.\n").lower()
                    if "elixer" in buy or "health" in buy or "healing" in buy:
                        print("You pay the man and drink his elixer, as you do you feel QWERTY")
                        health =+ random.randint(30,50)
                        print("You store exit")
                        break
                    elif "sharpen" in buy or "weapon" in buy:
                        print("You give him the money and the merchant takes your weapon and sharpens it on a large stone block.")
                        attack =+ random.randint(10,20)
                        print("You store exit")
                        break
                    elif "patch" in buy or "garments" in buy:
                        print("As you hand him the coins he takes a sewing kit from below his table and sews a large patch to the chest of your garments.")
                        defense =+ random.randint(10,20)
                        print("You store exit")
                        break
                    elif "leave" in buy:
                        print("You give your regards as you exit the man's store. There seems to be no choice other than to continue down the path, and so you do just that.")
                        break
                    else:
                        print("You sit there, confused by choice.")
                break
        while location == "item":
            #item stuff
            print("slay")

        #Enemy 
        echo = getenemy()
        print(f"As you walk there appeasrs {random.choice(DES)} looking {echo}.")



else:
    print("Sorry you don't wanna play the game I guess")

