import mysql.connector
from mysql.connector import Error


DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',       # Your MySQL username
    'password': 'Rooot', # Your MySQL password
    'database': 'banking_db'
}

def get_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            return conn
    except Error as e:
        print(f" Database Connection Fault: {e}")
        return None

def fetch_account(acc_num):
    conn = get_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM accounts WHERE account_number = %s", (acc_num,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row
    return None

def save_account(holder_name, acc_type, pin, balance):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        query = "INSERT INTO accounts (holder_name, account_type, pin, balance) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (holder_name, acc_type, pin, balance))
        conn.commit()
        acc_num = cursor.lastrowid
        cursor.close()
        conn.close()
        return acc_num
    return None

def update_balance(acc_num, new_balance, trans_type, amount):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        # Update Account Balance
        cursor.execute("UPDATE accounts SET balance = %s WHERE account_number = %s", (new_balance, acc_num))
        # Log Transaction
        cursor.execute(
            "INSERT INTO transactions (account_number, transaction_type, amount) VALUES (%s, %s, %s)",
            (acc_num, trans_type, amount)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return True
    return False

def fetch_transactions(acc_num):
    conn = get_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM transactions WHERE account_number = %s ORDER BY timestamp DESC", (acc_num,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    return []