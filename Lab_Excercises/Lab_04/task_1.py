# Write a Program that takes any string input from the user and interchanges the first and second
# half of the string with each other. For example, the input is 1000 and the program outputs 0010.
# Make sure your program works on any string and not just the example above.

string = input("Please enter a string")

str1 = ""

count = len(string)
while count > len(string)//2:
    count -= 1
    print(string[count])
    str1 = str1 + string[count]

count = 0
while count < len(string) // 2:
    print(string[count])
    str1 = str1 + string[count]
    count += 1

print(str1)

rep_str = input("Please enter the string to be modified: ")
index = int(input("please enter the place of the character to be replaced: "))
sub_str = input("Please input the string you want to add at the desired index: ")
print(rep_str[0:index]+sub_str+rep_str[index+1:])
