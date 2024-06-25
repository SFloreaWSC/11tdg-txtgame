import random

#------LISTS--------
NAME1 = ["Crystal", "Tranquil", "Gloomy", "Luminous", "Somber", "Crimson", "Jagged", "Dilapidated"]
NAME2 = ["River", "Pond", "Forest", "Clearing", "Flowerbed", "Cave", "Grave", "Statue"]
LOCT = ["store", "item"]
ENE = ["Bat", "Chamois", "Lynx", "Gray Wolf"]
DES = ["an imposing", "a threatening", "a concerning", "a worrisome"]
ITE = ["Shield", "Weapon"]
#-----FUNCTIONS-----
def checkstats():
    return print(f"Your health is {health}\nYour attack is {attack}\nYour defense is {defense}\n")
#-----MAIN CODE-----
notno=True
encon = 8
moon = 0
health = 100
attack = 10
defense = 10

while notno==True:
    print("WARNING: This game includes descriptions of graphic violence, and animal cruelty so it is not suitable for children below the age of 13")
    print("Also none of the actions depicted in this game should actually be done")
    play=input("do you still wish to play this game? ").lower()
    if play=="no":
        print("Sorry you don't wanna play the game I guess")
        break
    elif play!="yes" and play!='no':
        print("it has to be yes or no")
    elif play == "yes":
        while True:
            
            print("\nYou were on a path through the woods, a cool breeze carried the scent of pine needles through the air,")
            print("you continued walking for a while until you realised that you had got lost without noticing,")
            print("after panicking for a moment, you managed to gather your thoughts and decide that you should first find a place to stay,")
            print("and so you set out into the woods, with nothing but your trusty knife in hand & the clothes on your back.\n")
            
            while encon > 0:
                turn  = "x"
                nam1 = random.choice(NAME1)
                nam2 = random.choice(NAME2)
                print(f"You approach the {nam1} {nam2}.")
                location = "store" #random.choice(LOCT)
                while location == "store":
                    print("As you walk down the path, you come across what appeared to be a rickety looking wagon with shuttered windows.")
                    while location == "store":
                        opt = input("Do you want to Enter store, Continue down path, or Check your stats?\n").lower()
                        if "stat" in opt or "check" in opt:
                            checkstats()
                        if "continue" in opt or "path" in opt:
                            print("You decide not to enter store you continue down the path")
                            break
                        if "enter" in opt or "store" in opt:
                            sto = "yes"
                            print("As you approached the Wagon the shutters suddenly flew open, causing you to jump back with a start, after letting your heartrate go \n down for a moment you looked into the inky black window of the wagon & you saw what appeared to be the face of an old mam behind \n a counter of sorts, after a moment or two he seemed to notice you & he said with a raspy voice 'oh, traveler, I hadn't noticed you there, sorry' he said, giving you a toothy grin. Then he started speaking again & said 'I offer a wide range of wares & services that you /n can purchase, if you have the coin of course' he paused for a moment, seemingly contemplating something & the  eventually said 'but you may only pick one from three, I have other customers & they cannot go without supplies' he then placed three different items on the table")
                            one = random.randint(5,20)
                            two = random.randint(9,20)
                            three =  random.randint(9,20)
                            print(f"You look skinny, I can offer you an elixir of health, for {one} coins to put some meat on your bones")
                            print(f"That knife of yours looks rather dull, if you wish you may purchase a whetstone to sharpen it, but it is fragile & so will only work once. you can buy it for {two} coins.")
                            print(f"A patch for your garments for {three} coins.")
                            while sto == "yes":
                                buy = input("Would you like to purchase any of my items? Or just leave without buying anything.\n").lower()
                                # moon is money (for some reason)
                                if "elixir" in buy or "health" in buy or "healing" in buy and moon <= one:
                                    print("You pay the man and drink his elixir, as you do you feel QWERTY")
                                    health += random.randint(20,40)
                                    print(f"Your health is now {health}.")
                                    print("You store exit")
                                    break
                                elif "sharpen" in buy or "weapon" in buy and moon <= two:
                                    print(f"You give him the money and the merchant takes your weapon and sharpens it on a large stone block.\nYour attack is now {attack}.")
                                    attack += random.randint(5,10)
                                    print(f"Your attack is now {attack}.")
                                    print("You store exit")
                                    break
                                elif "patch" in buy or "garments" in buy and moon <= three:
                                    print("As you hand him the coins he takes a sewing kit from below his table and sews a large patch to the chest of your garments.")
                                    defense += random.randint(5,10)
                                    print(f"Your defense is now {defense}.")
                                    print("You store exit")
                                    break
                                elif "leave" in buy:
                                    abcd = input("You give your regards as you exit the man's store.\nContinue down path or Check stats?\n").lower()
                                    if "stat" in abcd or "check" in abcd:
                                        checkstats()
                                        break
                                    if "continue" in abcd or "path" in abcd:
                                        print("INSERT CONTINUE DOWN PATH TEXT HERE KIT")
                                else:
                                    print("You stand there, confused by choice.")
                        break
                    break
                while location == "item":
                    #item stuff
                    print(f"As you walk down the path you notice something peaking out from the {nam2}")
                    if "Pond" in nam2 or "River" in nam2:
                        print("placeholder")
                    if "Statue" in nam2:
                        print("placeholder")
                    if "Forest" in nam2 or "Flowerbed" in nam2 or "Cave" in nam2:
                        while True:
                            print(f"You walk towards the {nam2}, noticing something inside. As you enter the {nam2} you walk to the said object and pick it up.")
                            itemblah = random.choice(ITE)
                            print(f"It's a {itemblah}, which would clearly would be better than whatever you have now.")
                            if itemblah == "Shield":
                                itempick = input("The shield might up your defense, but it would make it harder to attack and lower your attack. \nDo you want to take it?\n")
                            if itemblah == "Weapon":
                                itempick == input("This weapon may give you a higher attack damage, but you'd have to be more free to move to do so, so you'd have to get rid of some of your protective gear. \nDo you want to take it?\n")
                            if "yes" in itempick or "yeah" in itempick or "ok" in itempick:
                                if itemblah == "Shield":
                                    ite1 = random.randint(3-9)
                                    defense += ite1
                                    ite2 = random.randint(3-9)
                                    attack -= ite2
                                    print("higher def lower atk")
                                if itemblah == "Weapon":
                                    ite1 = random.randint(3-9)
                                    attack += ite1
                                    ite2 = random.randint(3-9)
                                    defense -= ite2
                                    print("lower def higher atk")
                                break
                            if "no" in itempick or "not" in itempick:
                                print("placehodler")
                                break
                            else:
                                "You sit there, confused by choice."
                    input("It is time to move forward.")
                    break
                encon -= 1

                #Enemy 
                echo = random.choice(ENE)
                print(f"As you walk there appeasrs {random.choice(DES)} looking {echo}.")
                while "Bat" in echo:
                    ehealth = random.randint(20,30)
                    turn = random.randint(1,4)
                    if turn >= 2:    
                        print("You approach the bat, it clearly isn't happy to see you.")
                        aorr = input("Should you make an attack or run away?\n").lower()
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
                    print("chamois ")
                    break
                while "Lynx" in echo:
                    print("lynx")
                    break
                while "Wolf" in echo:
                    print("wolf")
                    break
                encon -= 1

            #BOSSFIGHT HERE

    elif play=="no":
        print("Sorry you don't wanna play the game I guess")
    else:
        print("it has ")

