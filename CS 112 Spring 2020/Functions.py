
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


def skip_sum(num1, num2, N):
    """Returns the sum of the integers between numl and num2 inclusive
       but it skips every Nth number in this sequence.
       N is always larger than 1 while num1 and num2 can be in any order
    """

    count = 0
    total = 0
    if num1 > num2:
        num1, num2 = num2, num1

    for i in range(num1, num2+1):
        count += 1
        # using another variable count as a counter so that Nth number can be skipped
        if count % N != 0:
            total += i
        else:
            pass

    return total


def cubic_root(num):
    """ Given a positive number num,
        it returns its cubic root only if it's a whole number.
    """

    for i in range(num):
        if (i * i * i) == num:
            return i

    return num if num == 1 else None


def count_moves(start, end, step):

    count = 0
    position = start

    while position < end:

        position += step
        count += 1

        if position % 10 == 7 or position % 10 == 8:
            position += position % 10
        else:
            pass

        if position % 10 == 3 or position % 10 == 5:
            step += position % 10
        else:
            pass

    return count


def max_dna(num):

    base_a = 0
    base_t = 0
    base_g = 0
    base_c = 0
    count = 1
    # anything divided(//) by 10,100,1000.....will strip the last digits from the right
    # correspoding to the number of 0s
    # by striping down the most least significant number the number can be iterated through
    # and by taking the modulus by 10 at every stage will procide the last digit thus isolating it for operations

    while num % count != num:
        if (num // count) % 10 == 1:
            base_a += 1
        elif (num // count) % 10 == 2:
            base_c += 1
        elif (num // count) % 10 == 3:
            base_g += 1
        elif (num // count) % 10 == 4:
            base_t += 1
        else:
            pass

        count *= 10

    if base_a > base_c and base_a > base_g and base_a > base_t:
        return "A"
    if base_c > base_a and base_c > base_g and base_c > base_t:
        return "C"
    if base_g > base_a and base_g > base_c and base_g > base_t:
        return "G"
    if base_t > base_a and base_t > base_c and base_t > base_g:
        return "T"


def scrabble_number(num):
    """Returns a scrabbled version of num by swapping the two digits
       of every consecutive pair of digits starting from the right.
    """

    diviser = 1
    digit_tacker = 0  # to keep track of digits in number
    scrambled_num = 0

    # this while loop gives correct results if the number of digits are even
    while num % diviser != num:

        pair = (num // diviser) % 100

        first_digit = pair // 10
        second_digit = pair % 10

        if diviser == 1:
            scrambled_num += second_digit * 10 + first_digit
        elif diviser > 1:
            scrambled_num += second_digit * \
                (diviser*10) + first_digit * (diviser)

        diviser *= 100
        digit_tacker += 1

    count = 0
    diviser = 1
    # loops through the number to count the digits
    while num % diviser != num:
        diviser *= 10
        count += 1

    # check whether digits in number are even or odd
    if count % 2 != 0:
        diviser = 1  # it iterates through the number in blocks of two

        limiter = 1  # local while loop variable for increment and make sure that the loop stops
        # before the first digit is reached

        scrambled_num = 0
        # for numbers who have odd number of digits but the logic is the same for extraction of pairs
        while limiter < digit_tacker:

            pair = (num // diviser) % 100

            first_digit = pair // 10
            second_digit = pair % 10

            if diviser == 1:
                scrambled_num += second_digit * 10 + first_digit
            elif diviser > 1:
                scrambled_num += second_digit * \
                    (diviser*10) + first_digit * (diviser)

            diviser *= 100
            limiter += 1

        # adds the single digit at the extreme left in case of odd number of digits
        scrambled_num += (num//diviser) * diviser

    return scrambled_num
