user_data = [ # Nested List,["Account Number","User PIN","Balance","Name"]
    ["101","1111",4000,"Ahmed"],
    ["102","2222",2000,"AbdelRahman"],
    ["103","3333",2000,"Zeyad"],
    ["104","4444",2000,"Moaz"],
    ["105","5555",3000,"Mohamed"],
]


def login(): # take account number and pin as input from user


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
