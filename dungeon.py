import random
import sys

player_name = input("What is your name punk bitch? ")
health: int = 100
gold:int = 50
inventory: list = ["sword"]
active_effects: list =[]

def main():
    global health
    print(f"Dungeon of Syntax \n Welcome {player_name}!")
    while health > 0:
        event = random.choice(["monster", "chest", "nothing"])
        if event == "monster":
            battle_monster()
        elif event == "chest":
            open_chest()
        else:
            print("Room is empty")

        display_status()

        choice = input("Next action(Continue/Use item/ Quit): ").lower()
        if choice == "use item":
            use_item()
        elif choice == "quit":
            print("You leave the dungeon with your loot.")
            break
        elif choice == "continue":
            print("You are daring to dive into deeper waters, eh? nice!")
            continue
        else:
            print("Invalid choice, try again")

def display_status():
    print(f"Status - Health: {health}, Gold: {gold}")
    print(f"Inventory: {inventory}")
    print(f"Active Effects: {active_effects}\n")

def battle_monster():
    global health, gold, active_effects
    monster_health = random.randint(20,40)
    print(f"There is a monster with {monster_health}")                                                                                                                                                                                                                                      
    while monster_health > 0 and health > 0:
        prompt = input("Attack or Run?: ").lower()
        if prompt == "attack":
            damage = random.randint(5, 15)
            if "amulet" in active_effects:
                damage += 5
                active_effects.remove("amulet")
           
            monster_health -= damage
            print(f"Damage done: {damage}; Monster health: {monster_health}")

            if monster_health > 0:
                monster_damage = random.randint(5, 12)
                if "shield" in active_effects:
                    monster_damage //=2
                    active_effects.remove("shield")
               
                health -= monster_damage
                print(f"Monster destroys you by {monster_damage}; Your health: {health}")
        
        elif prompt == "run":
            print("You escaped the battle!")
            return
       
        else:
            print("Invalid action")
    
    if health <= 0:
        sys.exit("You Suck! Game Over")
   
    else:
        reward = random.randint(10, 30)
        gold += reward
        print(f"Monster defeated, Victory to you! You earn {reward} gold")

def open_chest():
    global inventory
    reward = random.choice(["potion", "shield", "amulet"])
    inventory.append(reward)
    print(f"You have found a chest containing a {reward}")

def use_item():
    global health, inventory, active_effects
    if not inventory:
        print("No items")
    else:
        item = input("Enter item: ").lower()
        if item not in inventory:
            sys.exit("Item not foundin inventory")
        
        if item == "potion":
            health += 20
            inventory.remove("potion")
        elif item in ["shield", "amulet"]:
            active_effects.append(item)
            inventory.remove(item)
            print(f"{item.capitalize()} effect activated")

if __name__ == "__main__":
    main()
