Galala Bank Management System

A Python-based Command Line Interface (CLI) banking application that supports user authentication, financial transactions, and administrative management with persistent data storage using JSON.
🚀 Features
For Users

    Secure Login: Access accounts using an account number and PIN.

    Deposit & Withdraw: Update account balance with input validation.

    Funds Transfer: Transfer money to other existing accounts within the system.

    Balance Inquiry: Check current funds at any time.

For Administrators

    Add New Users: Register new accounts with custom details.

    Manage PINs: Reset or change any user's PIN.

    Manage Balances: Manually adjust account balances.

    System Overview: View a list of all registered users and their details.

Technical Highlights

    Data Persistence: Saves all changes to a user_data.json file so data isn't lost when the program closes.

    Cross-Platform UI: Automatic terminal clearing for both Windows (cls) and Linux/macOS (clear).

🛠️ How to Run

    Ensure you have Python 3.x installed.

    Download the main.py file.

    Run the script via terminal:
    Bash

    python main.py

📖 Code Explanation
1. Data Structure & Storage

The system uses a 2D List (a list of lists) to store user information. Each inner list represents a user profile mapped by index constants for readability:

    0: Account Number

    1: PIN

    2: Balance

    3: Name

    4: Admin Status (Boolean)

To ensure data isn't lost, the program uses the json library:

    load_user_data(): Triggered at startup. It checks if user_data.json exists and overwrites the default user_data list with the stored file content.

    save_user_data(): Triggered after every successful transaction (deposit, transfer, etc.) to ensure the JSON file is always up to date.

2. Authentication Logic (login)

The login() function acts as a gatekeeper. It iterates through the user_data list and compares user input against stored values. If a match is found, it returns the specific user's list; otherwise, it returns None.
3. Role-Based Access Control (RBAC)

In the main() function, once a user is logged in, the system checks the is_admin index (index 4):

    If True: The user is directed to the admin_menu().

    If False: The user is directed to the financial_menu().

4. Transaction Logic

    Validation: Functions like withdraw and transfer check if the amount is positive and if the user has enough balance before proceeding.

    Transfer Logic: The system searches for the target_account. If found, it subtracts from the sender and adds to the receiver simultaneously, then calls save_user_data().

5. Admin Capabilities

The admin menu allows for CRUD (Create, Read, Update) operations.

    add_user: Includes a check to prevent duplicate account numbers.

    manage_pin/balance: Allows targeted updates to specific users by searching for their account number.

6. User Experience (UX)

The clear() function uses the os module to detect the operating system and clear the screen, making the CLI feel more like a professional application rather than a continuous scrolling text file.
