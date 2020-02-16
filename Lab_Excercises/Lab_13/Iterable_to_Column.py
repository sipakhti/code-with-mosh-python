
def print_column(list1: "iterable", list2=[], col1="column 1", col2="column 2", dupes: bool = False):
    """ Outputs iterable in a verticle fashion.
        if a second list is provided with matching length and having a relationship
        between the corresponding values of both lists
        the function creates a second column to display them side by side
        if you want to get the length of individual elements then change dupes=True
        in case of dupes=True then the second argument will not give any results
    """
    if dupes:
        list2 = seq_count(list1)

    if bool(list2):
        print(
            f"{col1}{' '*(len(col1)+len(max(list1))-2)}{' '*( len(max(list1)))}{col2}\n")
        for x in range(len(list1)):
            print(
                f"{list1[x]}{' '*(len(col1)+len(max(list1)))}{' '*( len(max(list1)) - len(list1[x])  + len(max(list1)))}{list2[x]} ")
    else:
        print(f"{col1}{' '*3}{' '*len(max(list1))}INDEX\n")
        for x in range(len(list1)):
            print(
                f"{list1[x]} {'>'*5}{' '*(( len(max(list1))-len(list1[x]) ) + len(max(list1)))}{x} ")


def seq_count(iterable: "iterable"):
    """ Calculates length of individual elements of any iterbale(list, tuple, array)
        and returns a list whose indexes correspond with the original elements index
    """
    from array import array
    length = array("i")
    count = 0
    for item in iterable:
        count = 0
        for element in item:
            count += 1
        length.append(count)

    return length


def replace_element(iterable,  substitute: "substitute value", string: str = "existing value", index=None, dontcare: bool = False):
    """replaces the element that matches the parameter or index, with the given value
       raises ValueError if datatpye of string to substitute doesnt match the already
       existing datatype. change dontcare=True to bypass the error

       substitute = THE VALUE YOU WANT TO ADD INSTEAD
       string = THE EXISTING VALUE YOU WANT TO REPLACE
       index = IF YOU WANT TO REPLACE THE VALUE AT A SPECIFIC INDEX
       dontcare = True, if you want to replace the values which have different data types
    """

    if dontcare == False:
        if isinstance(substitute, str) and not isinstance(iterable[0], str):
            raise ValueError(
                "iterable and string have datatype mismatch\n set argument 'dontcare' to True if you want to do this operation")

# IF USER WANTS TO CHANGE THE ELEMENT BUT DONT INPUT THE INDEX
    if index == None:
        for i in range(len(iterable)):
            if iterable[i].lower() == string.lower():
                iterable[i] = substitute

# IF USER WANTS TO CHANGE THE ELEMENT AT A SPECIFIC INDEX
    if index != None:
        iterable[index] = substitute

    return iterable


user_input = input("Enter a string:\n")
user_list = user_input.split()

print_column(user_list, col1="words", col2="count", dupes=True)

user_input = input("Enter the word you want to replace: ")
user_sub = input("Enter the word you want to add: ")

print_column(replace_element(user_list, user_sub, user_input),
             col1="words", col2="count", dupes=True)
