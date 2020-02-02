letters = list("abc")
items = (0, "a")
index, letter = items

for letter in letters:
    print(letter)

# Enumeratre function return a tuple
for letter in enumerate(letters):
    print(letter[0], letter[1])

# Similar to the above expression but more cleaner. we used tuples unpacking, REFER to the line 3
for index, letter in enumerate(letters):
    print(index, letter)