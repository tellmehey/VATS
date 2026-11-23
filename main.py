gameState = ""
health = 100
concentration = 100
gameState = input("Start vats? (y/n):\n> ")
if gameState == "y":
    gameState = "in"
    while gameState == "in":
        print(f"Health: {health}  Ammo: null  Concentration: {concentration}")
        action = input("1. Attack\n2. Heal\n3. Reload\n4. Exit\n > ")
        if action == "1":
            pass
        elif action == "2":
            pass
        elif action == "3":
            pass
        elif action == "4":
            gameState = "out"
        print("something now test ts")