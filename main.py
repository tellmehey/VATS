import random
import os
import time

gameState = ""
health = 100.0
concentration = 100
cooldowns = 1
eHealth = 0
eAttack = 0
eSkill = 0
eBerzerk = 0
eBerzerking = False

def clears():
    os.system('cls' if os.name == 'nt' else 'clear')
def wait(s):
    time.sleep(s*cooldowns)

def AttackPlayer(dmg):
    global health
    health -= dmg * ArmorRate * Resistance
def AttackEnemy(dmg, area):
    global eHealth, eSkill
    if area == "head":
        eHealth -= dmg * 3
    elif area == "body":
        eHealth -= dmg
    elif area == "arms":
        eHealth -= dmg
        eSkill -= random.randint(1, 7) + dmg / 2

def enemyInit(lvl, skill):
    global eHealth, eAttack, eBerzerk, eBerzerking, eSkill
    eHealth = 75 + ((lvl - 1) * 5)
    eSkill = skill
    eAttack = 5 + 2 * skill
    eBerzerk = 0
    eBerzerking = False

def enemyThink():
    global eHealth, eAttack, eBerzerk, eBerzerking, eSkill
    if eHealth <= 20: # instant berzerk
        eBerzerking = True
    elif eBerzerk >= 100:
        eBerzerking = True

    if eBerzerking: # attack
        AttackPlayer(eAttack * 1.5)
    elif random.randint(1, 100) <= eSkill: # is it skilled enough to attack again?
        AttackPlayer(eAttack)

gameState = input("Start vats? (y/n/m/x):\n> ")
if gameState == "m":
    cooldowns = 0
    gameState = "in"
elif gameState == "x":
    gameState = "out"
elif gameState == "y":
    gameState = "in"

while gameState != "out":
    while gameState == "in":
        print(f"Health: {health}  Concentration: {concentration}")
        action = input("1. Attack\n2. Heal\n3. Reload\n4. Exit\n > ")
        if action == "1":
            pass
        elif action == "2":
            pass
        elif action == "3":
            pass
        elif action == "4":
            gameState = "out"
            print("come back again...")
        print("NEW TURN")
        wait(1)
        clears()