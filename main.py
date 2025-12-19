user_data = [  # Nested List,["Account Number","User PIN","Balance","Name","is Admin"]
    ["101", "1111", 4000, "Ahmed", False],
    ["102", "2222", 2000, "AbdelRahman", True],
    ["103", "3333", 2000, "Zeyad", False],
    ["104", "4444", 2000, "Moaz", True],
    ["105", "5555", 3000, "Mohamed", False],
]


def login():  # take account number and pin as input from user
    account_num = input("Enter your account number: ")
    pin = input("enter your PIN: ")
    for current_user in user_data:
        if current_user[0] == account_num and current_user[1] == pin:
            print(f"Welcome Back. {current_user[3]}")
            return current_user
    print("Invalid account number or PIN")
    return None


def financial(current_user):  # Withdraw and Deposit
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Transfer")
    print("4. Check Balance")
    choice = input("Select:")

    if choice == "1":
        amount = float(input("Enter a amount to Deposit: "))
        current_user[2] += amount
        print(f"New Balance: {current_user[2]}")

    elif choice == "2":
        amount = float(input("Enter amount to Withdraw: "))

        if amount <= current_user[2]:
            current_user[2] -= amount
            print(f"Withdrawal of {amount} successful. Remaining: {current_user[2]}")
        else:
            print("No enough balance!")
    elif choice == "3":
        target_account = input("Enter the account number want to transfer to: ")
        amount = float(input("Enter amount to Transfer: "))
        for user in user_data:
            if target_account == user[0]:
                if amount <= current_user[2]:
                    current_user[2] -= amount
                    user[2] += amount
                    print(f"Transfer of {amount} to {user[3]} successful. Your Remaining Balance: {current_user[2]}")
                else:
                    print("No enough balance!")

    elif choice == "4":
        print(f"Your Balance is: {current_user[2]}")
        

def export_user(current_user):
    with open("user_ATM_account", "w") as file:
        file.write("account num, name, balance")
        file.write(f"{current_user[0]},{current_user[3]},{current_user[2]}")


def log_action(acc_num, action, amount):
    with open ("receipt.txt", "a") as file:
        file.write(f"Acc: {acc_num} has {action} with the amount: {str(amount)}")

def change_pin(current_user):
    new_pin = input("enter the new pin: ")
    confirm_pin = input("confirm the new pin: ")
    if new_pin == confirm_pin:
        current_user[1] = new_pin
        print(f"the new pin is: {current_user[1]}")
    else:
        print("the pin doesn't match")


def maxiumim_withdraw(current_user, amount):
    if amount < 5000:
        return
    else:
        print("the max limit is 5000")

def export_all_users():
    with open("all_users_accounts","w") as file:
        file.write("account num, name, balance")
        for user in user_data:
            file.write(f"{user[0]},{user[3]},{user[2]}")



def admin(current_user):  # Add users and Manage theres pin and balance
    if current_user[4] == False:
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
            if user_change_pin == user[0]:
                user_new_pin = input("enter your new pin: ")
                user[1] = user_new_pin
                print(f"the new pin is: {user_new_pin} ")
                found = True
                break
        if not found:
            print("error: user not found")
    elif admin_choice == "3":
        user_change_balance = input("enter the user's account number: ")
        found = False
        for user in user_data:
            if user_change_balance == user[0]:
                user_new_balance = float(input("enter your balance "))
                user[2] = user_new_balance
                print(f"your new balance is: {user_new_balance}")
                found = True
                break
        if not found:
            print("error: user not found")


def main():  # Run Code all in one
    while True:
        active_user = login()

        if active_user:
            if active_user[4] == True:
                admin(active_user)

            else:
                financial(active_user)


main()
