user_data = [ # Nested List,["Account Number","User PIN","Balance","Name"]
    ["101","1111",4000,"Ahmed",False],
    ["102","2222",2000,"AbdelRahman",True],
    ["103","3333",2000,"Zeyad",False],
    ["104","4444",2000,"Moaz",True],
    ["105","5555",3000,"Mohamed",False],
]


def login(): # take account number and pin as input from user
    account_num = input("Enter your account number")
    pin = input("enter your PIN: ")
    for user in user_data:
        if user[0] == account_num and user[1] == pin:
            print(f"Welcome Back. {user[3]}")
            return user
    print("Invalid account number or PIN")
    return None

def financial(current_user): # Withdraw and Deposit
    print("1. Deposit")
    print("2. Withdraw")
    choice = input("Select:")
    if choice == "1":
        amount= float(input("Enter a amount to Deposit: "))
        current_user[2] += amount
        print(f"New Balance: {current_user[2]}")

    elif choice == "2":
        amount = float(input("Enter amount to Withdraw: "))

        if amount <= current_user[2]:
            current_user[2] -= amount
            print(f"Withdrawal of {amount} successful. Remaining: {current_user[2]}")
        else:
            print("No enough balance!")

def admin(current_user): # Add users and Manage theres pin and balance
    
        if current_user[4] == False:
            print("Access Denied: Admin privileges required.")
            return
        print("1. Add user")
        print("2. manage pin")
        print("3. manage balance")

        admin_choice = input("enter your choice:")

        if admin_choice == "1":
            new_user_account_number= input("the new account number: ")
            new_user_pin = input("enter your pin: ")
            new_user_balance = float(input("their balance: "))
            new_user_name = input("enter their name: ")
            user_data.append([new_user_account_number , new_user_pin , new_user_balance , new_user_name , False])
            print("User added successfully.")

        elif admin_choice == "2":
            user_change_pin= input("enter the user's account number: ")
            for user in user_data:
                if user_change_pin == user[0]:
                    user_new_pin = input("enter your new pin: ")
                    user[1] = user_new_pin
                    print(f"the new pin is: {user_new_pin} ")

        elif admin_choice == "3":
            user_change_balance= input("enter the user's account number: ")
            for user in user_data:
                if user_change_balance == user[0]:
                    user_new_balance = input("enter your balance ")
                    user[2] = user_new_balance
                    print(f"your new balance is: {user_new_balance}")

            else:
                print("invalid input")
                        
                


def main(): # Run Code all in one

    while True:
        print("\n--- SYSTEM RESTART ---")
        active_user = login()
        
        if active_user:

            if active_user[4] == True:
                admin(active_user)
                
            else:
                financial(active_user)
main()
