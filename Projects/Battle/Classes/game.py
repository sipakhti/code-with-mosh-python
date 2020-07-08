import random
import pickle


class Bcolors:
    """Output Color Formatter Map"""
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class Person:

    def __init__(self, name, hp: int, mp: int, atk: int, df: int, magic=[], items=[], level=1):

        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atk = atk
        self.atkl = self.atk - 10
        self.atkh = self.atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.level = int(level)

    def _calculate_hp_bar(self, player_hp):
        if player_hp < 5:
            color_hp = "52"
        elif player_hp < 10:
            color_hp = "208"
        elif player_hp < 15:
            color_hp = "178"
        elif player_hp < 20:
            color_hp = "190"
        elif player_hp >= 20:
            color_hp = "40"
        hp_bar = "\033[48;5;" + color_hp + "m" + " " * player_hp + "\033[0m"
        return hp_bar

    def reset_stats(self):
        self.hp = self.max_hp
        self.mp = self.max_mp
        self.atkl = self.atk - 10
        self.atkh = self.atk + 10

    def generate_damage(self, attackee):
        """ Generate random damage"""
        return random.randrange(int(
            self.atkl), int(self.atkh))

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

    def pop_items(self):
        """moves the item with 0 quantity to the end of the list.
            support method for choose_item()
        """
        print(type(self.items))
        x = -1
        for index in range(len(self.items)):

            if self.items[index].qty < 1:
                x = index
        if x != -1:
            self.items.pop(x)

    def load_magic(self, filename):
        with open(filename, "rb") as spells:
            self.magic = pickle.load(spells)

    def load_items(self, filename):
        with open(filename, "rb") as player_items:
            self.items = pickle.load(player_items)

    def compare_stats(self, other):
        """Compare stats of two instances of Player Class"""
        hp = self.hp > other.hp
        mp = self.mp > other.mp
        atk = self.atk > other.atk
        df = self.df > other.df
        lvl = self.level > other.level

        hp = self.compare_stat(hp, other)

        mp = self.compare_stat(mp, other)

        atk = self.compare_stat(atk, other)

        df = self.compare_stat(df, other)

        lvl = self.compare_level(lvl, other)

        print(f"    {self.name}    {other.name}")
        print(f"HP: {hp}\nMP: {mp}\nATK: {atk}\nDEF: {df}\nLEVEL: {lvl}")

    def compare_stat(self, stat, other):
        if stat:
            stat = Bcolors.OKGREEN + str(self.df) + \
                 "  >  " + str(other.df) + Bcolors.ENDC
        elif not stat:
            stat = Bcolors.FAIL + str(self.df) + "  <  " + \
                   str(other.df) + Bcolors.ENDC
        return stat

    def compare_level(self, lvl, other):
        if self.level == other.level:
            lvl = str(self.level) + " == " + str(other.level)
        else:
            lvl = self.compare_stat(lvl, other)

        return lvl

    def __str__(self):
        """Returns the breakdown of player stats,spells and inverntory"""

        magic = ""
        inventory = ""
        for spell in self.magic:
            magic += " " + spell.name
        for item in self.items:
            inventory += " " + item.name
        return f"HP:{self.hp}/{self.max_hp}\nMP:{self.mp}/{self.max_mp}\nATK:{self.atk}\nDEF:{self.df}\nLVL:{self.level}\nCREDITS:{self.money}\nMAGIC:{magic}\nINVERNTORY:{inventory}"


class Enemy(Person):

    def __init__(self, name, hp, mp, atk, df):
        super().__init__(name, hp, mp, atk, df)

    def get_enemy_stats(self):

        # Logic for dynamically adjusting the string to accomodate for different length strings
        player_mp_len = ' ' * len(str(self.mp) + '/' + str(self.max_mp))
        player_hp_len = ' ' * len(str(self.hp) + '/' + str(self.max_hp))
        # Logic for HP bar
        player_hp = int(((self.hp / self.max_hp) * 100) * 40 / 100)
        hp_bar = self._calculate_hp_bar(player_hp)
        # Logic for MP bar
        player_mp = int(((self.mp / self.max_mp) * 100) * 10 / 100)
        mp_bar = "\033[44m" + " " * player_mp + "\033[0m"
        # Console output

        print(f"{player_hp_len}       {' ' * (len(self.name) - 4)}     {'_' * 40}")
        print(f'{self.name}  HP: {self.hp}/{self.max_hp} |{hp_bar}{" " * (40 - player_hp)}|')


    def reset_stats(self):
        self.hp = self.max_hp
        self.mp = self.max_mp
        self.atkl = self.atk - 10
        self.atkh = self.atk + 10
        for item in self.items:
            item.qty += 1


