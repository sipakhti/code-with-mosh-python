letters = list("abc")

if "d" in letters:
    print(letters.index("d"))

print(letters.count("d"))

print(letters.index("a"))
print(letters.index("d")) # will return an error so us it with an if statement (line 3)