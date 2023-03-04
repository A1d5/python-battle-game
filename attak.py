import os
from pickle import TRUE
import random
import time


race_list= ["human", "elf", "drawf", "ork"]
monster_list= ["goblin", "skelinton"]
boss_list= ["dragon"]
weapon_list= ["sword", "axe", "stick","mace","spear"]


def game_over():
    print("game over")

    con= input("do you want to continue: (y/n)?")
    if con == str(1) or con == "Y" or con == "y" or con == "yes" or con == "Yes" or con== "YES":
        os.system("clear")
        menu()
    elif con == "2" or con== "n" or con == "N" or con == "no" or con== "No" or con== "NO":
        exit()

def battle():
    #stats
    race= random.choice(race_list)
    weapon= random.choice(weapon_list)
    monster= random.choice(monster_list)
    boss= random.choice(boss_list)
    monster_weapon= random.choice(weapon_list)
    monster_level= random.randint(1,3)
    monster_exp= random.randint(0, 10)
    monster_gold= random.randint(0,5)
    gold= 0
    exp= 0
    next_exp= 100
    next_level= 1
    level= 0

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
        dmg= random.randint(1,3)
    elif weapon== "axe":
        dmg= random.randint(3,5)
    elif weapon == "stick":
        dmg= random.randint(1,2)
    elif weapon== "spear":
        dmg= random.randint(1, 5)
    elif weapon== "mace":
        dmg= random.randint(2,4)


    if monster == "goblin":
        monster_hp= random.randint(3, 5)
    elif monster== "skelinton":
        monster_hp= random.randint(5, 10)
    elif monster== "dragon":
        monster_hp= random.randint(50,100)
        monster_weapon= "claws"
        monster_dmg= random.randint(3, 10) 

    if monster_weapon== "sword":
        monster_dmg= random.randint(1,3)
    elif monster_weapon== "axe":
        monster_dmg= random.randint(3,5)
    elif monster_weapon == "stick":
        monster_dmg= random.randint(1,2)
    elif monster_weapon== "spear":
        monster_dmg= random.randint(1, 5)
    elif monster_weapon== "mace":
        monster_dmg= random.randint(2,4)


    

    print("battle!")
    time.sleep(1)
    os.system("clear")

    while TRUE:
        time.sleep(2)
        os.system("clear")
        print("your turn!")
        print("=================================")
        print("race: " + str(race) + "\nhp: " + str(hp) + "\nweapon:"  + str(weapon) + "\nlevel: " + str(level) + "\ngold: " + str(gold) + "\n exp: "  + str(exp) + "\n\nmonster: " + str(monster) +  "\nmonster hp:" + str(monster_hp) + "\nmonster weapon: " + str(monster_weapon) + "\nmonster level: " + str(monster_level))
        print("=================================")

        turn= input("1.attak\n 2.run\n")
        if turn == str(1) or turn == "attak":
            print("you attaked")
            time.sleep(2)
            monster_hp= monster_hp - dmg
            #if monster_hp < 0:
                #monster_hp= 0
            
            print("you did dmg " + str(dmg) + " dmg")
            print("the monster has " + str(monster_hp) + " hp left")
            if monster_hp <= 0:
                print("you killed the monster")
                time.sleep(1)
                exp= exp + monster_exp
                gold= gold + monster_gold
                print("you earned: " + str(exp) + " exp and: " + str(gold) + " gold")
                monster= random.choice(monster_list)
                monster_weapon= random.choice(weapon_list)
            if monster == "goblin":
                monster_hp= random.randint(3, 5)
            elif monster== "skelinton":
                monster_hp= random.randint(5, 10)
            elif monster== "dragon":
                monster_hp= random.randint(50,100)
                monster_weapon= "claws"
                monster_dmg= random.randint(3, 10) 
                time.sleep(2)
            if exp== next_exp:
                next_exp= next_exp + 100
                next_level= next_level + 1
                print("you leveled up!")
                max_hp +=1
                hp = max_hp
                level +=1
                print("max hp +1")
                                
                #break
        elif turn== str(2)or turn == "run":
            print("you ran away")
            time.sleep(2)
            print("game over")

            con= input("do you want to continue: (y/n)?")
            if con == str(1) or con == "Y" or con == "y" or con == "yes" or con == "Yes" or con== "YES":
                os.system("clear")
                menu()
            elif con == "2" or con== "n" or con == "N" or con == "no" or con== "No" or con== "NO":
                exit()

        time.sleep(1)
        os.system("clear")
        print("there turn!")
        print("=================================")
        print("race: " + str(race) + "\nhp: " + str(hp) + "\nweapon:"  + str(weapon) + "\nlevel: " + str(level) + "\ngold: " + str(gold) + "\nexp: " + str(exp) + "\n\nmonster: " + str(monster) +  "\nmonster hp:" + str(monster_hp) + "\nmonster weapon: " + str(monster_weapon) + "\nmonster level: " + str(monster_level))
        print("=================================")
        time.sleep(2)
        print("the " + str(monster) + " attaked:")
        time.sleep(2)
        hp= hp - monster_dmg
        if hp < 0:
            hp= 0
        print("the " + str(monster) + " did " + str(monster_dmg) + " dmg")
        print("you have: " + str(hp) + " hp left")

        if hp == 0:
            game_over()
            break
            

    #menu
def menu():
    os.system("clear")
    print("battle test")
    choice= input("1.start:\n\n2.leave\n")
    if choice== str(1) or choice== "start":
        battle()
    elif choice == 2 or choice == "leave":
        exit()



menu()

#bugs: 
#the monsters hp dosnt update when it goes to 0
#the monsters weapon dosnt change sometimes
#the hp of monsters resets to its original hp

#updates: 
#-added 2 new weapons, mace and spear- 04/03/23
#-made goblin and skelinton hp random numbers- 04/03/23