from Classes.game import Bcolors
import random
from assorted import to_json
import json
from os import path
import pickle





class Person:

    def __init__(self, name, hp:int, mp:int, atk:int, df:int, magic=[], items=[], money=0, level=1:int):

        self.name = name
        self.max_hp = int(hp)
        self.hp = int(hp)
        self.max_mp = int(mp)
        self.mp = int(mp)
        self.atk = int(atk)
        self.atkl = self.atk - 10
        self.atkh = self.atk + 10
        self.df = int(df)
        self.magic = magic
        self.items = items
        self.money = int(money)
        self.level = int(level)
        self.action = ["Attack", "Magic", "Item"]

    # Alternate Contructor for Magic Property
    def mag_from_string(self, mag_string):
        """parses the string in which spells are seperated with a "-"
           and then passes the parsed string to the Spell class'
           alternate constructor and saves the object that is 
           instantiated in a list
        """

        self.magic.append(Spell.from_string(mag_string))

    def level_up(self):
        self.level += 1
        self.max_hp += int(self.max_hp * (self.level/200))
        self.max_mp += int(self.max_mp * (self.level/200))
        self.atk = int(self.atk * (1+self.level/50))
        self.df = int(self.df * (1+self.level/50))
        self.atkl = self.atk-10
        self.atkh = self.atk+10

        self.reset_stats()

    def reset_stats(self):
        self.hp = self.max_hp
        self.mp = self.max_mp
        self.atkl = self.atk-10
        self.atkh = self.atk+10

    def generate_damage(self, attackee):
        """ Generate random damage"""
        return random.randrange(int(self.atkl), int(self.atkh))

    def take_damage(self, dmg):
        """take damage"""
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

    def get_hp(self):
        """returns current HP"""
        return self.hp

    def get_max_hp(self):
        """returns maximum attainable HP"""
        return self.max_hp

    def heal_hp(self, amount):
        """heals HP for the amount provided. doesnt increase the HP above maximum HP"""
        if self.hp + amount > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += amount

    def heal_mp(self, amount):
        if self.mp + amount > self.max_mp:
            self.mp = self.max_mp
        else:
            self.mp += amount

    def elixer_boost(self):
        self.hp = self.max_hp
        self.mp = self.max_mp

    def get_mp(self):
        """Returns current MP"""
        return self.mp

    def get_max_mp(self):
        """Returns Maximum attainable MP"""
        return self.max_mp

    def reduce_mp(self, i):
        """Reduces MP when a spell is Cast
           Accepts index of the list in which magic spells are stored
        """
        self.mp -= self.magic[i].cost

    def choose_action(self):
        """prints on the screen the actions that a user can take"""
        i = 1
        print(Bcolors.OKBLUE, "Actions", Bcolors.ENDC)
        for item in self.action:
            print("    " + str(i) + ":", item)
            i += 1

    def choose_magic(self):
        """prints on the screen availible spells"""
        print("-"*50)
        print(Bcolors.OKGREEN, "Magic", Bcolors.ENDC)
        i = 1
        for spell in self.magic:
            # color codes the COST if MP is not sufficient
            if spell.cost > self.get_mp():
                x = Bcolors.FAIL
            else:
                x = Bcolors.OKGREEN
            print(
                f"    {i}: {spell.name} {x} (cost: {spell.cost}) {Bcolors.ENDC} (damage: {spell.dmg}) (Remaining : {self.mp//spell.cost})")
            i += 1

    def choose_item(self):
        """prints out the menu of items the player has.
            doesnt show the items with 0 quantity
        """
        i = 1
        print("-"*50)
        print(f"\r{Bcolors.OKGREEN}{Bcolors.BOLD}YOUR ITEMS {Bcolors.ENDC}")
        self.pop_items()
        for item in self.items:
            # changes color of the quantity if its low
            if item.qty == 1:
                x = Bcolors.WARNING
            else:
                x = Bcolors.OKGREEN
            # only prints out those items which the player has i.e those items whose qty is > 0
            if item.qty > 0:
                print(f"    {i}: {item.name} {x}(x{item.qty}){Bcolors.ENDC}")
                i += 1
            else:
                pass

    def pop_items(self):
        """moves the item with 0 quantity to the end of the list.
            support method for choose_item()
        """
        i = 0
        print(type(self.items))
        x = -1
        for index in range(len(self.items)):

            if self.items[index].qty < 1:
                # self.items.append(self.items[index])
                x = index
        if x != -1:
            self.items.pop(x)
        print(123456789)

    def compare_stats(self, other):
        """Compare stats of two instances of Player Class"""
        hp = self.hp > other.hp
        mp = self.mp > other.mp
        atk = self.atk > other.atk
        df = self.df > other.df
        lvl = self.level > other.level

        if hp == True:
            hp = Bcolors.OKGREEN + str(self.hp) + \
                "  >  " + str(other.hp) + Bcolors.ENDC
        elif hp == False:
            hp = Bcolors.FAIL + str(self.hp) + "  <  " + \
                str(other.hp) + Bcolors.ENDC

        if mp == True:
            mp = Bcolors.OKGREEN + str(self.mp) + \
                "  >  " + str(other.mp) + Bcolors.ENDC
        elif mp == False:
            mp = Bcolors.FAIL + str(self.mp) + "  <  " + \
                str(other.mp) + Bcolors.ENDC

        if atk == True:
            atk = Bcolors.OKGREEN + \
                str(self.atk) + "  >  " + str(other.atk) + Bcolors.ENDC
        elif atk == False:
            atk = Bcolors.FAIL + str(self.atk) + \
                "  <  " + str(other.atk) + Bcolors.ENDC

        if df == True:
            df = Bcolors.OKGREEN + str(self.df) + \
                "  >  " + str(other.df) + Bcolors.ENDC
        elif df == False:
            df = Bcolors.FAIL + str(self.df) + "  <  " + \
                str(other.df) + Bcolors.ENDC

        if self.level == other.level:
            lvl = str(self.level) + " == " + str(other.level)
        elif lvl == True:
            lvl = Bcolors.OKGREEN + \
                str(self.level) + "  >  " + str(other.level) + Bcolors.ENDC
        elif lvl == False:
            lvl = Bcolors.FAIL + str(self.level) + \
                "  <  " + str(other.level) + Bcolors.ENDC

        print(f"    {self.name}    {other.name}")
        print(f"HP: {hp}\nMP: {mp}\nATK: {atk}\nDEF: {df}\nLEVEL: {lvl}")

    def __str__(self):
        """Returns the breakdown of player stats,spells and inverntory"""

        magic = ""
        inventory = ""
        for spell in self.magic:
            magic += " " + spell.name
        for item in self.items:
            inventory += " " + item.name
        return f"HP:{self.hp}/{self.max_hp}\nMP:{self.mp}/{self.max_mp}\nATK:{self.atk}\nDEF:{self.df}\nLVL:{self.level}\nCREDITS:{self.money}\nMAGIC:{magic}\nINVERNTORY:{inventory}"

