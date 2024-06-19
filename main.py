import random

#lists
NAME1 = ["Crystal", "Tranquil", "Gloomy", "Luminous", "Somber", "Crimson", "Jagged", "Dilapidated"]
NAME2 = ["River", "Pond", "Forest", "Clearing", "Pathway", "Cave", "Grave", "Statue"]
LOCT = ["store", "item", "enemy"]
#end of lists
#-----FUNCTIONS-----

#-----MAIN CODE-----
enc = 8
moon = 0
print("WARNING: This game includes descriptions of graphic violence, & animal cruelty & is not suitable for children below the age of 13")
play=input("do you still wish to play this game?").lower()

if play == "yes":
    slay = input("AAAAAAAA").lower()
    print(slay)
    print("You were on a path through the woods, a cool breeze carried the scent of pine needles through the air,")
    print("you continued walking for a while until you ralised that you had got lost without noticing,")
    print("after panicking for a moment, you managed to gather your thoughts and decide that you should first find a place to stay,")
    print("& so you set out into the woods, with nothing but your trusty knife in hand & the clothes on your back,")
    while enc>=8:
        print(f"You enter the {random.choice(NAME1)} {random.choice(NAME2)}.")
        location = random.choice(LOCT)
        if location == "store":
            #store stuff
            print("you come across store")
            opt = input("Enter store or Continue down path").lower()
            if opt == "enter" or opt == "enter store":
                pri = random.randint(50,100)
                print(f"Item 1 healing {pri} coins")
                print(f"item 2 attack {pri} coins")
                print(f"item 3 defence {pri} coins")
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
    print("Sorry you dont wanna play the game I guess")

