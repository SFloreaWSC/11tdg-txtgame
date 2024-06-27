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
def endingdie():
    return print("You suddenly become acutely aware of the mass amount of pain coursing through your body. \nYou can feel it pulsing through your veins. Pure, unadulterated agony. \nYour legs give way and you collapse, unable to even try to move. \nThe animals in the forest surrounding you take notice, approaching you, they start to dig into your flesh with their razor sharp teeth. \nYour entire existence acting as nothing more than a snack for them. \n\nYou never should have come here.")
#-----MAIN CODE-----
boss=True
poison=False
notno=True
turn1=True
#CHANGE THIS BACK ONCE DONE WITH BOSSFIGHT
encon = 0
#REMEMBER ITS THIS ONE
moon = 0
health = 100
attack = 10
defense = 10
abcd = "x"
ehealth = 100
edamage = 15
randcoin = 10

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
                location = random.choice(LOCT)
                while location == "store":
                    print("As you walk down the path, you come across what appeared to be a rickety looking wagon with shuttered windows.")
                    while location == "store":
                        opt = input("Do you want to Enter store, Continue down path, or Check your stats?\n").lower()
                        if "stat" in opt or "check" in opt:
                            checkstats()
                        elif "continue" in opt or "path" in opt:
                            print("You decide not to enter store you continue down the path")
                            break
                        elif "enter" in opt or "store" in opt:
                            sto = "yes"
                            print("\nAs you approached the Wagon the shutters suddenly flew open, causing you to jump back with a start, after letting your heartrate go \ndown for a moment you looked into the inky black window of the wagon & you saw what appeared to be the face of an old mam behind \na counter of sorts, after a moment or two he seemed to notice you & he said with a raspy voice 'oh, traveler, I hadn't noticed you \nthere, sorry' he said, giving you a toothy grin. Then he started speaking again & said 'I offer a wide range of wares & services \nthat you can purchase, if you have the coin of course' he paused for a moment, seemingly contemplating something & eventually said \n'but you may only pick one from three, I have other customers & they cannot go without supplies' he then placed three different items on the table")
                            one = random.randint(5,20)
                            two = random.randint(9,20)
                            three =  random.randint(9,20)
                            print(f"You look skinny, I can offer you an elixir of health, for {one} coins to put some meat on your bones\n")
                            print(f"That knife of yours looks rather dull, if you wish you may purchase a whetstone to sharpen it, but it is fragile & so will only work once. you can buy it for {two} coins.") 
                            print(f"Your clothes are ragged & while they will protect you from the elements they will offer little protection against other forces, i can offer you a patch for your garments for {three} coins.")
                            while sto == "yes":
                                if "continue" in abcd:
                                    break
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
                                    print("You give your regards as you exit the man's store.")
                                    while "leave" in buy:
                                        abcd = input("Continue down path or Check stats?\n").lower()
                                        if "stat" in abcd or "check" in abcd:
                                            checkstats()
                                        elif "continue" in abcd or "path" in abcd:
                                            print("INSERT CONTINUE DOWN PATH TEXT HERE KIT\n")
                                            break
                                        else:
                                            print("You sit there, confused by choice.")
                                else:
                                    print("You stand there, confused by choice.")
                            break
                        else:
                            ("You sit there, confused by choice.")
                    break
                while location == "item":
                    #item stuff
                    print(f"As you walk down the path you notice something peaking out from the {nam2}")
                    if "Pond" in nam2 or "River" in nam2:
                        while True:
                            print(f"You walk towards the {nam2}, noticing something inside of it. As you walk around the {nam2} you approach the said object and pick it up.")
                            itemblah = random.choice(ITE)
                            print(f"It's a {itemblah}, which would clearly would be better than whatever you have on your person now.")
                            if itemblah == "Shield":
                                itempick = input("The shield might up your defense, but it would make it harder to attack and lower your attack. \nDo you want to take it?\n")
                            if itemblah == "Weapon":
                                itempick == input("This weapon may give you a higher attack damage, but you'd have to be more free to move to do so, so you'd have to get rid of some of your protective gear. \nDo you want to take it?\n")
                            if "yes" in itempick or "yeah" in itempick or "ok" in itempick:
                                if itemblah == "Shield":
                                    defense += random.randint(2-5)
                                    attack -= random.randint(2-5)
                                    print("higher def lower atk")
                                if itemblah == "Weapon":
                                    attack += random.randint(2-5)
                                    defense -= random.randint(2-5)
                                    print("lower def higher atk")
                                break
                            if "no" in itempick or "not" in itempick:
                                print("placehodler")
                                break
                            else:
                                "You sit there, confused by choice."
                    if "Statue" in nam2 or "Grave" in nam2:
                        while True:
                            print(f"You walk towards the {nam2}, noticing something behind it. As you walk around the {nam2} you approach the said object and pick it up.")
                            itemblah = random.choice(ITE)
                            print(f"It's a {itemblah}, which would clearly would be better than whatever you have on your person now.")
                            if itemblah == "Shield":
                                itempick = input("The shield might up your defense, but it would make it harder to attack and lower your attack. \nDo you want to take it?\n")
                            if itemblah == "Weapon":
                                itempick == input("This weapon may give you a higher attack damage, but you'd have to be more free to move to do so, so you'd have to get rid of some of your protective gear. \nDo you want to take it?\n")
                            if "yes" in itempick or "yeah" in itempick or "ok" in itempick:
                                if itemblah == "Shield":
                                    defense += random.randint(2-5)
                                    attack -= random.randint(2-5)
                                    print("higher def lower atk")
                                if itemblah == "Weapon":
                                    attack += random.randint(2-5)
                                    defense -= random.randint(2-5)
                                    print("lower def higher atk")
                                break
                            if "no" in itempick or "not" in itempick:
                                print("placehodler")
                                break
                            else:
                                "You sit there, confused by choice."
                    if "Forest" in nam2 or "Flowerbed" in nam2 or "Cave" in nam2:
                        while True:
                            print(f"You walk towards the {nam2}, noticing something inside. As you enter the {nam2} you approach the said object and pick it up.")
                            itemblah = random.choice(ITE)
                            print(f"It's a {itemblah}, which would clearly would be better than whatever you have on your person now.")
                            if itemblah == "Shield":
                                itempick = input("The shield might up your defense, but it would make it harder to attack and lower your attack. \nDo you want to take it?\n")
                            if itemblah == "Weapon":
                                itempick == input("This weapon may give you a higher attack damage, but you'd have to be more free to move to do so, so you'd have to get rid of some of your protective gear. \nDo you want to take it?\n")
                            if "yes" in itempick or "yeah" in itempick or "ok" in itempick:
                                if itemblah == "Shield":
                                    defense += random.randint(2-5)
                                    attack -= random.randint(2-5)
                                    print("higher def lower atk")
                                if itemblah == "Weapon":
                                    attack += random.randint(2-5)
                                    defense -= random.randint(2-5)
                                    print("lower def higher atk")
                                break
                            if "no" in itempick or "not" in itempick:
                                print("placehodler")
                                break
                            else:
                                "You sit there, confused by choice."
                    input("It is time to move forward.\n")
                    break
                encon -= 1

                #Enemy 
                echo = random.choice(ENE)
                if echo == "Bat":
                    ehealth = random.randint(15,25)
                    edamage = random.randint(10,15)
                    randcoin = random.randint(5,10)
                if echo == "Chamois":
                    ehealth = random.randint(35,45)
                    edamage = random.randint(15,20)
                    randcoin = random.randint(7,15)
                if echo == "Lynx":
                    ehealth = random.randint(55,65)
                    edamage = random.randint(20,25)
                    randcoin = random.randint(10,20)
                if echo == "Wolf":
                    ehealth = random.randint(75,85)
                    edamage = random.randint(20,30)
                    randcoin = random.randint(18,25)
                print(f"As you walk there appeasrs {random.choice(DES)} looking {echo}.")
                turn = random.randint(1,4)
                print(f"You look at the {echo}, it clearly isn't happy to see you.")
                while True:
                    print(f"As you walk there appears {random.choice(DES)} looking {echo}.")
                    while "Bat" in echo:
                        ehealth = random.randint(20,30)
                        turn = random.randint(1,4)
                        if turn >= 2:    
                            print("It stares at you, you stare back.")
                            aorr = input("Should you make an Attack or Run away?\n").lower()
                            if "run" in aorr:
                                print("You attempt to run away.")
                                running = random.randint(1,10)
                                if running == 1:
                                    print("You succesfully run PLACEHOLDER")
                                    break
                                if running >= 2:
                                    turn = 1
                            elif "attack" in aorr:
                                pdamage = random.randint(attack-2,attack+5)
                                print(f"You attack the {echo}, dealing {pdamage} damage.\n")
                                ehealth -= pdamage
                                if ehealth <= 0:
                                    break
                                turn = 1
                            elif "check" in aorr:
                                checkstats()
                            else:
                                print(f"You take too long to decide and the {echo} decides to ambush you.")
                                turn = 1
                        elif turn == 1:
                            print(f"The {echo} lunges at you, your health lowers by {edamage}\n")
                            health -= random.randint(edamage-2,edamage+2)
                            if health <= 0:
                                endingdie()
                                while True:
                                    dead = "dead"
                            turn = 2
                    print(f"PLACEHOLDER you defeat the enemy. You collect {randcoin} coins")
                    encon -= 1

            #BOSSFIGHT HERE
            print("You had a sense that you were nearing the edge of the forest, & after walking forward for a few more minutes you saw a plume of smoke coming over the treeline, you quickly ran towards it & saw a log cabin with a disheveled looking man in front of it sharpening his knife. As he saw you approach he said 'ah, traveler, you finally found this place' he stood up from his chair & brandished his knife at you as you realised that he wasn't going to be helful towards you drew your knife & steeled your nerves, preparing for combat")
            while boss == True:
                bhealth=100
                print("you noticed that the man appeared to stop for a moment as he daubed a strange fluid on his blade")
                while bhealth>0:
                    if poison==True:
                        health-=5
                        print("you feel the poison coursing through your veins & take 5 damage as a result of this")
                        print(f"your health is currently {health}")
                    print(f"your health is currently {health}")
                    aod=input("would you like to attack him, or defend yourself").lower()
                    if "attack" in aod and turn1==True:
                        print("you took the opportunity to try & stab him in the gut")
                        atkq=random.randint(1,2)
                        if atkq==1:
                                bdam=random.randint(attack-5,attack+5)
                                print(f"you managed to slice a wide gash in his stomach, dealing {bdam} damage")
                                print("after you attacked him he leaped back & started approaching for an attack")
                                bayq=random.randint(1,5)
                                if bayq==1:
                                    print("he managed to make a long cut along your right arm, you feel immense pain as you realised the fluid his blade was coated in ")
                        if atkq==2:
                            print("you lunged towards him to try & attack, but he dodged to the side & tried to stab you with his knife")
                            bayq=random.randint(1,3)
                            if bayq==1:
                                pdam=random.randint(health-5%-5,health-5%+5)
                                print(f"he managed to stab his knife right into your back, dealing {pdam} damage")
                                nhitless=1
                                poison=True
                        elif bayq!=1:
                            print("he lunged towards you, raising his arms up to stab you as hard as he could, but missed & tumbled across the ground")
                    elif "defend" in aod:
                        print("you tried to grab a log off the ground & shield yourself with it")
                        bayq=random.randint(1,8)


                    
            #BOSSFIGHT END
            #END OF GAME
   

