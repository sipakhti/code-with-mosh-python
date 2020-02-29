from assorted import count_occurances


filename = "Crash_Course\ALICE.txt"

try:
    with open(filename, encoding="utf8") as file_object:
        content = file_object.read()
except FileNotFoundError:
    print(f"The file {filename} does not exist in the root directory")
else:
    words = content.split()
    num_words = len(words)

print(num_words)
print("the word '{}' is the most occuring word which repeated {} times.".format(
    *count_occurances(words, "alice")))
