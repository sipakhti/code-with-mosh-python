import math as m


def grader(subject_marks, total_marks=150):
    if 50 <= ((subject_marks * 100) / total_marks) < 60:
        return "E"
    if 60 <= ((subject_marks * 100) / total_marks) < 70:
        return "D"
    if 70 <= ((subject_marks * 100) / total_marks) < 80:
        return "C"
    if 80 <= ((subject_marks * 100) / total_marks) < 90:
        return "B"
    if 90 <= ((subject_marks * 100) / total_marks):
        return "A"
    return "F"


def asec(*numbers):
    temp_list = []
    for num in numbers:
        for digit in num:
            temp_list.append(int(digit))
    temp_list.sort()
    print(*temp_list)


def avg(numbers):
    average = 0
    for x in numbers:
        average += x
    return average / len(numbers)


def lowest_highest(iterable):
    """ Returns the lowest and highest element of an iterable (list, tuple, array)
        in a Tuple
    """
    lowest = 0
    highest = 0
    for element in iterable:
        if element > highest:
            highest = element
        if element < lowest:
            lowest = element
    return lowest, highest


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


def count_occurances(iterable: "Iterable", element=""):

    num_freq = {}
    for num in iterable:
        if num.lower() in num_freq:
            num_freq[num.lower()] += 1
        else:
            num_freq[num.lower()] = 1

    try:
        if element != "":
            return element, num_freq[element.lower()]
    except KeyError:
        return element, 0

    sorted_num_freq = sorted(
        num_freq.items(), key=lambda kv: kv[1], reverse=True)

    return sorted_num_freq[0]


def bar_grapher(num_bars: int, graph_range: int, height: list, asdata=True, placeholder="X"):
    """Returns a nested list as a 2D bar graph for manipulation
       or prints it on the screen if asdata=False
       by default it returns a 2D list.
       Param placeholder is "X" by default and will use "X" as 
       the bar body, however it could be given any argument to be placed
       instead of "X"
    """
    if graph_range >= 10:
        placeholder += " "

    print("\n\n")
    graph_range += 1  # so that i can add the column height aboce the bars to help readability of large graphs
    bar_graph = [[" " for j in range(num_bars)] for i in range(graph_range)]

    for i in range(num_bars):
        error = True
        while error:
            error = False

            try:
                for j in range(height[i]):
                    bar_graph[graph_range - 1 - j][i] = placeholder
            except IndexError:
                error = True
                return f"!!!Bar height cannot exceed {graph_range}, Index[{i}] Value: {height[i]}!!!"
            bar_graph[-1].insert(i, height[i])

    if asdata:
        return bar_graph
    else:
        for row in bar_graph:
            print(*row)


def power_funct(number: int or str, power: int or str):
    """Takes a number and its exponenent
        to calulate the answer"""
    number, power = int(number), int(power)
    if power == 1:
        return number

    return number * power_funct(number, power - 1)


def check_palindromicity(s=str):
    limit = len(s)
    count = 0
    for index in range(limit):
        if s[index] == s[limit - 1 - index]:
            count += 1

    return True if count == limit else False


def hi_temp(iterable: "of type int"):
    """ Takes a 2D list or array and returns a list containing
        the highest value in a row cooresponding to the row index
    """

    cities_max_temp = []
    max_temp = 0
    for row in iterable:
        for temprature in row:
            if temprature.isnumeric():
                if int(temprature) > max_temp:
                    max_temp = int(temprature)
        cities_max_temp.append(max_temp)
        max_temp = 0

    return cities_max_temp


def hailstone(number, step=1):
    if isinstance(number, str):
        number = int(number)
    # HAILSTONE SEQUENCE PRINTING
    newline = " "
    if step % 10 == 0:
        newline = f"[{step}]\n"
    print(number, end=f"{newline}")
    # RECURSION LIMITER
    if number == 1:
        print(f"\rSteps : {step} ")
        return 1
    # HAILSTONE SEQUENCE CALCULATION
    elif number % 2 == 1:
        number = number * 3 + 1
    elif number % 2 == 0:
        number = number // 2

    hailstone(number, step+1)


def factorial(number: int):
    for n in range(1, number):
        number *= n
    return number


def combination(n: int, r: int):
    if n < 0 or r < 0:
        raise ValueError(
            "\033[1;31m!!!Value of 'n' or 'r' cannot be less than '0'!!!\033[0m")
    if r > n:
        raise ValueError(
            "\033[1;31m!!!Value of 'r' cannot be bigger than value of 'n'!!!\033[0m")
    if r == 0 and n == 0:
        ncr = 0
    else:
        ncr = (factorial(n) / (factorial(r) * factorial(n - r)))

    return ncr


def permutation(n: int, r: int):
    if n < 0 or r < 0:
        raise ValueError(
            "\033[1;31m!!!Value of 'n' or 'r' cannot be less than '0'!!!\033[0m")
    if r > n:
        raise ValueError(
            "\033[1;31m!!!Value of 'r' cannot be bigger than value of 'n'!!!\033[0m")
    if r == 0 and n == 0:
        npr = 0
    else:
        npr = factorial(n) / factorial(n - r)

    return npr


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
        decany += 1 * pow(2, len(binary)-1)
    if binary[0] == "0":
        pass
    decany += bin_to_dec(binary[1:])
    return decany


def str_reverse(string: str = ...):
    temp_list = []
    for char in string:
        temp_list.append(char)

    return list_concat(temp_list)


def list_concat(items: str):
    """ concatenate list elements"""
    out = ""
    for element in items:
        out = out + element
    return out


def distance(x1: int, x2: int, y1: int, y2: int):
    return m.sqrt((pow((x2 - x1), 2) + pow((y2 - y1), 2)))


def midpoint(x1: int, x2: int, y1: int, y2: int):
    return (x1 + x2) / 2, (y1 + y2) / 2


def slope(x1: int, x2: int, y1: int, y2: int):
    if x1 == x2:
        raise ValueError("Vertical - Undefined Slope")
    return (y2 - y1) / (x2 - x1)


def to_json(filepath, obj):
    """saves the object in a file using JSON module"""

    from os import path
    import json

    overwrite = True
    # to make sure that user knows that he could overwrite existing data if present
    if path.exists(filepath):
        print(
            "the file {filepath} already exists\nproceeding will overwrtite the existing data")
        user_input = input("Press Y to continue or Press N to to stop: ")
        if user_input.lower() == "n":
            overwrite == False

    if overwrite:
        with open(filepath, "w") as f_obj:
            json.dump(obj, f_obj)
            print("Your file has be saved!")
            exit()
    elif overwrite:
        return None


def from_json(filepath):

    from json import load

    try:
        with open(filepath) as f_obj:
            variable = load(f_obj)
    except FileNotFoundError:
        print("The file you requested cannot be found at the specified place")
        exit()
    else:
        return variable
