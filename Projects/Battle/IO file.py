from pickle import dump, load
from os import path

from .Classes.game import Item, Spell

# # Create Black Magic
# fire = Spell.from_string("Fire-10-100-black")
# thunder = Spell.from_string("Thunder-10-100-black")
# blizzard = Spell.from_string("Blizzard-10-100-black")
# meteor = Spell.from_string("Meteor-20-200-black")
# quake = Spell.from_string("Quake-14-140-black")

# # Create White Magic
# cure = Spell.from_string("Cure-12-120-white")
# cura = Spell.from_string("Cure-18-200-white")
# filename = "spells.json"
spells_file = "C:\\Users\\omers\\Desktop\\HelloWorld\\Projects\\Battle\\spells.pkl"
player_item_file = "C:\\Users\\omers\\Desktop\\HelloWorld\\Projects\\Battle\\player_items.pkl"
shop_item_file = "C:\\Users\\omers\\Desktop\\HelloWorld\\Projects\\Battle\\shop_item.pkl"

spells = []
i = 0
if path.exists(spells_file):
    print("The spells data file already exists")
    view_data = input("Press Enter to view the content or input N to overwrite the existing file: ")
    print("")
    if view_data == "":
        with open(spells_file, "rb") as f_obj:
            file_data = load(f_obj)
            count = 0
            for spell in file_data:
                count += 1
                print(count, ":", spell)

        user_in = input("Press Enter to add new spells or Press N to overwrite the existong file:")
        if user_in == "":
            spells = file_data
        else:
            pass
    else:
        pass

while True:

    user_in = input("press enter to continue adding spells.\nEnter q to exit: ")
    if user_in.lower() == "q":
        break
    spell_name = input("Enter the name of the spell: ")
    spell_cost = input("Enter the cost of the spell: ")
    spell_dmg = input("Enter the damage of the spell: ")
    spell_type = input("Enter type of the spell: ")

    spell = "-".join((spell_name, spell_cost, spell_dmg, spell_type))
    spells.append(Spell.from_string(spell))
    i += 1

if i > 0:
    with open(spells_file, "wb") as spells_file:
        dump(spells, spells_file, -1)

i = 0
items = []
if path.exists(spells_file):
    print("The player item data file already exists")
    view_data = input("Press Enter to view the content or input N to overwrite the existing file: ")
    print("")
    if view_data == "":
        with open(player_item_file, "rb") as f_obj:
            file_data = load(f_obj)
            count = 0
            for item in file_data:
                count += 1
                print(count, ":", item)

        user_in = input("Press Enter to add new spells or Press N to overwrite the existong file:")
        if user_in == "":
            items = file_data
        else:
            pass
    else:
        pass
while True:
    user_in = input(
        "press enter to continue adding Items.\nEnter q to exit: ")
    if user_in.lower() == "q":
        break

    item_name = input("Enter Item Name: ")
    item_type = input("Enter Item Type: ")
    item_desc = input("Enter Item Description: ")
    item_prop = input("Enter Item Prop: ")
    item_qty = input("Enter Item qty: ")
    item_price = input("Enter Item Price: ")

    item = "-".join((item_name, item_type, item_desc, item_prop, item_qty, item_price))
    items.append(item)

    i += 1

if i > 0:
    with open(player_item_file, "wb") as player_items:
        dump(items, player_items, -1)

# SHOP ITEMS
i = 0
items = []
if path.exists(spells_file):
    print("The shop data file already exists")
    view_data = input("Press Enter to view the content or input N to overwrite the existing file: ")
    print("")
    if view_data == "":
        with open(shop_item_file, "rb") as f_obj:
            file_data = load(f_obj)
            count = 0
            for item in file_data:
                count += 1
                print(count, ":", item)

        user_in = input("Press Enter to add new spells or Press N to overwrite the existong file:")
        if user_in == "":
            items = file_data
        else:
            pass
    else:
        pass
while True:
    user_in = input(
        "press enter to continue adding Items.\nEnter q to exit: ")
    if user_in.lower() == "q":
        break

    item_name = input("Enter shop Item Name: ")
    item_type = input("Enter shop Item Type: ")
    item_desc = input("Enter shop Item Description: ")
    item_prop = input("Enter shop Item Prop: ")
    item_price = input("Enter shop Item Price: ")

    item = "-".join((item_name, item_type, item_desc, item_prop, "99", item_price))
    items.append(Item.from_string(item, shop=True))

    i += 1

if i > 0:
    with open(shop_item_file, "wb") as shop_items:
        dump(items, shop_items, -1)
