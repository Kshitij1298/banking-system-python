Enterprise Banking Management System

A console-based Banking Management System built in Python, demonstrating core Object-Oriented Programming principles (Abstraction, Encapsulation, Inheritance, Polymorphism) combined with a MySQL database backend for persistent, secure data storage.

Overview

This system allows users to open a bank account (Savings or Current), authenticate with a secure PIN, check their balance, deposit and withdraw money, and view a complete transaction history — all backed by a real relational database.

Features

Open a new Savings or Current account
Secure PIN-based authentication required for every sensitive operation
Deposit and withdraw funds, with balance validation (no overdrawing allowed)
View a complete, timestamped transaction history
Input validation on account holder name and PIN before account creation
SQL injection protection via parameterized queries
Clean, modular architecture — data access, business logic, and UI kept fully separate
Tech Stack
Language: Python 3
Database: MySQL
Core Concepts: Object-Oriented Programming, Exception Handling, Factory Design Pattern
Libraries: abc (Abstract Base Classes), mysql-connector-python



Project Architecture
banking-system/
├── main.py               # Entry point — menu-driven CLI interface
├── bank_manager.py         # Business logic — account operations & authentication
├── banking_entities.py       # Class hierarchy — BankAccount, SavingsAccount, CurrentAccount
└── db_handler.py                # Data layer — MySQL connection & queries
File	Responsibility
main.py	Displays the menu and routes user input
bank_manager.py	Handles authentication and all account operations
banking_entities.py	Defines the account class hierarchy and validation rules
db_handler.py	Handles all MySQL database interactions


Class Design (OOP)
BankAccount (Abstract Base Class)
 ├── holder_name, pin → validated via @property setters
 ├── balance → read-only property (cannot be set directly from outside)
 ├── account_type → abstract property
 ├── get_details() → abstract method
 │
 ├── SavingsAccount
 └── CurrentAccount
Abstraction: BankAccount is an abstract class — it cannot be instantiated directly.
Encapsulation: balance has no public setter — it can only be changed through controlled deposit/withdraw logic, never set directly.
Inheritance: SavingsAccount and CurrentAccount both inherit shared validation and behavior from BankAccount.
Polymorphism: Each subclass implements get_details() and account_type independently.


Database Schema
sql

CREATE TABLE accounts (
    account_number INT AUTO_INCREMENT PRIMARY KEY,
    holder_name VARCHAR(100) NOT NULL,
    account_type VARCHAR(20) NOT NULL,
    pin CHAR(4) NOT NULL,
    balance DECIMAL(12,2) NOT NULL DEFAULT 0.00
);

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_number INT NOT NULL,
    transaction_type VARCHAR(20) NOT NULL,
    amount DECIMAL(12,2) NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_number) REFERENCES accounts(account_number)
);


Getting Started

Prerequisites
Python 3.8+
MySQL Server running locally
mysql-connector-python package
Installation
bash
git clone https://github.com/<your-username>/banking-system.git
cd banking-system
pip install mysql-connector-python
Create a MySQL database named banking_db, then run the schema above.
Update the DB_CONFIG dictionary in db_handler.py with your own MySQL username and password.
Run the app:
bash
python main.py


Usage
▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪
      ENTERPRISE BANKING MANAGEMENT SYSTEM
▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪
1. Open New Account
2. Check Balance
3. Deposit Money
4. Withdraw Money
5. View Transaction History
6. Exit Shell

Key Learnings

Implementing abstract base classes with @abstractmethod to enforce a consistent contract across subclasses
Using read-only @property (no setter) to protect sensitive data like account balance from direct external modification
Writing parameterized SQL queries to prevent SQL injection
Structuring a multi-file Python project using clean separation of concerns (data layer / business logic / UI)
Applying the Factory design pattern to dynamically create the correct account type at runtime





📄 License

This project is open source and available for learning purposes.
