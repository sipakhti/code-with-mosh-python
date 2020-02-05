from pprint import pprint
from timeit import timeit
# MY METHOD (runs faster than MOSH_mod algorithim but slower than MOSH algorithim)

sentence = "This is a sentence of some sorts"  # input("Please Input a string")

count = 0
for char in sentence:
    if char != " ":
        if sentence.count(char) > count:
            count = sentence.count(char)
            winner = char


print(winner, count)
# count = 0
# temp = []
# char1 = input("which alphabet do you want to count?")
# for char in sentence.lower():
#     if char == char1.lower():
#         count += 1

# print(char1, count)

# MOSH METHOD (fastest)
# char_freq = {}
# for char in sentence:
#     if char in char_freq:
#         char_freq[char] += 1
#     else:
#         char_freq[char] = 1
# MOSH METHOD (MODIFIED) (slowest)
# char_freq = {char: sentence.count(char) for char in sentence}

# char_freq_sorted = sorted(
#     char_freq.items(),
#     key=lambda kv: kv[1],
#     reverse=True)

# print(char_freq_sorted[0])
