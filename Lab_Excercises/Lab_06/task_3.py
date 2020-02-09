string = input(
    "Input coordinates (X,Y). Values must be separated by either a comma(\",\") or blank space(\" \")\n")
if "," in string:
    x, y = string.split(",")
else:
    x, y = string.split()
x, y = int(x), int(y)

movement = input("Press keys W,S,D,A to move UP,DOWN,RIGHT,LEFT repectively")

if "w" in movement.lower():
    y = y + movement.lower().count("w")
if "s" in movement.lower():
    y = y - movement.lower().count("s")
if "d" in movement.lower():
    x = x + movement.lower().count("d")
if "a" in movement.lower():
    x = x - movement.lower().count("a")

print(f"X:{x} Y:{y}")
