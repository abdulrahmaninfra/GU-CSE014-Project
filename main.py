user_data = [ # Nested List,["Account Number","User PIN","Balance","Name"]
    ["101","1111",4000,"Ahmed",False],
    ["102","2222",2000,"AbdelRahman",True],
    ["103","3333",2000,"Zeyad",False],
    ["104","4444",2000,"Moaz",True],
    ["105","5555",3000,"Mohamed",False]
]

def login(): # take account number and pin as input from user
    account_num = input("Enter your account number")
    pin = input("enter your PIN: ")
    for user in user_data:
        if user[0] == account_num and user[1] == pin:
            print(f"Welcome Back. {user[3]}")
            return user
        else:
            print("Invalid account number or PIN")
            return None

def financial(current_user): # Withdraw and Deposit
    print("1. Deposit")
    print("2. Withdraw")
    choice = input("Select:")
    if choice == "1":
        amount= float(input("Enter a amount to Deposit: "))
        current_user[2] += amount
    elif choice == "2":
        if amount <= current_user[2]:
            current_user[2] -= amount
            print(f"Withdrawal of {amount} successful. Remaining: {current_user[2]}")
        else:
            print("No enough balance!")

def ShowBalance_ChangePIN(current_user): # Show User Balance
    print("1. Show Balance")
    print("2. Change PIN")
    choice = input("Select:")
    if choice == "1":
        print(f"Your Balance is {current_user[2]}")
    elif choice == "2":
        changed_pin = input("Please enter your new PIN: ")
        current_user[1] = changed_pin
        print("PIN Changed Successfully!!")
def admin():# Add users and Manage theres pin and balance
    for user in user_data:
        if user[4] == True:
            print("1. Add user")
            print("2. manage pin")
            print("3. manage balance")
            admin_choice = input("enter your choice:")
            if admin_choice == "1":
                new_user_account_number= input("the new account number: ")
                new_user_pin = input("enter your pin: ")
                new_user_balance = input("their balance: ")
                new_user_name = input("enter their name: ")
                user_data.append([new_user_account_number , new_user_pin , new_user_balance , new_user_name , False])
            elif admin_choice == "2":
                user_change_pin= input("enter the user's account number: ")
                for user in user_data:
                    if user_change_pin == user_data[0]:
                        user_new_pin = input("enter your new pin: ")
                        user_data.remove(1)
                        user_data.insert(1, user_new_pin)
            elif admin_choice == "3":
                user_change_balance= input("enter the user's account number: ")
                for user in user_data:
                    if user_change_balance == user_data[0]:
                        user_new_balance = input("enter your balance ")
                        user_data.remove(2)
                        new_balance = user_data.insert(2, user_new_balance)
                        print(f"your new balance is: {new_balance}")
            else:
                print("invalid input")
def main(): # Run Code all in one
