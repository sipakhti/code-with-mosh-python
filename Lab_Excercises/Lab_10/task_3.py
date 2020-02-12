
def check_palindromicity(s=str):
    limit = len(s)
    count = 0
    for index in range(limit):
        if s[index] == s[limit - 1 - index]:
            count += 1

    return True if count == limit else False


user_input = input(
    "Enter any Word or sequence or alphabets to check for palindromicity:\n")


if check_palindromicity(user_input):
    print("It's a Palindromic sequence!!")
else:
    print("It's just a plain old sequence!!")
