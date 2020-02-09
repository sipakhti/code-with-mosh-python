from distutils import util


def user_input():
    price, items = 0, 0

    try:
        product = input("Enter the name of the product:\n")
        price = int(input("Enter the price of product\n"))
        items = int(input("Enter the No. of items:\n"))
    except ValueError:
        print("Wrong PRICE or QUANTITY!!!")
        exit

    return product, price, items


product_list = {}
bill_total = 0
try:
    product, price, items = user_input()
    product_list[product] = (price, items)
    print(f"{product} has been added to the bill.")
except (UnboundLocalError, NameError):
    pass


item_add = True

while item_add:
    try:
        item_add = bool(util.strtobool(
            input("Do you want to add another product?\n")))
    except ValueError as error:
        print("Wrong Input, the program will quit beacuse of your own stupidity!")
        break

    if item_add == False:
        break

    product, price, items = user_input()
    product_list[product] = (price, items)
    print(f"{product} has been added to the bill.")

print(f"PRODUCT{' '*16}PRICE        QTY        Total")
for prod in product_list.items():
    print(f"{prod[0]}{' '*(16-len(prod[0]))}       {prod[1][0]} {' '*(12-len(str(prod[1][0])))}{prod[1][1]} {' '*(10-len(str(prod[1][1])))}{prod[1][0]*prod[1][1]}")
    bill_total += prod[1][0] * prod[1][1]

print(f"\n{' '*32}TOTAL PAYABLE: {bill_total}")
