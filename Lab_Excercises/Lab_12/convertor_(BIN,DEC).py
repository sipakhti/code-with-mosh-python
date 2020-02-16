def dec_to_bin(decany: int, output=""):
    decany = int(decany)
    if decany == 0:
        return output
    elif decany % 2 == 0:
        output += "0"

    elif decany % 2 == 1:
        output += "1"

    output = dec_to_bin(decany // 2, output)

    return output[::-1]


def bin_to_dec(binary: str):
    if len(binary) == 0:
        return 0
    decany = 0
    if binary[0] == "1":
        decany += 1 * pow(2,len(binary)-1)
    if binary[0] == "0":
        pass
    decany += bin_to_dec(binary[1:])
    return decany


user_input = input("Enter a binary sequence:\n")
print(bin_to_dec(user_input))
user_input = input("Enter a Decany number:\n")
print(dec_to_bin(user_input))


# index = 1
# decany = 0
# for bit in user_input:
#     if bit == "1" :
#         decany += 1 * pow(2,len(user_input) - index)
#     if bit == "0":
#         decany += 0
#     index += 1

# print(decany)
# binary = []
# user_input = int(input("Enter a Decany Value:\n"))
# while user_input != 0:
#     if user_input % 2 == 0:
#         user_input = user_input//2
#         binary.insert(0,0)
#     elif user_input % 2 == 1:
#         user_input = user_input//2
#         binary.insert(0, 1)

# print(*binary)




    
