vowels_count = 0
user_input = input("Enter any phrase:\n")


for char in "aeiou":
    vowels_count += user_input.lower().count(char)

print("Total Number of Words:", len(user_input.split()))
print("Total Number of Vowels:", vowels_count)
