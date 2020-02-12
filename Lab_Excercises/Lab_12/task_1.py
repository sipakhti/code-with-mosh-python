

def reversal(string, output=""):
    """ RECURSIVE FUNCTION """
    if len(string) == 0:
        return output
    output += string[-1]
    output = reversal(string[:-1], output)
    
    return output



user_input = input("ENTER STRING: ")

print(reversal(user_input))






