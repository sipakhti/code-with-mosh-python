import random
from os import path
import pickle

from Classes.game import *




def input_name(players):
    length = 0
    for player in players:
        player_name = input("Enter Player name: ")
        player.name = player_name
        if len(player_name) > length:
            length = len(player_name)
    return length

def justify_player_name(players,length):
    for player in players:
        while len(player.name) < length:
            player.name += " "

def justify_enemy_name(*enemies):
    length = 0
    for enemy in enemies:
        if len(enemy.name) > length:
            length = len(enemy.name)
    for enemy in enemies:
        while len(enemy.name) < length:
            enemy.name += " "


    


# # Create Black Magic
# fire = Spell.from_string("Fire-10-100-black")
# thunder = Spell.from_string("Thunder-10-100-black")
# blizzard = Spell.from_string("Blizzard-10-100-black")
# meteor = Spell.from_string("Meteor-20-200-black")
# quake = Spell.from_string("Quake-14-140-black")

# # Create White Magic
# cure = Spell.from_string("Cure-12-120-white")
# cura = Spell.from_string("Cure-18-200-white")

# Create Some items
# potion = Item.from_string("Potion-potion-Heals 50 HP-50-2-70")
# hipotion = Item.from_string("HiPotion-potion-Heals 100 HP-100-1-110")
# superpotion = Item.from_string("SuperPotion-potion-Heals 500 HP-500-0-200")
# megapotion = Item.from_string(
#     "MegaPotion-potion-Heals entire party HP-9999-1-500")
# elixer = Item.from_string(
#     "Elixer-elixer-Fully Restores HP/MP of one party-9999-1-300")
# hielixer = Item.from_string(
#     "HiElixer-elixer-Fully Restores party's HP/MP-9999-2-600")

# grenade = Item.from_string("Grenade-attack-Deals 500 Damage-500-1-450")


# potion_s = Item.from_string("Potion-potion-Heals 50 HP-50-2-70", shop=True)
# hipotion_s = Item.from_string(
#     "HiPotion-potion-Heals 100 HP-100-1-110", shop=True)
# superpotion_s = Item.from_string(
#     "SuperPotion-potion-Heals 500 HP-500-0-200", shop=True)
# megapotion_s = Item.from_string(
#     "MegaPotion-potion-Heals entire party HP-9999-1-500", shop=True)
# elixer_s = Item.from_string(
#     "Elixer-elixer-Fully Restores HP/MP of one party-9999-1-300", shop=True)
# hielixer_s = Item.from_string(
#     "HiElixer-elixer-Fully Restores party's HP/MP-9999-2-600", shop=True)

# grenade_s = Item.from_string(
#     "Grenade-attack-Deals 500 Damage-500-1-450", shop=True)

# player_items = [potion, hipotion, superpotion,
#                 megapotion, elixer, hielixer, gr/enade]
# player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
# shop_items = [potion_s, hipotion_s, superpotion_s, megapotion_s,
#               elixer_s, hielixer_s, grenade_s]


data_files = {"user_data":"C:\\Users\\omers\\Desktop\\HelloWorld\\Projects\\Battle\\game_data.pkl",
                "player_items":"C:\\Users\\omers\\Desktop\\HelloWorld\\Projects\\Battle\\player_items.pkl",
                "spells":"C:\\Users\\omers\\Desktop\\HelloWorld\\Projects\\Battle\\spells.pkl",
                "shop_items":"C:\\Users\\omers\\Desktop\\HelloWorld\\Projects\\Battle\\shop_item.pkl"}


if path.exists(data_files["user_data"]):
    user_in = input("Save file found, Press enter to load from file to start new game press N: ")
    # Continue the game where it left off
    if user_in == "":
        with open(data_files["user_data"],"rb") as save_file:
            game_data = pickle.load(save_file)
            players = game_data[0] # load player data
            enemies = game_data[1] # load enemy data
    # start the game all over again
    else:
        while True:
            try:
                num_players = int(input("How many players wanna play: "))
                num_enemies = int(input("How many enemies do you want to fight with"))
            except ValueError:
                print("Invalid number!")
            else:
                break

        players = []  # Empty players list which will be populated with multiple player instances
        for num in range(num_players):
            players.append(Player("player",460,65,60,343))
    
        # input name and modify it for a cleaner and consistent formatting
        justify_player_name(players,input_name(players))

        # add items and magic for every player

        for player in players:
            player.load_items(data_files["player_items"])
            player.load_magic(data_files["spells"])

        enemies = []
        for num in range(num_enemies):
            enemies.append(Enemy(f"Enemy{num}",700,65,45,25))


    if bool(enemies) == False:
        enemy_count = players[0].level//5 + 1
        for num in range(enemy_count):
            enemies.append(Enemy(f"Enemy {num+1}",700,65,45,25))




