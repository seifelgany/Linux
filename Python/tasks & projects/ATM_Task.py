# Initialize the ATM machine with a dictionary
atm = {
    'balance': 1000,
    'transactions': []
}

# Function to check balance
def check_balance():
    print("Your current balance is: ${}".format(atm['balance']))

# Function to deposit money
def deposit_money(amount):
    atm['balance'] += amount
    atm['transactions'].append(('deposit', amount))
    print("${} has been deposited to your account.".format(amount))

# Function to withdraw money
def withdraw_money(amount):
    if amount > atm['balance']:
        print("Insufficient funds.")
    else:
        atm['balance'] -= amount
        atm['transactions'].append(('withdraw', amount))
        print("${} has been withdrawn from your account.".format(amount))

# Function to display transaction history
def transaction_history():
    print("Transaction History:")
    for transaction in atm['transactions']:
        print("{}: ${}".format(transaction[0], transaction[1]))

# Main program loop
while True:
    print("\nWelcome to the ATM Machine\n")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Exit")
    choice = input("\nEnter your choice: ")
    
    if choice == '1':
        check_balance()
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        deposit_money(amount)
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        withdraw_money(amount)
    elif choice == '4':
        transaction_history()
    elif choice == '5':
        print("\nThank you for using the ATM Machine. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
