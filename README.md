# 🏦 Alala Bank Management System

A **Python-based Command Line Interface (CLI) banking application** that simulates core banking operations such as authentication, transactions, and administrative management.
The system features **persistent data storage using JSON**, ensuring user data remains intact across sessions.

---

## 🚀 Features

### 👤 For Users

* 🔐 **Secure Login**
  Access accounts using a unique **account number** and **PIN**.
* 💰 **Deposit & Withdraw**
  Safely update account balances with proper input validation.
* 🔄 **Funds Transfer**
  Transfer money to other existing accounts within the system.
* 📊 **Balance Inquiry**
  Check your current balance at any time.

---

### 🛠️ For Administrators

* ➕ **Add New Users**
  Create new bank accounts with custom details.
* 🔑 **Manage PINs**
  Reset or change any user’s PIN.
* ⚖️ **Manage Balances**
  Manually adjust user balances when required.
* 📋 **System Overview**
  View all registered users and their account details.

---

## 💡 Technical Highlights

* 💾 **Data Persistence**
  All user data is saved to `user_data.json`, so information is not lost when the program exits.
* 🖥️ **Cross-Platform UI**
  Automatically clears the terminal on:

  * Windows → `cls`
  * Linux/macOS → `clear`

---

## 🛠️ How to Run

1. Ensure **Python 3.x** is installed on your system.
2. Download or clone this repository.
3. Navigate to the project directory.
4. Run the program from your terminal:

```bash
python main.py
```

---

## 📖 Code Explanation

### 1️⃣ Data Structure & Storage

The system uses a **2D list (list of lists)** to store user data.
Each user profile follows a fixed index mapping for clarity:

| Index | Description                     |
| ----: | ------------------------------- |
|     0 | Account Number                  |
|     1 | PIN                             |
|     2 | Balance                         |
|     3 | Name                            |
|     4 | Admin Status (`True` / `False`) |

To maintain persistence, the program uses Python’s built-in `json` module:

* **`load_user_data()`**
  Runs at startup. Loads data from `user_data.json` (if it exists) and overwrites the default dataset.
* **`save_user_data()`**
  Runs after every successful transaction or update to keep data synchronized.

---

### 2️⃣ Authentication Logic (Login)

The `login()` function:

* Iterates through the `user_data` list.
* Compares user input with stored account numbers and PINs.
* Returns the matching user profile if found, otherwise returns `None`.

---

### 3️⃣ Role-Based Access Control (RBAC)

After login, the system checks the **admin status** (index `4`):

* ✅ `True` → Redirects to `admin_menu()`
* ❌ `False` → Redirects to `financial_menu()`

This ensures users only access features appropriate to their role.

---

### 4️⃣ Transaction Logic

* ✔️ **Validation**
  Withdrawals and transfers verify:

  * Amount is positive
  * User has sufficient balance
* 🔁 **Transfer Logic**

  * Searches for the target account
  * Deducts from sender and credits receiver
  * Saves changes immediately using `save_user_data()`

---

### 5️⃣ Admin Capabilities (CRUD Operations)

Admins can perform essential management tasks:

* ➕ **Add User**
  Prevents duplicate account numbers.
* 🔑 **Manage PIN / Balance**
  Updates specific users by searching for their account number.
* 📖 **View Users**
  Displays all registered users and account details.

---

### 6️⃣ User Experience (UX)

The `clear()` function uses the `os` module to detect the operating system and clear the terminal screen.
This provides a **clean, professional CLI experience** instead of cluttered scrolling output.

---

## 🌟 Summary

The **Alala Bank Management System** is a simple yet robust CLI banking application that demonstrates:

* Authentication & RBAC
* Transaction safety & validation
* Persistent storage with JSON
* Clean, user-friendly terminal interaction

Perfect for **learning Python fundamentals**, **CLI application design**, and **basic data persistence concepts** 🚀