class Spell:

    # Constructor
    def __init__(self, name, cost, dmg, typ):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.typ = typ

    # Alternate Constructor
    @classmethod
    def from_string(cls, mag_string, seperator="-"):
        """takes a formated string where each property is separated by a "-"
            Correct format is: name-cost-dmg-type
        """
        name, cost, dmg, typ = mag_string.split(seperator)
        return cls(name, int(cost), int(dmg), typ)

    def generate_damage(self):
        """Generates random damage"""
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)

    def get_spell_name(self):
        return self.name

    def get_spell_cost(self):
        return self.cost

    def get_spell_type(self):
        return self.typ

    def __str__(self):
        return self.name

# INventory


class Item:

    def __init__(self, name, typ, description, prop: int, qty: int, price: int):
        self.name = name
        self.typ = typ
        self.description = description
        self.prop = int(prop)
        self.qty = int(qty)
        self.price = int(price)

    @classmethod
    def from_string(cls, item_string, seperator="-", shop=False):
        """parses string seperated by a custom seperator into individual
           attributes.
           By default the "-" is the seperator
        """
        name, typ, description, prop, qty, price = item_string.split(seperator)
        return cls(name, typ, description, prop, qty, price) if shop == False else cls(name, typ, description, prop, 99, price)

    def reduce_quantity(self):
        self.qty -= 1

    def to_tuple(self):
        return self.name, self.typ, self.description, self.prop, self.qty, self.price


