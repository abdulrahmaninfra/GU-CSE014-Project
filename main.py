user_data = [ # Nested List,["Account Number","User PIN","Balance","Name"]
    ["101","1111",4000,"Ahmed"],
    ["102","2222",2000,"AbdelRahman"],
    ["103","3333",2000,"Zeyad"],
    ["104","4444",2000,"Moaz"],
    ["105","5555",3000,"Mohamed"],
]

user_account_number = user[0]
user_pin = user[1]
user_balance = user[2]
user_name = user[3]

def login(): # take account number and pin as input from user
    account_num = input("Enter your account number")
    pin = input("enter your PIN: ")
    for user in user_data:
        if user_account_number == account_num and user_pin == pin:
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
