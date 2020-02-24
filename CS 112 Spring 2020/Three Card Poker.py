
def straight_flush(one, two, three):
    """Returns True if its a straight flush"""
    # three combination of cards (a,b,c), (b,a,c), (c,a,b)
    combo1 = (one + two + three) / 3 == one
    combo2 = (one + two + three) / 3 == two
    combo3 = (one + two + three) / 3 == three

    # to calculate the midlde card
    middle_card = (one + two + three) / 3

    # to make sure that the cards are of the same type i.e Clubs,Diamonds,Hearts,Spades
    if 12 < middle_card < 15 or 25 < middle_card < 28 or 38 < middle_card < 41:
        return False
    else:
        pass

    # for Clubs
    if one / 13 <= 1 and two / 13 <= 1 and three / 13 <= 1:
        if combo1 or combo2 or combo3:
            return True
        else:
            return False

    # for Diamonds
    elif (one / 13 <= 2 and one >= 14) and (two / 13 <= 2 and two >= 14) and (three / 13 <= 2 and three >= 14):
        if combo1 or combo2 or combo3:
            return True
        else:
            return False

    # for Hearts
    elif (one / 13 <= 3 and one >= 27) and (two / 13 <= 3 and two >= 27) and (three / 13 <= 3 and three >= 27):
        if combo1 or combo2 or combo3:
            return True
        else:
            return False

    # for Spades
    elif (one / 13 <= 4 and one >= 40) and (two / 13 <= 4 and two >= 40) and (three / 13 <= 4 and three >= 40):
        if combo1 or combo2 or combo3:
            return True
        else:
            return False

    else:
        return False


def three_of_a_kind(one, two, three):
    """return True if all the cards are of the same rank"""

    # same rank cards have a difference which is a multiple of 13
    combo1 = abs(one-two) % 13 == 0
    combo2 = abs(two-three) % 13 == 0

    if combo1 and combo2:
        return True

    return False


def straight(one, two, three):
    """ Returns True if three cards are in sequence"""

    if straight_flush(one, two, three):
        return False

    # if two contigous suited cards and one different kind card in sequence where the lone card is smaller
    if (abs(one - two) % 12 == 0 or abs(one - three) % 12 == 0 or abs(two - three) % 12 == 0):
        return True

    # if two contigous suited cards and one different kind card in sequence where the lone card is larger
    if (abs(one - two) % 14 == 0 or abs(one - three) % 14 == 0 or abs(two - three) % 14 == 0):
        return True

    # if all three are in a series but of different kinds
    if (abs(one - two) % 14 == 0 or abs(one-three) % 14 == 0) and (abs(two-three) % 14 == 0):
        return True

    # to make the code more cleaner the last IF logic is saved in three variables because the code
    # is lenghty owing to the fact that the difference increases as the difference in the Kinds increase
    # and due to limition of not using loops the code is repetitive
    diff12 = abs(one - two) == 12 or abs(one -
                                         three) == 12 or abs(two - three) == 12
    diff25 = abs(one - two) == 25 or abs(one -
                                         three) == 25 or abs(two - three) == 25
    diff40 = abs(one - two) == 40 or abs(one -
                                         three) == 40 or abs(two - three) == 40

    # if the central card is of a different kind and the same kind cards are seperated
    if (abs(one - two) == 2 or abs(one - three) == 2 or abs(two - three) == 2) and (diff12 or diff25 or diff40):
        return True

    return False


def flush(one, two, three):
    """Returns True if all cards are of the same kind"""

    # demaracation of boundries
    clubs = one <= 13 and two <= 13 and three <= 13

    diamonds = 13 < one <= 26 and 13 < two <= 26 and 13 < three <= 26

    hearts = 26 < one <= 39 and 26 < two <= 39 and 26 < three <= 39

    spades = 39 < one <= 52 and 39 < two <= 52 and 39 < three <= 52

    if clubs:
        return True
    elif diamonds:
        return True
    elif hearts:
        return True
    elif spades:
        return True

    return False


def pair(one, two, three):
    """ Returns True if ONLY two cards are of the same rank"""

    # different combinations that could result in a pair
    combo1 = abs(one-two) % 13 == 0
    combo2 = abs(two - three) % 13 == 0
    combo3 = abs(one-three) % 13 == 0

    # check to see if all are same or not
    if three_of_a_kind(one, two, three):
        return False

    if combo1:
        return True
    elif combo2:
        return True
    elif combo3:
        return True

    return False


def high_card(one, two, three):
    """Returns True if no other scenario satisfies the argument"""

    if straight_flush(one, two, three) or three_of_a_kind(one, two, three) or straight(one, two, three) or flush(one, two, three) or pair(one, two, three):
        return False

    return True
