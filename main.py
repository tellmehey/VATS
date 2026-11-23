import random
import os
import time

gameState = ""
health = 100
concentration = 100
cooldowns = 1

def clears():
    os.system('cls' if os.name == 'nt' else 'clear')
def wait(s):
    time.sleep(s*cooldowns)

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