class Player(Person):

    def __init__(self, name, hp, mp, atk, df, money=0):
        super().__init__(name, hp, mp, atk, df)
        self.money = int(money)
        self.action = ["Attack", "Magic", "Item"]

    def level_up(self):
        self.level += 1
        self.max_hp += int(self.max_hp * (self.level / 200))
        self.max_mp += int(self.max_mp * (self.level / 200))
        self.atk = int(self.atk * (1 + self.level / 50))
        self.df = int(self.df * (1 + self.level / 50))
        self.atkl = self.atk - 10
        self.atkh = self.atk + 10

        self.reset_stats()

    def choose_action(self):
        """prints on the screen the actions that a user can take"""
        i = 1
        print(Bcolors.OKBLUE, "What do you want to do ", self.name, Bcolors.ENDC)
        for item in self.action:
            print("    " + str(i) + ":", item)
            i += 1

    def choose_magic(self):
        """prints on the screen availible spells"""
        print("-" * 50)
        print(Bcolors.OKGREEN, "Which spell to cast, ", self.name, Bcolors.ENDC)
        i = 1
        for spell in self.magic:
            # color codes the COST if MP is not sufficient
            if spell.cost > self.get_mp():
                x = Bcolors.FAIL
            else:
                x = Bcolors.OKGREEN
            print(
                f"    {i}: {spell.name} {x} (cost: {spell.cost}) {Bcolors.ENDC} (damage: {spell.dmg}) (Remaining : {self.mp // spell.cost})")
            i += 1

    def choose_item(self):
        """prints out the menu of items the player has.
            doesnt show the items with 0 quantity
        """
        i = 1
        print("-" * 50)
        print(
            f"\r{Bcolors.OKGREEN}{Bcolors.BOLD}{self.name} these are the items currently in your inventory {Bcolors.ENDC}")
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

    def get_player_stats(self):
        """Prints out a nice formatted version of the instance stats"""
        # Logic for dynamically adjusting the string to accomodate for different length strings
        player_mp_len = ' ' * len(str(self.mp) + '/' + str(self.max_mp))
        player_hp_len = ' ' * len(str(self.hp) + '/' + str(self.max_hp))
        # Logic for HP bar
        player_hp = int(((self.hp / self.max_hp) * 100) * 25 / 100)

        hp_bar = self._calculate_hp_bar(player_hp)
        # Logic for MP bar
        player_mp = int(((self.mp / self.max_mp) * 100) * 10 / 100)
        mp_bar = "\033[44m" + " " * player_mp + "\033[0m"
        # Console output

        print(f"{' ' * len(self.name)}      {player_hp_len}  {'_' * 25}  {player_mp_len}      {'_' * 10}")
        print(
            f'{self.name}  HP: {self.hp}/{self.max_hp} |{hp_bar}{" " * (25 - player_hp)}| {self.mp}/{self.max_mp} MP: |{mp_bar}{" " * (10 - player_mp)}|')


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
        return f"{self.name} cost:{self.cost} damage:{self.dmg} type:{self.typ}"


class Item:

    # Constructor 
    def __init__(self, name, typ, description, prop: int, qty: int, price: int):
        self.name = name
        self.typ = typ
        self.description = description
        self.prop = int(prop)
        self.qty = int(qty)
        self.price = int(price)

    @classmethod
    def from_string(cls, item_string, shop=False):
        """parses string seperated by a custom seperator into individual
           attributes.
           By default the "-" is the seperator
           correct format = name-type-descripton-prop-qty-price
        """
        name, typ, description, prop, qty, price = item_string.split("-")
        return cls(name, typ, description, prop, qty, price) if shop == False else cls(name, typ, description, prop, 99,
                                                                                       price)

    def reduce_quantity(self):
        """ Reduces quantity of the item by 1"""
        self.qty -= 1

    def to_tuple(self):
        """ creates a tuple of all its attributes to be used to instantiate new items
            in player inverntory during shopping
        """
        return self.name, self.typ, self.description, self.prop, self.qty, self.price

    def __str__(self):
        return f"{self.name} type:{self.typ} description:{self.description} price:{self.price}"


class Shop:

    def __init__(self, items=[]):
        self.items = items

    def load_shop_items(self, filename):
        """ populates the shop attribute items from a Json file """
        with open(filename, "rb") as f_obj:
            self.items = pickle.load(f_obj)

    def sell_items(self, player):
        print("*" * 20)
        print(Bcolors.BOLD, "The shop is selling:", Bcolors.ENDC)
        print(
            f"{Bcolors.OKGREEN}{Bcolors.BOLD}{Bcolors.UNDERLINE}{player.name.strip()}'s{Bcolors.ENDC} current credits: {Bcolors.OKBLUE}{Bcolors.BOLD}{player.money}{Bcolors.ENDC}")
        print(Bcolors.OKGREEN, "~" * 50, Bcolors.ENDC)
        i = 1
        for item in self.items:
            if item.price > player.money:
                x = Bcolors.FAIL
            else:
                x = Bcolors.OKGREEN

            print(
                f"{i}: {item.name}  {item.description} {x} {item.price}{Bcolors.ENDC}")

            print(Bcolors.WARNING, Bcolors.BOLD, "-" * 50, Bcolors.ENDC)
            i += 1
        while True:
            # try block to make sure that the input is within range and upon pressing only enter it exits the funtion
            try:
                print("press enter to go back")
                item_choice = int(input("Choose an item to buy: ")) - 1
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

        total = buy_qty * self.items[item_choice].price

        # if player buys more items than he can afford
        if total > player.money:
            print(
                f"{Bcolors.FAIL}YOU DONOT HAVE ENOUGH CREDITS.KILL SOME MORE ENEMIES AND THEN COME BACK{Bcolors.ENDC}")
        else:
            player.money -= total
            print(
                f"{Bcolors.OKGREEN}{player.name} successfully bought {buy_qty} x {self.items[item_choice].name} for {total} credits.{Bcolors.ENDC}")
            print(f"{player.name.strip()}'s remaining credits are: {player.money}")

            # checks if the item is present in the player's items list
            for item in player.items:
                item_present = False
                # if item is present it increments the item.qty
                if item.name == self.items[item_choice].name:
                    player.items[item_choice].qty += buy_qty
                    item_present = True
                    break
            # if item isnt present then it will instantiate another object and appends it to the list
            if not item_present:
                name, typ, description, prop, qty, price = self.items[item_choice].to_tuple()
            player.items.append(self.items[item_choice])
            player.items[-1].qty = buy_qty
