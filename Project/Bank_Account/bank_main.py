from deposit import deposit
from show_balance import show_balance
from withdraw import withdraw


print("Welcome to the Python Bank")

# main.py
from deposit import deposit
from withdraw import withdraw
from show_balance import show_balance
#balance = 0.0
def main():
    balance = 0.0

    while True:
        print("Choose an action:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: $"))
            balance = deposit(balance, amount)

        elif choice == '2':
            amount = float(input("Enter amount to withdraw: $"))
            balance = withdraw(balance, amount)

        elif choice == '3':
            balance = show_balance(balance)

        elif choice == '4':
            print("👋 Thank you for banking with us!")
            break

        else:
            print("Invalid option. Please choose between 1 and 4.")

if __name__ == "__main__":
    main()
