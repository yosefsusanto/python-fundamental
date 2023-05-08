"""
MAX_LINE = 3
MIN_BET = 1
MAX_BET = 100

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("please enter the number.")

    return amount
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINE) +")?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINE:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("please enter the number.")

    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET :
                break
            else:
                print(f"Amount must be between ${MIN_BET} - {MAX_BET}.")
        else:
            print("please enter the number.")

    return amount
def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = bet * lines
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")



main()

"""

MAX_LINE = 3
MIN_BET = 1
MAX_BET = 100

def get_input(prompt, validator_func):
    while True:
        value = input(prompt)
        if validator_func(value):
            return int(value)

def validate_amount(amount, min_amount=1, max_amount=1000000):
    if not amount.isdigit():
        print("Please enter a valid amount.")
        return False
    amount = int(amount)
    if amount < min_amount or amount > max_amount:
        print(f"Amount must be between {min_amount} and {max_amount}.")
        return False
    return True

def deposit():
    return get_input("What would you like to deposit? $", lambda x: validate_amount(x, 1))

def get_number_of_lines():
    return get_input(f"Enter the number of lines to bet on (1-{MAX_LINE})?", lambda x: validate_amount(x, 1, MAX_LINE))

def get_bet():
    return get_input(f"What would you like to bet on each line? $", lambda x: validate_amount(x, MIN_BET, MAX_BET))

def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = bet * lines
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

main()
