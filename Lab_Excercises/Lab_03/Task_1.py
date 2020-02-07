from os import system
char1 = input("Char1: ")
char2 = input("Char2: ")
char3 = input("Char3: ")

char1, char2 = char2, char1
char2, char3 = char3, char2

system("cls")
print(f"Char1: {char1}")
print(f"Char2: {char2}")
print(f"Char3: {char3}")
