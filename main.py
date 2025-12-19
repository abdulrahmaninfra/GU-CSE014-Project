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

def login():  # take account number and pin as input from user
    account_num = input("Enter your account number: ")
    pin = input("enter your PIN: ")
    for current_user in user_data:
        if current_user[acc_number] == account_num and current_user[user_pin] == pin:
            print(f"Welcome Back. {current_user[name]}")
            return current_user
    print("Invalid account number or PIN")
    return None

def deposit(current_user):  # Deposit Function
        amount = float(input("Enter a amount to Deposit: "))
        if amount <= 0:
            print("Invalid amount. Please enter a positive value.")
            return
        current_user[balance] += amount
        print(f"New Balance: {current_user[balance]}")
        
def withdraw(current_user):  # Withdraw Function
        amount = float(input("Enter amount to Withdraw: "))
        if amount <= 0:
            print("Invalid amount. Please enter a positive value.")
            return
        if amount <= current_user[balance]:
            current_user[balance] -= amount
            print(f"Withdrawal of {amount} successful. Remaining: {current_user[balance]}")
        else:
            print("No enough balance!")

def transfer(current_user):  # Transfer Function
        target_account = input("Enter the account number want to transfer to: ")
        amount = float(input("Enter amount to Transfer: "))
        if amount <= 0:
            print("Invalid amount. Please enter a positive value.")
            return
        for user in user_data:
            if target_account == user[acc_number]:
                if amount <= current_user[balance]:
                    current_user[balance] -= amount
                    user[balance] += amount
                    print(f"Transfer of {amount} to {user[name]} successful. Your Remaining Balance: {current_user[balance]}")
                else:
                    print("No enough balance!")

def check_balance(current_user):  # Check Balance Function
        print(f"Your current balance is: {current_user[balance]}")

def financial(current_user):  # Combine each of the following functions for financial operations (Deposit, Withdraw, Transfer, Check Balance)
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Transfer")
    print("4. Check Balance")
    choice = input("Select:")

    if choice == "1":
        deposit(current_user)
    elif choice == "2":
        withdraw(current_user)
    elif choice == "3":
        transfer(current_user)
    elif choice == "4":
        check_balance(current_user)


def admin(current_user):  # Add users and Manage theres pin and balance
    if current_user[is_admin] == False:
        print("Access Denied: Admin privileges required.")
        return
    print("1. Add user")
    print("2. manage pin")
    print("3. manage balance")

    admin_choice = input("enter your choice:")

    if admin_choice == "1":
        new_user_account_number = input("the new account number: ")
        new_user_pin = input("enter your pin: ")
        new_user_balance = float(input("their balance: "))
        new_user_name = input("enter their name: ")
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

    elif admin_choice == "2":
        user_change_pin = input("enter the user's account number: ")
        found = False
        for user in user_data:
            if user_change_pin == user[acc_number]:
                user_new_pin = input("enter your new pin: ")
                user[user_pin] = user_new_pin
                print(f"the new pin is: {user_new_pin} ")
                found = True
                break
        if not found:
            print("error: user not found")
    elif admin_choice == "3":
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


def main():  # Run Code all in one
    while True:
        active_user = login()

        if active_user:
            if active_user[is_admin] == True:
                admin(active_user)
    
            else:
                financial(active_user)


main()
