import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 4,
    "B": 6,
    "C": 6,
    "D": 8
}
symbols_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        all_symbols.extend([symbol] * symbol_count)

    columns = []

    if random.random() < 0.15:
        rigged_symbol = random.choice(list(symbols.keys()))
        for _ in range(cols):
            column = []
            for row in range(rows):
                if row == 1:
                    column.append(rigged_symbol)
                else:
                    value = random.choice(all_symbols)
                    column.append(value)
            columns.append(column)
        return columns

    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns




def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please Enter a number. ")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please Enter a number. ")
    return lines

def get_bet():
    while True:
        amount = input("How much would you like to bet on each lines? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between.${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please Enter a number. ")
    return amount

def spin(balance, spin_count):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet on that amount, your current balance is: ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbols_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines if winning_lines else "none")
    return winnings - total_bet


def main():
    balance = deposit()
    spin_count = 0
    while True:
        print(f"current balance is ${balance}")
        answer = input("Press enter to play (s to stop).")
        if answer == "s":
            break

        spin_count += 1
        balance += spin(balance, spin_count)
    print(f"You left with ${balance}")

main()