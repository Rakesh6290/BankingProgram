def show_balance():
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter the amount to deposit: "))
    if amount < 0:
        print("It is not a valid amount.")
    else:
        global balance
        balance += amount
        print(f"Deposited ${amount:.2f}")

def withdraw():
    amount = float(input("Enter the amount to withdraw: "))
    global balance
    if amount < 0:
        print("It is not a valid amount.")
    elif amount > balance:
        print("Insufficient funds.")
    else:
        balance -= amount
        print(f"Withdrew ${amount:.2f}")

def exit_program():
    global is_running
    is_running = False

balance = 0.0
is_running = True

while is_running:
    print("\n**Banking Program**")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        show_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        exit_program()
    else:
        print("This is not a valid choice.")

print("Thank you! Have a nice day!")
