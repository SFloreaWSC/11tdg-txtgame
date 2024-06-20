import random

#------lists--------
NAME1 = ["Crystal", "Tranquil", "Gloomy", "Luminous", "Somber", "Crimson", "Jagged", "Dilapidated"]
NAME2 = ["River", "Pond", "Forest", "Clearing", "Pathway", "Cave", "Grave", "Statue"]
LOCT = ["store", "item"]
ENE = ["Bat", "Chamois", "Lynx", "Gray Wolf"]
DES = ["an imposing", "a threatening", "a concerning", "a worrisome"]
#------end of lists------
#-----FUNCTIONS-----
def checkstats():
    return print(f"Your health is {health}\nYour attack is {attack}\nYour defense is {defense}")
#-----MAIN CODE-----
encon = 8
moon = 0
health = 100
attack = 10
defense = 5
pdamage = random.randint(attack-5,attack+5)
print(pdamage)
pdamage = random.randint(attack-5,attack+5)
print(pdamage)
pdamage = random.randint(attack-5,attack+5)
print(pdamage)
print("WARNING: This game includes descriptions of graphic violence, and animal cruelty so it is not suitable for children below the age of 13")
print("Also none of the actions depicted in this game should actually be done")
play=input("do you still wish to play this game?").lower()

if play == "yes":
    print("You were on a path through the woods, a cool breeze carried the scent of pine needles through the air,")
    print("you continued walking for a while until you ralised that you had got lost without noticing,")
    print("after panicking for a moment, you managed to gather your thoughts and decide that you should first find a place to stay,")
    print("and so you set out into the woods, with nothing but your trusty knife in hand & the clothes on your back,")
    
    while encon >= 8:
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
                one = random.randint(5,20)
                two = random.randint(9,20)
                three =  random.randint(9,20)
                print(f"An elixer of health, for {one} coins.")
                print(f"I can sharpen your weapon {two} coins.")
                print(f"A patch for your garments {three} coins.")
                while sto == "yes":
                    buy = input("Would you like to purchase any of my items? Or just leave without buying anything.\n").lower()
                    if "elixer" in buy or "health" in buy or "healing" in buy and moon <= one:
                        print("You pay the man and drink his elixer, as you do you feel QWERTY")
                        print(f"Your defense is now {defense}.")
                        health += random.randint(20,50)
                        print("You store exit")
                        break
                    elif "sharpen" in buy or "weapon" in buy and moon <= two:
                        print("You give him the money and the merchant takes your weapon and sharpens it on a large stone block.")
                        print(f"Your attack is now {attack}.")
                        attack += random.randint(5,10)
                        print("You store exit")
                        break
                    elif "patch" in buy or "garments" in buy and moon <= three:
                        print("As you hand him the coins he takes a sewing kit from below his table and sews a large patch to the chest of your garments.")
                        defense += random.randint(5,10)
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
        encon -= 1

        #Enemy 
        echo = random.choice(ENE)
        print(f"As you walk there appeasrs {random.choice(DES)} looking {echo}.")
        while "Bat" in echo:
            ehealth = random.randint(20,30)
            turn = random.randint(1,4)
            if turn >= 2:    
                print("You approach the bat, it clearly isn't happy to see you.")
                aorr = input("Should you make an attack or run away?").lower()
                if "run" in aorr:
                    print("You attempt to run away.")
                    running = random.randint(1,10)
                    if running == 1:
                        break
                    if running >= 2:
                        turn = 1
                if "attack" in aorr:
                    pdamage = random.randint(attack-5,attack+5)
                    print(f"You attack the bat, dealing {pdamage}")
            if turn == 1:
                edamage = random.randint(10,15)
                print(f"The bat ambushes you, your health lowers by {edamage}")
                health -= 1

                break
        while "Chamois" in echo:
            print("chamois")
            break
        while "Lynx" in echo:
            print("lynx")
            break
        while "Wolf" in echo:
            print("wolf")
            break
        encon -= 1

    #BOSSFIGHT HERE

else:
    print("Sorry you don't wanna play the game I guess")

