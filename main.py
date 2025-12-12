user_data = [ # Nested List,["Account Number","User PIN","Balance","Name"]
    ["101","1111",4000,"Ahmed"],
    ["102","2222",2000,"AbdelRahman"],
    ["103","3333",2000,"Zeyad"],
    ["104","4444",2000,"Moaz"],
    ["105","5555",3000,"Mohamed"],
]
for users in user_data:
    Account_number = user_data[0]
    user_pin = user_data[1]
    user_balance = user_data[2]
    user_name = user_data[3]

def login(): # take account number and pin as input from user
    account_num = user_data [0][1] and user_data [1][1] and user_data[2][1] and user_data[3][1] and user_data[4][1]
    user_login = input("enter your account number: ")
    if user_login in account_num:
        return True
    return False

def financial(): # Withdraw and Deposit
    print("1. Deposit")
    print("2. Withdraw")
    choice = input("Select:")
    if choice == "1":
        amount= float(input("Enter a amount to Deposit: "))
        user[2] += amount
    elif choice == "2":
        if amount <= user[2]:
            user[2] -= amount
            print(f"Withdraw of {amount} Done Successfully")
        else:
            print("No enough balance!")

def ShowBalance_ChangePIN(): # Show User Balance
def admin(): # Add users and Manage theres pin and balance
def main(): # Run Code all in one
