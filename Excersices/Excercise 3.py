from pprint import pprint
# MY METHOD
sentence = input("Please Input a string")

count = 0
for char in sentence:
    if char != " ":
        if sentence.count(char) > count:
            count = sentence.count(char)
            winner = char


print(winner, count)

# MOSH METHOD(MODIFIED)
# char_freq = {}
# for char in sentence:
#     if char in char_freq:
#         char_freq[char] += 1
#     else:
#         char_freq[char] = 1
# MOSH METHOD (MODIFIED)
# char_freq = {char: sentence.count(char) for char in sentence}

# char_freq_sorted = sorted(
#     char_freq.items(),
#     key=lambda kv: kv[1],
#     reverse=True)

# print(char_freq_sorted[0])
