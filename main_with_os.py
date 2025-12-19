import os

user_data = [  # Nested List,["Account Number","User PIN","Balance","Name","is Admin"]
    ["101", "1111", 4000, "Ahmed", False],
    ["102", "2222", 2000, "AbdelRahman", True],
    ["103", "3333", 2000, "Zeyad", False],
    ["104", "4444", 2000, "Moaz", True],
    ["105", "5555", 3000, "Mohamed", False],
]


acc_number = 0
user_pin = 1
balance = 2
name = 3
is_admin = 4

def clear(): # https://docs.python.org/3/library/os.html
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def login():  # take account number and pin as input from user
    account_num = input("Enter your account number: ").strip()
    pin = input("enter your PIN: ").strip()
    for current_user in user_data:
        if current_user[acc_number] == account_num and current_user[user_pin] == pin:
            return current_user
    print("Invalid account number or PIN")
    return None

def deposit(current_user):  # Deposit Function
        amount = float(input("Enter a amount to Deposit: ").strip())
        if amount <= 0:
            print("\nInvalid amount. Please enter a positive value.")
            return
        current_user[balance] += amount
        print(f"\nNew Balance: {current_user[balance]}")
        
def withdraw(current_user):  # Withdraw Function
        amount = float(input("Enter amount to Withdraw: ").strip())
        if amount <= 0:
            print("\nInvalid amount. Please enter a positive value.")
            return
        if amount <= current_user[balance]:
            current_user[balance] -= amount
            print(f"\nWithdrawal of {amount} successful. Remaining: {current_user[balance]}")
        else:
            print("No enough balance!")

def transfer(current_user):  # Transfer Function
        target_account = input("Enter the account number want to transfer to: ").strip()
        amount = float(input("Enter amount to Transfer: ").strip())
        if amount <= 0:
            print("Invalid amount. Please enter a positive value.")
            return
        for user in user_data:
            if target_account == user[acc_number]:
                if amount <= current_user[balance]:
                    current_user[balance] -= amount
                    user[balance] += amount
                    clear()
                    print(f"\nTransfer of {amount} to {user[name]} successful. Your Remaining Balance: {current_user[balance]}")
                else:
                    clear()
                    print("No enough balance!")

def check_balance(current_user):  # Check Balance Function
        print(f"\nYour current balance is: {current_user[balance]}")

def financial_menu(current_user):  # Combine each of the following functions for financial operations (Deposit, Withdraw, Transfer, Check Balance)
    while True:
        clear()
        print(f"{'='*20}")
        print(f"MAIN MENU: {current_user[name]}")
        print(f"{'='*20}")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("\nChoose an option: ").strip()
        if choice == "1":
            deposit(current_user)
        elif choice == "2":
            withdraw(current_user)
        elif choice == "3":
            transfer(current_user)
        elif choice == "4":
            check_balance(current_user)
        elif choice == "5":
            print("you have exited.")
            break
        else:
            print("Invalid choice.")
            return
        input("Press Enter to continue...")
def add_user():  # Add User Function
    new_user_account_number = input("\nthe new account number: ").strip()
    new_user_pin = input("\nenter your pin: ").strip()
    new_user_balance = float(input("\ntheir balance: ").strip())
    new_user_name = input("\nenter their name: ").strip()
    user_data.append(
        [
            new_user_account_number,
            new_user_pin,
            new_user_balance,
            new_user_name,
            False,
        ]
    )
    print("User added successfully.")

def manage_pin():  # Manage Pin 
    user_change_pin = input("\nenter the user's account number: ")
    found = False
    for user in user_data:
        if user_change_pin == user[acc_number]:
            user_new_pin = input("\nenter your new pin: ")
            user[user_pin] = user_new_pin
            print(f"\nThe new pin is: {user_new_pin} ")
            found = True
            break
    if not found:
        print("error: user not found")

def manage_balance():  # Manage Balance
        user_change_balance = input("enter the user's account number: ")
        found = False
        for user in user_data:
            if user_change_balance == user[acc_number]:
                user_new_balance = float(input("enter your balance "))
                user[balance] = user_new_balance
                print(f"your new balance is: {user_new_balance}")
                found = True
                break
        if not found:
            print("error: user not found")

def admin_menu(current_user):  # Add users and Manage theres pin and 
    while True:
        clear()
        print(f"{'='*20}")
        print(f"ADMIN MENU: {current_user[name]}")
        print(f"{'='*20}")
        print("1. Add user")
        print("2. Manage pin")
        print("3. Manage balance")
        print("4. Exit")

        admin_choice = input("Enter your choice: ").strip()
        if admin_choice == "1":
            add_user()
        elif admin_choice == "2":
            manage_pin()
        elif admin_choice == "3":
            manage_balance()
        elif admin_choice == "4":
            print("you have exited.")
            clear()
            break
        else:
            print("Invalid choice.")
            return


def main():
    while True:
        clear()
        print(f"{'='*26}")
        print("  WELCOME TO GALALA BANK")
        print(f"{'='*26}")
        active_user = login()

        if active_user:
            if active_user[is_admin]:
                admin_menu(active_user)
            else:
                financial_menu(active_user)
        else:
            retry = input("Try again? (y/n): ").lower().strip()
            if retry != 'y':
                print("System shutting down. Goodbye!")
                break

main()
