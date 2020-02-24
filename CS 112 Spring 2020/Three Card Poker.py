
def straight_flush(one, two, three):
    """Returns True if its a straight flush"""
    # three combination of cards (a,b,c), (b,a,c), (c,a,b)
    combo1 = (one + two + three) / 3 == one
    combo2 = (one + two + three) / 3 == two
    combo3 = (one + two + three) / 3 == three

    middle_card = (one + two + three) / 3

    # to make sure that the cards are of the same type i.e Clubs,Diamonds,Hearts,Spades
    if 12 < middle_card < 15 or 25 < middle_card < 28 or 38 < middle_card < 41:
        return False
    else:
        pass

    if three / 13 <= 1:
        if combo1 or combo2 or combo3:
            return True
        else:
            return False
    elif three / 13 <= 2 and one >= 14:
        if combo1 or combo2 or combo3:
            return True
        else:
            return False
    elif three / 13 <= 3 and one >= 27:
        if combo1 or combo2 or combo3:
            return True
        else:
            return False
    elif three / 13 <= 4 and one >= 40:
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

    # if cards are in sequence but all three are of different kind
    combo1 = (abs(one - two) % 14 == 0) or (abs(one - three) % 14 == 0)
    combo2 = (abs(two - three) % 14 == 0)

    combo3 = (abs(one - two) == 1 or abs(one - three) == 1) and (combo1 or combo2)
    combo4 = abs(two-three) == 1 and (combo1 or combo2)

    if combo1 and combo2:
        return True
    

    
    return False


def is_flush(one, two, three):
    pass


def is_pair(one, two, three):
    pass


def is_high_card(one, two, three):
    pass


for x in range(15):
    one, two, three = input("Enter three cards: ").split()
    print(straight(int(one), int(two), int(three)))
