import sys
from sys import exit 
import random 

def dead():
    print("You have died... Exit the game")
  

def combat(health,score,weapons,monsters,current_weapon,current_monster):
    display_stats()
 
    player_turn = True
    Monster_turn = False
 
    while health >= 1 or current_monster[1] >= 1:
        move = ""
        monMove = ""
        
        if player_turn:
            if current_monster[1] <= 0:
                print("")
                print("You defeated the",current_monster[0])
                g = random.randint(10,50)
                score += g
                print("You got",g,"gold!")
                print("Gold:",score)
                print("")
                print("After your victory against the",current_monster[0]+", you decide to continue towards your previous direction.")
                break
            elif health <= 0:
                dead()
                break
            else:                
                print("")
                print("Your Turn:")
                print("[a] - Attack")
                print("[d] - Defend")
                move = input("> ")
                print("")
                if move == "a": 
  
                    current_monster[1] -= current_weapon[1] 
                    print("You Attacked the",current_monster[0]+".")
                    print("You dealt",current_weapon[1],"damage to the",current_monster[0]+".")
                    print(current_monster[0]+"'s Health:",current_monster[1])
                        
                elif move == "d":
                    print("You raise your",current_weapon[0],"in defence.")
                    
                player_turn = False
                monster_turn = True
            if monster_turn:
                if current_monster[1] <= 0:
                    print("You defeated the",current_monster[0])
                    print("")
                    g = random.randint(10,50)
                    score += g
                    print("You got",g,"gold!")
                    print("Gold:",score)                    
                    break
                elif health <= 0:
                    dead()
                    break
                else:                      
                    print("")
                    print("The",current_monster[0]+"'s Turn:") #does not display for some reason
                    if move != "d":
                            health -= current_monster[2]
                            print("The",current_monster[0],"attacks you!")
                            print("The",current_monster[0],"Dealt",current_monster[2],"damage to you.")
                            print("Your health:",health)
                            player_turn = True
                            monster_turn = False
                    elif move == "d":
                            if current_monster[2] > current_weapon[2]:
                                health -= current_monster[1] + current_weapon[2]
                                print("The",current_monster[0],"dealt",current_monster[1] - current_weapon[2],"damage to you.")
                                print("You blocked",current_weapon[2],"damage.")
                                print("Your health:",health)
                                player_turn = True
                                monster_turn = False    
                            elif current_monster[2] <= current_weapon[2]:
                                print("You Blocked the",current_monster[0]+"'s attack.")
                                print("Health:",health)
                                player_turn = True
                                monster_turn = False                                 
                        

def display_stats():
    print("<< Player >>") #create name system at beginning
    print("Health:",health)
    print("Weapon:",current_weapon[0])
    print("Attack:",weapons[1][1])
    print("Defence:",weapons[1][2])    
    print("")
    print("<<",current_monster[0],">>")
    print("Health:",current_monster[1])
    print("Attack:",current_monster[2])
    print("Defence:",current_monster[3])
   

health = 100
score = 0
weapons =[['fists',1,1],['stick',2,2],['knife',4,1]]
monsters = [["Imp",6,2,1],["Troll",50,5,2],["Ogre",10,8,1],[],[]]
current_weapon = weapons[0]
current_monster = monsters[0]

print("")
print(" ==============================================================================================================================")
print("")                                                                                                                                 
print("")                                                                                                                                
print(" 7MMF' 'YMM'   db                           7MM                                 .g8''8q.                                 mm")     
print("  MM   .M'                                   MM                               .dP'    `YM.                               MM")     
print("  MM .d'     `7MM  `7MMpMMMb.  .P'Ybmmm ,M''bMM  ,pW'Wq.`7MMpMMMb.pMMMb.      dM'      `MM `7MM  `7MM  .gP'Ya  ,pP'Ybd mmMMmm")   
print("  MMMMM.       MM    MM    MM :MI  I8 ,AP    MM 6W'   `Wb MM    MM    MM      MM        MM   MM    MM ,M'   Yb 8I   `''   MM")    
print("  MM  VMA      MM    MM    MM  WmmmP' 8MI    MM 8M     M8 MM    MM    MM      MM.      ,MP   MM    MM 8MOOOOOO/ `YMMMa.   MM")     
print("  MM   `MM.    MM    MM    MM 8M      `Mb    MM YA.   ,A9 MM    MM    MM      `Mb.    ,dP'   MM    MM YM.    , L.   I8   MM")     
print(" JMML.   MMb  JMML  JMML  JMML.YMMMMMb `Wbmd'MML.`Ybmd9'.JMML  JMML  JMML.      `'bmmd'     `Mbod'YML.`Mbmmd' M9mmmP'   `Mbmo")   
print("                             6'     dP                                             MMb")                                         
print("                             Ybmmmd'                                                `OOOO")                                     
print("")                                                                                                                               
print(" ===============================================================================================================================")
print("")
input("Press any key to continue >")
print("")
print("You are lost in a ancient forest. You remember something about finding a treasure but your memories prior to this moment seem foggy.")
print("The forest must be giving you amnesia. Everywhere you look seems to be the same and you don't feel in control as if youu are in a dream.")
print("You walk aimlessly along a path until something shiny catches your eye. It seems to be coming from inside a tree knot")
print("")
print("Would you like investigate? [y / n]")
yesno = input("> ")
while (yesno != "y" or yesno != "n"):
    if yesno == "y":
        g = random.randint(2,15)
        score += g
        print("")
        print("You walk over to the knot in the tree and pull out some shiny gold coins")
        print("You found" ,g, "gold")
        print("Gold:",score) 
        break
    elif yesno == "n":
        print("")
        print("You decide to leave the tree alone and continue wandering.")
        break
    else:
        yesno = input(">")
