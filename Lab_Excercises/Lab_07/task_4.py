
account_balance = 15000.00
user_input = ""
total_cash_withdrawn = 0.0
bank_charges = 0.0


def menu():
    user_input = input("""
        1) Enter 'check' if you want to check your balance.\n
        2) Enter 'withdraw' if you want to make a cash withdrawal.\n
        3) Enter 'quit' if you want to end transactions and quit the program\n\n""")

    return user_input


while user_input != "quit":
    user_input = menu()

    if user_input.lower().strip() == "check":
        print(f"Your account balance is: Rs. {account_balance}")
        pass
    if user_input.lower().strip() == "withdraw":
        withdraw_amount = float(
            input("Enter the amount you want to Withdraw: "))
        if (withdraw_amount % 500 == 0) and (withdraw_amount >= 500) and (withdraw_amount + 18.75 < account_balance):
            print(
                f"\033[1;92mWithdrawal of Rs. {withdraw_amount} Successful.\033[0m\n")
            total_cash_withdrawn += withdraw_amount
            bank_charges += 18.75

        elif (withdraw_amount + 18.75 > account_balance):
            print("\033[1;31m!!!Insufficient Balance!!!\033[0m")
            user_input = menu()

        else:
            print("\033[1;31m!!!Only enter in multiples of 500!!!\033[0m")

    if user_input.lower().strip() == "quit":
        break


final_balance = account_balance - total_cash_withdrawn - bank_charges

print(f"Previous Balance: {' '*20}Rs. {format(account_balance, '.2f')}")
print(
    f"Total Cash Withdrawn: {' '*16}Rs. {format(total_cash_withdrawn,  '.2f')}")
print(f"Total Bank Charges: {' '*18}Rs. {format(bank_charges, '.2f')}")
print(f"Remaining Balance: {' '*19}Rs. {format(final_balance, '.2f')}")
print(f"Interest Earned: {' '*21}Rs. {format(final_balance*0.03, '.2f')}")
print(
    f"New Balance after Interest: {' '*10}Rs. {format(final_balance*1.03, '.2f')} ")