class Shop:

    def __init__(self, items=[]):
        self.items = items

    def sell_items(self, player):
        print("*"*20)
        print(Bcolors.BOLD, "The shop is selling:", Bcolors.ENDC)
        print("~"*50)
        i = 1
        for item in self.items:
            if item.price > player.money:
                x = Bcolors.FAIL
            else:
                x = Bcolors.OKGREEN

            print(
                f"{i}: {item.name}  {item.description} {x} {item.price}{Bcolors.ENDC}")

            print("-"*50)
            i += 1
        while True:
            # try block to make sure that the input is within range and upon pressing only enter it exits the funtion
            try:
                print("press enter to go back")
                item_choice = int(input("Choose an item to buy: ")) - 1
                self.items[item_choice]
                verify = self.items[item_choice]
            except IndexError:
                print(
                    f"{Bcolors.WARNING}the item doesnt exist. choose the correct item\n{Bcolors.ENDC}")
            except ValueError:
                return None
            else:
                break
        # if player doesnt have sufficient money to buy the item
        if player.money < self.items[item_choice].price:
            print(
                f"{Bcolors.FAIL}YOU DONOT HAVE ENOUGH CREDITS.KILL SOME MORE ENEMIES AND THEN COME BACK{Bcolors.ENDC}")
            return None

        # asks how many items the player wants to buy
        while True:
            try:
                buy_qty = int(
                    input(f"How many {self.items[item_choice].name} do you want to buy: "))
            except ValueError:
                print(f"{Bcolors.FAIL}Enter a number greater than 0{Bcolors.ENDC}")
            else:
                break

        total = buy_qty*self.items[item_choice].price

        # if player buys more items than he can afford
        if total > player.money:
            print(
                f"{Bcolors.FAIL}YOU DONOT HAVE ENOUGH CREDITS.KILL SOME MORE ENEMIES AND THEN COME BACK{Bcolors.ENDC}")
        else:
            player.money -= total
            print(
                f"{Bcolors.OKGREEN}You successfully bought {buy_qty} x {self.items[item_choice].name} for {total} credits.{Bcolors.ENDC}")
            print(f"Your remaining credits are: {player.money}")

            # checks if the item is present in the player's items list
            for item in player.items:
                item_present = False
                # if item is present it increments the item.qty
                if item.name == self.items[item_choice].name:
                    player.items[item_choice].qty += buy_qty
                    item_present = True
                    break
            # if item isnt present then it instantiate another object and appends it to the list
            if item_present == False:
                name, typ, description, prop, qty, price = self.items[item_choice].to_tuple(
                )
                player.items.append(
                    Item(name, typ, description, prop, buy_qty, price))


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
player_items = []
shop_items = []
with open("items.json") as f_obj:
    items = json.load(f_obj)
for item in items:
    player_items.append(Item.from_string(item))
    shop_items.append(Item.from_string(item,shop=True))

if path.exists("game_data.pkl"):
    user_in = input("Save file found, Press enter to load from file to start new game press N: ")
    if user_in == "":
        with open("game_data.pkl","rb") as save_file:
            game_data = pickle.load(save_file)
            player = game_data[0]
            enemy = game_data[1]
    else:
        player = Person("Umer", 460, 65, 60, 34, items=player_items)
        enemy = Person("Xerg", 500, 65, 45, 25)