print("")
print("You walk along the path. Every direction you look, looks the same until you notice something lying on the path ahead")
print("You come across a medium-sized stick that is smooth to the touch and as straight as an arrow.")
print("Do you pick it up? [y / n]")
yesno = input("> ")
while (yesno != "y" or yesno != "n"):
    if yesno == "y":
        current_weapon = weapons[1]
        print("")
        print("You picked up the stick")
        print("")
        print("Weapon: Stick")
        print("Attack:",weapons[1][1])
        print("Defence:",weapons[1][2])
        break
    elif yesno == "n":
        print("")
        print("You decide to leave the stick where it is and continue walking.")
        break
    else:
        yesno = input("> ")
    
print("")
print("As you continue, you get a strange feeling as if something is watching you. You think nothing of it but a few moments later,")
print("You hear scurrying behind you and nervously walk faster down the path. Suddenly you hear ruslting in a bush to your left.")
print("what do you do?")
print("[1] check out the bush.")
print("[2] Run away as fast as you can.")
answer = input("> ")
while (answer != 1 or answer  != 2):
    if answer == "1":
        print("")
        print("You slowly walk over to the bushes with your",current_weapon[0],"raised.")
        print("You creep ever so closer to bush until something suddenly jumps out!")
        print("It's an angry", monsters[0][0]+". Get ready to fight...")# fix period with spaces on either side 
        current_monster = monsters[0]
        input("Press any key to continue > ")
        print("")
        combat(health,score,weapons,monsters,current_weapon,current_monster)
        break
    elif answer == "2":
        print("")
        print("You run passed the bush as fast as you can but you move so quickly that you don't pay attention to your footing")
        print("Your gets caught on a root and you fall")
        print("")
        g = random.randint(5,11)
        health -= g    
        print("you lost", g ,"health")
        print("Health:", health)
        break
    else:
        answer = input("> ")

print("")
print("You keep along the trail until you come across a rive with a rickety old bridge over it. It looks as if a strong breeze would collapse it.")
print("You notice that the stream under the bridge is about waist height but the water is moving very fast fast")
print("what do you do?")
print("[1] Go over the rickety bridge.")
print("[2] Go through the rushing river.")
answer = input("> ")

while answer != 1 or answer != 2:
    if answer == "1":
        print("")
        print("You decide to take your chances with the rickety bridge.")
        print("As you walk on each plank of wood, you hear a unsettling creaking noise.") 
        print("Half way across the bridge, you hear a booming voice coming from below")
        print("")
        print("  'Who's that trip trapping over my bridge!!' ")
        current_monster = monsters[1]
        print("")
        print("It's a",current_monster[0]+"!")
        print("")
        print("The Troll lumbers it's way onto the bridge. It speeks in a deep, baritone, voice.")
        print(" 'If you want to cross my bridge... You have to answer my riddle or else you are dead!' ")
        input("Press any key to continue >")
        print("")
        print(" 'Only one color, but not one size.'")
        print(" 'Stuck at the bottom, yet I easily fly.'") 
        print(" 'Present in sun, but not in rain.'")
        print(" 'Doing no harm, and feeling no pain.'") 
        print(" 'What Am I?'")
        riddle = input("Answer > ")
        if riddle == "shadow":
            print("")
            print(" 'Correct! Astounding! I will let you pass unharmed!")
            break
        else:
            print("")
            print(" 'Incorrect! Prepare to die fool!'") 
            print("Get ready to fight...")
            input("Press any key to continue > ")
            print("")
            combat(health,score,weapons,monsters,current_weapon,current_monster)
            break
                        
        
    elif answer == 2:
        print("You decide to cross the rushing river")
        print("You wade into the water slowly. It's freezing cold. As you creep further and further across the river, it gets deeper an deeper until you can barely touch.")
        print("You tip-tow through the water but you realize you have nowhere to step anymor. It has become too deep!")
        print("You frantically try to swim to the other side but the current sweeps you away...")
        dead()
        break
    else:
        answer = input("> ") 
    
    print("You made it across the bridge to the other side to find a stone tower")
    print("You climbed 1 000 of the towers steps top the very top to discover the treasure.")
    print("She has blue eyes and long blonde hair...")
    print("")
    print("YOU WIN!")
  
        

           
        
        
        
        
        
        








    
   
            