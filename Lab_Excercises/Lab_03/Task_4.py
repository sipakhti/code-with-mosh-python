# Implement a program that directs a cashier how to give change. The program has two inputs: the
# amount due and the amount received from the customer.
# Display the dollars, quarters, dimes, nickels, and pennies that the customer should receive in
# return.
#  A dollar is worth 100 cents
#  A quarter is worth 25 cents
#  A dime is worth 10 cents
#  A nickel is worth 5 cents
#  A penny is worth 1 cent


recieved = float(input("Received Amount: "))
due = float(input("Amount Due: "))


dollar = int(due)
buffer = (due - int(due))*100
quarter = buffer // 25
dime = (buffer % 25) // 10
nickel = (buffer % 25 % 10) // 5
penny = (buffer % 20 % 10 % 5) // 1

dic = {25: "quarter", 10: "dime", 5: "nickel", 1: "penny"}

print(int(due), "DOLLARS")
for number in dic:
    print(int(buffer // number), dic[number])
    buffer = buffer % number
