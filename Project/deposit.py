from show_balance import show_balance
def deposit(balance,amount):
    #global balance
    if amount <= 0:
        print("❌ Deposit amount must be positive.")
    else:
        balance += amount
        print(f"✅ Deposited: ${amount:.2f}")
    show_balance(balance)
    return balance