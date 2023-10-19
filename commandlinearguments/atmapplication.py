# ATM application to display the values Check Balance , WithDraw , Deposit Cash, Deposit Check based on the the option
# passed in the command line arguments

import sys

# Initial balance
balance = 1000  


if len(sys.argv) != 3:
    print("Usage: python atm.py <action> <amount>")
    sys.exit(1)

action = sys.argv[1]
amount = float(sys.argv[2])

if action == "check_balance":
    print(f"Your balance is: ${balance}")
elif action == "withdraw":
    if amount > 0 and amount <= balance:
        balance -= amount
        print(f"Withdrew ${amount}. Your new balance is: ${balance}")
    else:
        print("Invalid withdrawal amount or insufficient funds.")
elif action == "deposit_cash":
    if amount > 0:
        balance += amount
        print(f"Deposited ${amount} in cash. Your new balance is: ${balance}")
    else:
        print("Invalid deposit amount.")
elif action == "deposit_check":
    if amount > 0:
        balance += amount
        print(f"Deposited a check of ${amount}. Your new balance is: ${balance}")
    else:
        print("Invalid deposit amount.")
else:
    print("Invalid action. Please use one of the following: check_balance, withdraw, deposit_cash, deposit_check")


