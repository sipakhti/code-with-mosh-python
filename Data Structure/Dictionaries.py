point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 10  # index are names of key
point["z"] = 20
print(point)

# to make sure the program doesnt crash due to invalid dict key
if "a" in point:
    print(point["a"])

# Alternative approach using .get function and it makes the code cleaner 
print(point.get("a", 0))

# for deleting an item
del point["x"]
print(point)

# itereating over a dictionary. When looping only the key is returned
for key in point:
    print(key, point[key])

# .item funtion returns a tuple of (key, value) pair which can be unpacked like any other tuple
for key, value in point.items():
    print(key, value)


# this comprehensioin can also be used with sets and dictionaries
values = [x * 2 for x in range(5)]
# Comprehnsion method for sets
sets = {x * 2 for x in range(5)}
print(sets)
# Comprehension metthod for dictionary
dicts = {x: x*2 for x in range(5)}
print(dicts)
# Topic for next lecture -- Genearator object
tupes = (x * 2 for x in range(5)) 
print(tupes)