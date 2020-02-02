from collections import deque
from os import system
numbers = [3, 51, 2, 8, 6, 9, 48, 34]
numbers.sort(reverse=True)  # Will modify orignial list
print(numbers)

sorted(numbers)  # will not modify original list instead it will generate a new list

items = [
    ("Product1", 10),
    ("Product2", 150),
    ("Product3", 20),

]

items.sort()  # it wont work as the list is complicated for that we create a function that unpacks the tuple inside the list and return the value accourding to whic we want to sort (line 18)
print(items)


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)


# LAMBDA Function
# similar function as the code on line 18 - 21 but much much much cleaner and better
items.sort(key=lambda item: item[1])

# MAP() Function
# extract prices from the items list we can use the following code to create a new list of prices
prices = []
for item in items:
    prices.append(item[1])

print(prices)

# However this is muchb  cleaner and better approach than that of line 31 - 33
# map(x,y). the map function iterates through "y" and pass every element of "y" to "x" which is a function and the map function returns an iterable which can be converted to a list be LIST()
x = list(map(lambda item: item[1], items))
print(x)


# FILTER Function

filtered = list(filter(lambda item: item[1] >= 20, items))


# LIST Comprehensions
prices = list(map(lambda item: item[1], items))
# better than the code on the above line but similar in effect
prices = [item[1] for item in items]

filtered = list(filter(lambda item: item[1] >= 20, items))
# another way of doing the same thing via LIST comprehension
filtered = [item for item in items if item[1] >= 20]


# ZIP Function

list1 = [1, 2, 3]
list2 = [10, 20, 30]

[(1, 10), (2, 20), (3, 30)]

print(list(zip("abc", list1, list2)))

# STACK... LIFO(Last In - First Out) behaviour is exhibited by stack
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
print("Redirect", browsing_session[-1])

if not browsing_session:
    print("disable back button")


# QUEUES... FIFO(First In - First Out)
from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
