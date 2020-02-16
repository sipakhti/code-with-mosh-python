user_input = input("Enter String:\n")



def str_permutation(string: str = ...):
    """
    break any string into every possible substring
    """
    temp_list = []
    for x in range(1,len(string)+1):
        for y in range(len(string)):
            temp = string[y:x]
            if temp != "":
                temp_list.append(temp)
    return sorted(temp_list, key=lambda item: len(item))
    

print(*str_permutation(user_input))