# if no save_game is found
else:
    while True:
        try:
            num_players = int(input("How many players wanna play: "))
            num_enemies = int(input("How many enemies do you wanna fight with: "))
        except ValueError:
            print("Invalid number!")
        else:
            break

    players = []  # Empty players list which will be populated with multiple player instances
    for num in range(num_players):
        players.append(Player("player",460,65,60,34 ))
    
    # input name and modify it for a cleaner and consistent formatting
    justify_player_name(players,input_name(players))

    # add items and magic for every player
    for player in players:
        player.load_items(data_files["player_items"])
        player.load_magic(data_files["spells"])
        
        
    enemies = []
    for num in range(num_enemies):
        enemies.append(Enemy(f"Enemy {num+1}",700,65,45,25))

# instantiate Shop 
item_shop = Shop()
item_shop.load_shop_items(data_files["shop_items"]) # load shop items
 
# enemy = Person("Xerg", 1500, 65, 45, 25)

for enemy in enemies:
    enemy.load_items(data_files["player_items"])





running = True
defeated_enemies = []
print(Bcolors.FAIL + Bcolors.BOLD + "AN WILD TROLLINA APPEARS" + Bcolors.ENDC)

# Main program Block
while running:
    for player in players:
        player.get_player_stats()
    
    print("\n")
    for enemy in enemies:
        enemy.get_enemy_stats()
    #enemy2.get_enemy_stats()
    print("==================================")
  
    for player in players:
        player.choose_action()
        choice = input("Choose action: ")
        # TRY block so that wrong input leads to player attacking by default
        try:
            index = int(choice) - 1
            player.action[index]
        except (ValueError, IndexError):
            index = 0
        else:
            print(f"{player.name.strip()} chose {player.action[index]}!")


# IF player choose to attack
        if index == 0:
            target = random.choice(enemies)
            print("="*50)
            dmg = player.generate_damage(target)
            target.take_damage(dmg)
            print(f"{player.name.upper()} did {dmg} damage to the {target.name}.")

# IF player choose to use magic
        elif index == 1:
            print("="*50)
            player.choose_magic()
            print("Enter 0 if you want to go to the previous menu")

            while True:

                # TRY block to make sure that the user input is within range
                try:
                    magic_choice = int(input("Choose Magic: ")) - 1
                    if magic_choice == -1:
                        break
                    spell = player.magic[magic_choice]
                except (IndexError, ValueError):
                    print(
                        f"{Bcolors.WARNING}NO SUCH SPELL EXIST. SELECT THE CORRECT SPELL{Bcolors.ENDC}")
                else:
                    break
        # if the user wants to go back
            if magic_choice == -1:
                continue
    

            magic_damage = spell.generate_damage()
            current_mp = player.get_mp()

        # to make sure spell is only cast when their is enough mp
            if spell.cost > current_mp:
                print(Bcolors.FAIL, "\n not enough MP \n", Bcolors.ENDC)
                continue

            player.reduce_mp(magic_choice)
        # spells that attack (BLACK)
            if spell.typ.lower() == "black":
                target = random.choice(enemies)
                print(
                    f"{Bcolors.OKBLUE}{player.name} used {spell.name} dealing {magic_damage} damage to {target.name} {Bcolors.ENDC} ")
                target.take_damage(magic_damage)
                print(f"the player did {magic_damage} damage to the enemy.")

        # Spells that Heal (WHITE)
            elif spell.typ.lower() == "white":
                print(
                    f"{Bcolors.OKGREEN}{player.name} used {spell.name} which Heals {magic_damage} HP {Bcolors.ENDC} ")

                player.heal_hp(spell.dmg)
                print(f"YOUR HP: {player.get_hp()}")

