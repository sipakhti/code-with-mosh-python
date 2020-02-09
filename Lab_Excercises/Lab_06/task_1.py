str1 = list(input("Please input the string: "))
encrypted_string = ""

for i in range(len(str1)):
    if str1[i].lower() in "aeiou" and i % 2 != 0:
        str1[i] = "_"
for char in str1:
    encrypted_string = encrypted_string + char

print(encrypted_string)


