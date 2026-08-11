import random
import time

print("================================")
print("          DARK QUEST")
print("================================")
print("1. Start Game")
print("2. Inventory")
print("3. Search for Treasure")
print("4. Exit")
print("================================")

choice = input("Choose: ")

match choice:

    case "1":
        print("\nStarting game...")
        time.sleep(1)

        enemy = random.choice([
            "Goblin",
            "Wolf",
            "Skeleton",
            "Dark Knight"
        ])

        print(f"A {enemy} appeared!")

        action = input("Attack or Run? ").lower()

        match action:
            case "attack":
                damage = random.randint(10, 50)
                print(f"You dealt {damage} damage.")

            case "run":
                print("You escaped safely.")

            case _:
                print("Unknown action.")

    case "2":
        print("\nInventory")
        print("----------------")
        print("Sword")
        print("Shield")
        print("Health Potion")
        print("50 Gold")

    case "3":
        print("\nSearching...")
        time.sleep(2)

        gold = random.randint(1, 100)

        match gold:
            case x if x >= 80:
                print(f"You found a rare treasure: {gold} gold!")

            case x if x >= 40:
                print(f"You found {gold} gold.")

            case _:
                print("You found almost nothing.")

    case "4":
        print("\nGame closed.")

    case _:
        print("\nInvalid choice.")