# if player choose ITEM
        elif index == 2:
            print("="*50)
            player.choose_item()
            while True:

                try:
                    print("Enter 0 if you want to go to the previous menu")
                    item_choice = int(input("Choose Item: ")) - 1
                    item = player.items[item_choice]
                except (ValueError, IndexError):
                    print(f"{Bcolors.WARNING}Wrong Input!{Bcolors.ENDC}")
                else:
                    break

        # if the user wants to go back
            if item_choice == -1:
                continue

            item.reduce_quantity()
            print(f"{Bcolors.WARNING}{player.name} is using {item.name}...")
            print(f"{Bcolors.OKBLUE}{item.name} {item.description}{Bcolors.ENDC}")

            if item.typ == "potion":
                player.heal_hp(item.prop)

            elif item.typ == "elixer":
                if item.name == "HiElixer":
                    for player in players:
                        player.heal_hp(item.prop)
                        player.heal_mp(item.prop)
                player.heal_hp(item.prop)
                player.heal_mp(item.prop)

            elif item.typ == "attack":
                target = random.choice(enemies)
                target.take_damage(item.prop)


# ENEMY attacks

    # chooses a player randomly to attack
    
    for enemy in enemies:
        if bool(players) == False:
            break
        attack = True
        if enemy.hp/enemy.max_hp < 0.2:
            
            for item in enemy.items:
                if item.typ == "elixer"  and item.qty > 0:
                    enemy.heal_hp(item.prop)
                    item.qty -= 1
                    print("enemy used elixer..")
                    attack = False
                    break
        
        elif enemy.hp/enemy.max_hp < 0.6:
            for item in enemy.items:
                if item.typ == "potion" and item.qty > 0:
                    enemy.heal_hp(item.prop)
                    item.qty -= 1
                    print(f"{enemy.name} used {item.name} which HEALS for {item.prop}")
                    attack = False
                    break
           
        
        if attack:
            target = random.choice(players)
            enemy_dmg = enemy.generate_damage(target)
            target.take_damage(enemy_dmg)
            print(
                f"Enemy attacks {target.name} for {enemy_dmg} points")




# WIN

        # Removes the defeated enemy from the enemies list and add it to the deafeated enemies list
    for y in range(len(enemies)):
        try:
            if enemies[y].get_hp() == 0:
                print(f"\n{enemies[y].name} has been defeated!\n")
                defeated_enemies.append(enemies[y])
                enemies.pop(y)
        except IndexError:
            continue
        else:
            pass
        # if all the enemies are defeated
        if bool(enemies) == False:

            

            print(f"{Bcolors.OKGREEN} you win! {Bcolors.ENDC}")

            for player in players:
                player.money += 500
                print(f"{player.name.strip()} won 500 credits. You can buy various items with them\n")
                restart = input("Press Enter to advance to next level")

                enter_shop = input(
                    "Now you can buy items from the shop!!\n Press Y to enter and N to continue: ")

                if enter_shop.lower() == "y" or enter_shop == "":
                    while True:
                        item_shop.sell_items(player)

                        remain_in_shop = input(
                            "Press 'Q' to exit the shop.\nPress enter to continue shopping: ")
                        if remain_in_shop.lower() != "q":
                            continue
                        else:
                            break
                            print("*"*20)
                
            play_again = input("Press enter to continue else type Q to quit: ")
    
            if play_again.lower() == "q":
                for player in players:
                    player.reset_stats()
                    player.level_up()
                for enemy in enemies:
                    enemy.reset_stats()
                game_data = [players, enemies]
                # saving game_data in Pickle file
                print("Saving Progress...")
                with open(data_files["user_data"], "wb") as save_file:
                    pickle.dump(game_data, save_file, -1)
                running = False
                break
            elif play_again == "":
                for player in players:
                    player.level_up()
            
            for enemy in defeated_enemies:
                enemy.max_hp += int(players[0].hp)
                enemy.atk += 5 * players[0].level//2
                enemy.df += 5 * players[0].level//2
                enemy.reset_stats()
                enemies.append(enemy)
            defeated_enemies.clear()
            running = True
            game_data = [players,enemies]
            print("Saving Progress...")
            with open(data_files["user_data"],"wb") as save_file:
                pickle.dump(game_data,save_file,-1)
# LOSE
    
    if bool(players) == False:
        running = False
        print("All the players have been eliminated!")
        print("THE GAME IS CLOSING!!!")
    
    else:
        for x in range(len(players)):
            if players[x].hp == 0:
                print(f"{Bcolors.FAIL} {players[x].name} lost! {Bcolors.ENDC}")
                print(f"{players[x].name} has been eliminated")
                players.pop(x)
                break
                


