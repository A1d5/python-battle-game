import os
from pickle import TRUE
import random
import time


race_list= ["human", "elf", "drawf", "ork"]
monster_list= ["goblin", "skelinton",  "zombie", "vampire"]
boss_list= ["dragon", "hydra", "kraken", "cerberus", "deamon lord", "giant spider", "giant", "cyclops", "troll" ]
weapon_list= ["sword", "axe", "stick", "mace", "spear", "club", "dagger", "whip", "flail", "fists"]
armour_list= ["leather", "chain","metal", "plate"]



def scores(user, score):
    

    with open("scores.txt", "a") as f:
        f.write(f"user: {user} score: {score}\n")
        print("your score was: " + str(score))

    with open("scores.txt", "r") as f:
        for line in f:
            print(line.strip())
            
            

def game_over(user, score):
    print("game over")
    scores(user, score)

    con= input("do you want to continue: (y/n)?")
    if con == str(1) or con == "Y" or con == "y" or con == "yes" or con == "Yes" or con== "YES":
        os.system("clear")
        menu()
    elif con == "2" or con== "n" or con == "N" or con == "no" or con== "No" or con== "NO":
        exit()


def battle(user):
    #stats
    race= random.choice(race_list)
    weapon= random.choice(weapon_list)
    monster= random.choice(monster_list)
    monster_weapon= random.choice(weapon_list)
    monster_level= random.randint(1,3)
    monster_exp= random.randint(1, 10)
    monster_gold= random.randint(0,5)
    gold= 0
    exp= 0
    next_exp= 100
    next_level= 1
    level= 0

    score= 0
    attak_time= 0
    

    

    if race == "human":
        hp= 5
        max_hp= 5
    elif race == "elf":
        hp = 3
        max_hp= 3
    elif race == "drawf":
        hp = 7
        max_hp= 7
    elif race == "ork":
        hp= 9
        max_hp= 9
    


    if weapon== "sword":
        dmg= random.randint(1,5)
    elif weapon== "axe":
        dmg= random.randint(3,9)
    elif weapon == "stick":
        dmg= random.randint(1,2)
    elif weapon== "spear":
        dmg= random.randint(1,5)
    elif weapon== "mace":
        dmg= random.randint(2,6)
    elif weapon== "club":
        dmg= random.randint(1,3)
    elif weapon== "dagger":
        dmg= random.randint(1,3)
    elif weapon== "whip":
        dmg= random.randint(1,7)
    elif weapon== "flail":
        dmg= random.randint(1,5)
    elif weapon== "fists":
        dmg= random.randint(1,3)

    



    if monster == "goblin":
        monster_hp= random.randint(3, 5)
    elif monster== "skelinton":
        monster_hp= random.randint(5,10)
    elif monster== "zombie":
        monster_hp= random.randint(5,10)
    elif monster== "vampire":
        monster_hp= random.randint(5, 10)

    if monster_weapon== "sword":
        monster_dmg= random.randint(1,5)
    elif monster_weapon== "axe":
        monster_dmg= random.randint(3,9)
    elif monster_weapon == "stick":
        monster_dmg= random.randint(1,2)
    elif monster_weapon== "spear":
        monster_dmg= random.randint(1,5)
    elif monster_weapon== "mace":
        monster_dmg= random.randint(2,6)
    elif monster_weapon== "club":
        monster_dmg= random.randint(1,3)
    elif monster_weapon== "dagger":
        monster_dmg= random.randint(1,3)
    elif monster_weapon== "whip":
        monster_dmg= random.randint(1,7)
    elif monster_weapon== "flail":
        monster_dmg= random.randint(1,5)
    elif monster_weapon== "fists":
        monster_dmg= random.randint(1,3)
        monster_weapon= "fists"



                
    print("battle!")
    time.sleep(1)
    os.system("clear")

    while TRUE:
        time.sleep(2)
        os.system("clear")
        print("your turn!")
        print("=================================")
        print("race: " + str(race) + "\nhp: " + str(hp) + "/" + str(max_hp) + "\nweapon:"  + str(weapon) + "\nlevel: " + str(level) + "\ngold: " + str(gold) + "\nexp: "  + str(exp) + "\n\nmonster: " + str(monster) +  "\nmonster hp:" + str(monster_hp) + "\nmonster weapon: " + str(monster_weapon) + "\nmonster level: " + str(monster_level))
        print("=================================")

        turn= input("1.attak\n2.run\n")
        if turn == str(1) or turn == "attak":
            print("you attaked")
            attak_time +=1
            #print(str(attak_time))
            
            if attak_time >= 2:
                print("you need to wait before you attak")
            else:
                time.sleep(2)
                monster_hp= monster_hp - dmg
            #if monster_hp < 0:
                #monster_hp= 0
            
                print("you did dmg " + str(dmg) + " dmg")
                print("the " + str(monster) + " has " + str(monster_hp) + " hp left")
                

            
            if monster_hp <= 0:
                print("you killed the " + str(monster))
                time.sleep(1)
                exp= exp + monster_exp
                gold= gold + monster_gold
                score +=1
                print("you earned: " + str(exp) + " exp and: " + str(gold) + " gold")
                monster= random.choice(monster_list)
                monster_weapon= random.choice(weapon_list)
                if monster == "goblin":
                    monster_hp= random.randint(3, 5)
                elif monster== "skelinton":
                    monster_hp= random.randint(5,10)
                elif monster== "zombie":
                    monster_hp= random.randint(5,10)
                elif monster== "vampire":
                    monster_hp= random.randint(5, 10)
                
                choice= input("1. continue\n2. heal\n")#3.shop\n\n")
                if choice== str(1) or choice== "continue":
                    attak_time-= 1
                    continue
                elif choice== str(2) or choice== "heal":
                    print("your hp: " + str(hp) + "/ " + str(max_hp) + "\n\ngold: " + str(gold))
                    health= input("do you want to heal? Y/N")
                    if health== str(1) or health== "Y" or health== "y" or health== "Yes" or health== "yes" or health== "YES":
                        if gold <= 0:
                            print("your dont have enough gold!")
                            continue

                        if hp== max_hp:
                            print("you have enough hp!")
                            continue  
                        else:
                            gold -=1
                            hp +=1
                            print("your hp has been recoverd")
                            print("your hp: " + str(hp) + "/ " + str(max_hp) + "\n\ngold: " + str(gold))
                            time.sleep(2)
                            os.system("clear")
                    elif health== str(2) or health== "n" or health== "N" or health== "no" or health== "No" or health== "NO":
                        attak_time -=1
                        continue
                """elif choice== str(3) or choice== "shop":
                    print("shop!!")
                    os.system("clear")

                    print("what do you want to buy?")

                    for i in range(10):
                        item = random.choice(weapon_list)
                        price = random.randint(1,10)
                        print(f"{i+1}: {item} price: {price}")"""

                    

                    



                   
        

                    

            if level % 5:
                monster= random.choice(boss_list)
                if monster == "dragon":
                    monster_hp= random.randint(50,100)
                    monster_weapon= "claws"
                    monster_dmg= random.randint(3,10)
                    monster_exp= random.randint(50,100)
                    monster_gold= random.randint(10,50)
                elif monster== "hydra":
                    monster_hp= random.randint(50,150)
                    monster_weapon= "claws"
                    monster_dmg= random.randint(6,20)
                    monster_exp= random.randint(50,100)
                    monster_gold= random.randint(10,50)
                elif monster== "kraken":
                    monster_hp= random.randint(50,200)
                    monster_weapon= "tenticals"
                    monster_dmg= random.randint(3,40)
                    monster_exp= random.randint(50,200)
                    monster_gold= random.randint(10,100)
                elif monster== "cerberus":
                    monster_hp= random.randint(50,250)
                    monster_weapon= "bite"
                    monster_dmg= random.randint(3,70)
                    monster_exp= random.randint(50,200)
                    monster_gold= random.randint(10,100)
                    monster_dmg= random.randint(1,50)

                elif monster== "deamon lord":
                    monster_hp= random.randint(50,300)
                    monster_weapon= "deamon staff"
                    monster_dmg= random.randint(9,80)
                    monster_exp= random.randint(50,500)
                    monster_gold= random.randint(10,150)

                elif monster== "giant spider":
                    monster_hp= random.randint(50,350)
                    monster_weapon= "fangs"
                    monster_dmg= random.randint(3,100)
                    monster_exp= random.randint(50,250)
                    monster_gold= random.randint(10,150)

                elif monster== "giant":
                    monster_hp= random.randint(50,100)
                    monster_weapon= "feet"
                    monster_dmg= random.randint(3,100)
                    monster_exp= random.randint(50,150)
                    monster_gold= random.randint(10,100)
                elif monster== "cyclops":
                    monster_hp= random.randint(50,150)
                    monster_weapon= "feet"
                    monster_dmg= random.randint(6,100)
                    monster_exp= random.randint(50,200)
                    monster_gold= random.randint(10,150)
                elif monster== "troll":
                    monster_hp= random.randint(50,150)
                    monster_weapon= "claws"
                    monster_dmg= random.randint(3,100)
                    monster_exp= random.randint(50,150)
                    monster_gold= random.randint(10,100)
                    
        time.sleep(2)

        if exp== next_exp:
            next_exp= next_exp + 100
            next_level= next_level + 1
            score +=1
            print("you leveled up!")
            max_hp +=1
            hp = max_hp
            level +=1
            print("max hp +1")
                             
                #break
        elif turn== str(2)or turn == "run":
            print("you ran away")
            time.sleep(2)
            game_over(user, score)
            break
            

        time.sleep(1)
        os.system("clear")
        print("there turn!")
        print("=================================")
        print("race: " + str(race) + "\nhp: " + str(hp) + "/" + str(max_hp) + "\nweapon:"  + str(weapon) + "\nlevel: " + str(level) + "\ngold: " + str(gold) + "\nexp: " + str(exp) + "\n\nmonster: " + str(monster) +  "\nmonster hp:" + str(monster_hp) + "\nmonster weapon: " + str(monster_weapon) + "\nmonster level: " + str(monster_level))
        print("=================================")
        time.sleep(2)
        print("the " + str(monster) + " attaked:")
        time.sleep(2)
        hp= hp - monster_dmg
        if hp < 0:
            hp= 0
        print("the " + str(monster) + " did " + str(monster_dmg) + " dmg")
        print("you have: " + str(hp) + " hp left")
        attak_time -=1

        if hp == 0:
            game_over(user, score)
            break
            


def name():
    user= input("what is your name:\n")
    battle(user)

    #menu
def menu():
    os.system("clear")
    print("battle test")
    choice= input("1.start:\n\n2.leave\n")
    if choice== str(1) or choice== "start":
        name()
    elif choice == 2 or choice == "leave":
        exit()



menu()

#bugs: 
#the monsters hp dosnt update when it goes to 0- fixed 22/03/23
#you can spam the attak or just spam 1

#updates: 
#-added 2 new weapons, mace and spear- 04/03/23
#-made goblin and skelinton hp random numbers- 04/03/23
#-added 5 new weapons: club, dagger, whip, flail andf ists
#-added new monster: zombie- 04/03/23
#-added bosses -dragon now a boss- bosses: dragon, hydra, kraken, cerberus, deamon lord, giant spider, giant, cyclops and troll- 04/03/23
#-added heal system- 07/03/23
#-added new monster-vampire- 22/03/23
#-added score system- 22/03/23
#-increed dmg of weapons- 22/03/23




#todo:
#level system with bosses- done
#implement bosses- done
#iventory system
#shop/upgrade system
#armour system
#armour protection, strength and deffence
#enchants- random weapons/armour enchant chance