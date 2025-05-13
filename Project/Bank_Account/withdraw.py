from show_balance import show_balance
def withdraw(balance,amount):
    #global balance
    if amount <= 0:
        print(" Withdrawal amount must be positive.")
    elif amount > balance:
        print(" Insufficient balance.")
    else:
        balance -= amount
        print(f"✅ Withdrawn: ${amount:.2f}")
        
    show_balance(balance)
    return balance