else:
    player = Person("Umer", 460, 65, 60, 34, items=player_items)
    enemy = Person("Xerg", 500, 65, 45, 25)

item_shop = Shop(shop_items)

# load spells data from a JSON file
with open("spells.json") as f_obj:
    spells = json.load(f_obj)
for spell in spells:
    player.mag_from_string(spell)


running = True


print(Bcolors.FAIL + Bcolors.BOLD + "AN ENEMY ATTACKS" + Bcolors.ENDC)

# Main program Block
while running:

    print("==================================")
    player.choose_action()
    choice = input("Choose action: ")
    # TRY block so that wrong input leads to player attacking by default
    try:
        index = int(choice) - 1
        player.action[index]
    except (ValueError, IndexError):
        index = 0
    else:
        print(f"You chose {player.action[index]}!")


# IF player choose to attack
    if index == 0:
        print("="*50)
        dmg = player.generate_damage(enemy)
        enemy.take_damage(dmg)
        print(f"the player did {dmg} damage to the enemy.")

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
            print(
                f"{Bcolors.OKBLUE} the {spell.name} does {magic_damage} damage {Bcolors.ENDC} ")
            enemy.take_damage(magic_damage)
            print(f"the player did {magic_damage} damage to the enemy.")

        # Spells that Heal (WHITE)
        elif spell.typ.lower() == "white":
            print(
                f"{Bcolors.OKGREEN} the {spell.name} Heals {magic_damage} HP {Bcolors.ENDC} ")

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
        print(f"{Bcolors.OKBLUE}{item.name} {item.description}{Bcolors.ENDC}")

        if item.typ == "potion":
            player.heal_hp(item.prop)

        elif item.typ == "elixer":
            player.heal_hp(item.prop)
            player.heal_mp(item.prop)

        elif item.typ == "attack":
            enemy.take_damage(item.prop)


# ENEMY attacks

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage(player)
    player.take_damage(enemy_dmg)
    # player2.take_damage(enemy_dmg)

    # changes color of player's current HP according to remaining HP
    if player.get_hp() / player.get_max_hp() < 0.15:
        x = Bcolors.FAIL
    elif player.get_hp() / player.get_max_hp() < 0.8:
        x = Bcolors.WARNING
    else:
        x = Bcolors.OKGREEN
    print(
        f"Enemy attacks for {enemy_dmg} points", enemy.atk, enemy.df)

    print("============================================")
    print(
        f"ENEMY HP:{Bcolors.FAIL} {enemy.get_hp()}/{enemy.get_max_hp()}{Bcolors.ENDC}\n")

    print(
        f"PLAYER HP:{x} {player.get_hp()}/{player.get_max_hp()}{Bcolors.ENDC}")
    print(
        f"YOUR MP:{Bcolors.OKBLUE} {player.get_mp()}/{player.get_max_mp()}{Bcolors.ENDC}")

    # Fail or Win check
    if enemy.get_hp() == 0:

        print(f"{Bcolors.OKGREEN} you win! {Bcolors.ENDC}")

        player.money += 500
        print("You won 500 credits. You can buy various items with them")
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
                    print("*"*20)
                    break

        play_again = input("Press enter to continue else type Q to quit: ")
        

        if play_again.lower() == "q":
            print("Saving Progress...")
            player.reset_stats()
            enemy.reset_stats()
            game_data = [player, enemy]
            # saving game_data in Pickle file
            with open("game_data.pkl", "wb") as save_file:
                pickle.dump(game_data, save_file, -1)
            running = False
        else:
            enemy.max_hp += int(player.hp)
            player.level_up()
            enemy.atk += 5 * player.level//2
            enemy.df += 5 * player.level//2
            enemy.reset_stats()
            running = True
            game_data = [player,enemy]
            print("Saving Progress...")
            with open("game_data.pkl","wb") as save_file:
                pickle.dump(game_data,save_file,-1)
    elif player.get_hp() == 0:
        print(f"{Bcolors.FAIL} you lost! {Bcolors.ENDC}")

        running = False
