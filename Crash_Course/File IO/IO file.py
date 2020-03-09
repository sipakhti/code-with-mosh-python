from assorted import to_json

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
spells = []
i = 0
while True:
    user_in = input("press enter to continue adding spells.\nEnter q to exit: ")
    if user_in.lower() == "q":
        break
    spell_name = input("Enter the name of the spell: ")
    spell_cost = input("Enter the cost of the spell: ")
    spell_dmg = input("Enter the damage of the spell: ")
    spell_type = input("Enter type of the spell: ")

    spell = "-".join((spell_name,spell_cost,spell_dmg,spell_type))
    spells.append(spell)
    i +=1


if i >0:
    filename = "spells.json"
    to_json(filename,spells)

i = 0
items = []
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

    item = "-".join((item_name,item_type,item_desc,item_prop,item_qty,item_price))
    items.append(item)

    i += 1

if i > 0:    
    filename = "items.json"
    to_json(filename,items)
