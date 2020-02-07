# Implement a program that calculates the bill of a hotdog stand. The program should ask the user to
# enter the quantity of each of the items. Then compute 13 % GST on the total amount and generate
# a bill with items, their quantity along with price of each item and the total(inclusive GST). Since
# the prices should remain fixed so store them wisely.
# The stand has the following items:
#  Hotdog for $2.50
#  Drink for $1.25
#  Extra Sauce for $0.50
#  Extra Meat for $1.25

menu = {"Hotdog     ": 2.50, "Drink      ": 1.25,
        "Extra Sauce": 0.50, "Extra Meat ": 1.25}
user_menu = {"Hotdog     ": 2.50, "Drink      ": 1.25,
             "Extra Sauce": 0.50, "Extra Meat ": 1.25}
total = 0

for item, price in menu.items():
    user = input(f"do you want {item}for ${price}: ")
    if ("s" in user.lower()) or ("e" in user.lower()) or ("y" in user.lower()):
        user_menu[item] *= float(input("Please enter the required amount: "))
    else:
        del user_menu[item]
print("ITEM             PRICE    QTY      TOTAL")
for item, price in user_menu.items():
    print(f"{item}      ${menu[item]}     {price/menu[item]}      ${price}")
    total += price

gst = (13*total)/100
print(f"\nAmount in USD                      {total}")
print(f"GST 17%                            {gst}")
print(f"TOTAL in USD                       {round(total+gst, 2)}")
