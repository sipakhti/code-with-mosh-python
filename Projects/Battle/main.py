from Classes.game import Bcolors
import random


class Person:

    def __init__(self, hp, mp, atk, df, magic=[], items=[]):
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.action = ["Attack", "Magic", "Item"]

    # Alternate Contructor for Magic Property
    def mag_from_string(self, mag_string):
        """parses the string in which spells are seperated with a ","
           and then passes the parsed string to the Spell class'
           alternate constructor and saves the object that is 
           instantiated in a list
        """
        magics = mag_string.split(",")
        for magic in magics:
            self.magic.append(Spell.from_string(magic))

    def generate_damage(self):
        """ Generate random damage"""
        return random.randrange(self.atkl, self.atkh)

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

    def heal_mp(self, amount):
        if self.mp + amount > self.max_mp:
            self.mp = self.max_mp
        else:
            self.mp += amount

    def choose_action(self):
        """prints on the screen the actions that a user can take"""
        i = 1
        print("Actions")
        for item in self.action:
            print(str(i) + ":", item)
            i += 1

    def choose_magic(self):
        """prints on the screen availible spells"""
        print("Magic")
        i = 1
        for spell in self.magic:
            # usre_friendly output as it color codes the COST if MP is not sufficient
            if spell.cost > self.get_mp():
                x = Bcolors.FAIL
            else:
                x = Bcolors.OKGREEN
            print(f"{i}: {spell.name} {x} (cost: {spell.cost}) {Bcolors.ENDC} (damage: {spell.dmg}) (Remaining : {self.mp//spell.cost})")
            i += 1

    def choose_item(self):
        i = 1
        print(f"{Bcolors.OKGREEN}{Bcolors.BOLD} ITEM {Bcolors.ENDC}")
        for item in self.items:
            if item.qty == 0:
                x = Bcolors.FAIL
            elif item.qty == 1:
                x = Bcolors.WARNING
            else:
                x = Bcolors.OKGREEN
            print(f"{i}: {item.name} {x}(QTY: {item.qty}){Bcolors.ENDC}")
            i += 1


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

# INventory


class Item:

    def __init__(self, name, typ, description, prop: int, qty: int):
        self.name = name
        self.typ = typ
        self.description = description
        self.prop = int(prop)
        self.qty = int(qty)

    @classmethod
    def from_string(cls, item_sring, seperator="-"):
        """parses string seperated by a custom seperator into individual
           attributes.
           By default the "-" is the seperator
        """
        name, typ, description, prop, qty = item_sring.split(seperator)
        return cls(name, typ, description, prop, qty)

    def reduce_quantity(self):
        self.qty -= 1


# # Create Black Magic
# fire = Spell.from_string("Fire-10-100-black")
# thunder = Spell.from_string("Thunder-10-100-black")
# blizzard = Spell.from_string("Blizzard-10-100-black")
# meteor = Spell.from_string("Meteor-20-200-black")
# quake = Spell.from_string("Quake-14-140-black")

# # Create White Magic
# cure = Spell.from_string("Cure-12-120-white")
# cura = Spell.from_string("Cure-18-200-white")
# [fire,thunder,blizzard,meteor,quake,cure,cura]

# Create Some items
potion = Item.from_string("Potion-potion-Heals 50 HP-50-2")
hipotion = Item.from_string("HiPotion-potion-Heals 100 HP-100-1")
superpotion = Item.from_string("SuperPotion-potion-Heals 500 HP-500-0")
elixer = Item.from_string(
    "Elixer-elixer-Fully Restores HP/MP of one party-9999-1")
hielixer = Item.from_string(
    "HiElixer-elixer-Fully Restores party's HP/MP-9999-0")

grenade = Item.from_string("Grenade-attack-Deals 500 Damage-500-1")

items = [potion, hipotion, superpotion, elixer, hielixer, grenade]

# INSTANTIATION
player = Person(460, 65, 60, 34, items=items)
enemy = Person(1200, 65, 45, 25)
3
player.mag_from_string(
    "Fire-10-100-Black,Blizzard-10-100-Black,Cure-12-120-White")
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
    except ValueError:
        index = 0
    else:
        print(f"You chose {player.action[index]}!")

# IF player choose to attack
    if index == 0:
        print("==================================")
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print(f"the player did {dmg} damage to the enemy.")

# IF player choose to use magic
    elif index == 1:
        print("==================================")
        player.choose_magic()

        while True:

            magic_choice = int(input("Choose Magic: ")) - 1
            # TRY block to make sure that the user input is within range
            try:
                spell = player.magic[magic_choice]
            except IndexError:
                print(
                    f"{Bcolors.WARNING}NO SUCH SPELL EXIST. SELECT THE CORRECT SPELL{Bcolors.ENDC}")
            else:
                break

        magic_damage = spell.generate_damage()
        current_mp = player.get_mp()

        # to make sure spell is only cast when their is enough mp
        if spell.cost > current_mp:
            print(Bcolors.FAIL, "\n not enough MP \n", Bcolors.ENDC)
            continue

            player.reduce_mp(magic_choice)
        # spells that attack (BLACK)
        if spell.typ == "Black":
            print(
                f"{Bcolors.OKBLUE} the {spell.name} does {magic_damage} damage {Bcolors.ENDC} ")
            enemy.take_damage(magic_damage)
            print(f"the player did {magic_damage} damage to the enemy.")

        # Spells that Heal (WHITE)
        elif spell.typ == "White":
            print(
                f"{Bcolors.OKGREEN} the {spell.name} Heals {magic_damage} HP {Bcolors.ENDC} ")

            player.heal_hp(spell.dmg)
            print(f"YOUR HP: {player.get_hp()}")

# if player choose ITEM
    elif index == 2:
        player.choose_item()
        item_choice = int(input("Choose Item: ")) - 1

        item = player.items[item_choice]
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

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)

    # changes color of player's current HP according to remaining HP
    if player.get_hp() / player.get_max_hp() < 0.15:
        x = Bcolors.FAIL
    elif player.get_hp() / player.get_max_hp() < 0.8:
        x = Bcolors.WARNING
    else:
        x = Bcolors.OKGREEN
    print(
        f"Enemy attacks for {enemy_dmg} points")

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
        running = False
    elif player.get_hp() == 0:
        print(f"{Bcolors.FAIL} you lost! {Bcolors.ENDC}")
