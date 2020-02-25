
def count_multiples(num1, num2, N):
    """ Reutrns the number of multiples of N that exist between num1 and num2
        N cannot be 0 while num1 and num2 can be in any order
    """
    count = 0
    if num1 > num2:
        num1, num2 = num2, num1

    for i in range(num1, num2 + 1):
        if i % N == 0:
            count += 1

    return count
