# Import necessary libraries
import sqlite3    
import hashlib    

# Define the main BankApp class to manage the bank application


class BankApp:
    # Initialize the BankApp class with a database name
    def __init__(self, db_name):
        # Create a connection to the SQLite database with the given name
        self.conn = sqlite3.connect(db_name)
        # Create a cursor object to execute SQL queries on the database
        self.cursor = self.conn.cursor()
        # Ensure that the accounts table is created when the application starts
        self.create_table()

    # Method to create the accounts table if it doesn't already exist
    def create_table(self):
        # Execute an SQL command to create the 'accounts' table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY,    -- Primary key for each account
                username TEXT,             -- Username column for account name
                password TEXT,             -- Password column for hashed passwords
                balance REAL               -- Balance column to store account balance
            )
        ''')
        # Commit changes to the database to save the table
        self.conn.commit()

    # Method to check if a username already exists in the database
    def user_already_exist(self):
        # Prompt the user to enter a username
        username = input("Enter a username: ")
        # Execute SQL query to find if the username already exists in the 'accounts' table
        self.cursor.execute(
            "SELECT username FROM accounts WHERE username = ?", (username,))
        # Fetch the result of the query
        account = self.cursor.fetchone()
        # If an account with the username exists, prompt the user to try again
        if account:
            print("Username already in use, use another new one")
            return self.user_already_exist()  # Recursive call if username exists
        else:
            # Return the valid username if it doesn't exist
            return username

    # Method to create a new account in the database
    def create_account(self, username, password):
        # Hash the password using SHA-256 for security before storing it
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        # Insert the new account details into the accounts table with an initial balance of 0.0
        self.cursor.execute(
            "INSERT INTO accounts (username, password, balance) VALUES (?, ?, ?)", (username, hashed_password, 0.0))
        # Commit changes to the database
        self.conn.commit()
        print("Account created successfully.")

    # Method to log in by verifying username and password
    def login(self, username, password):
        # Hash the entered password for comparison
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        # Query the accounts table to find a matching username and password
        self.cursor.execute(
            "SELECT * FROM accounts WHERE username=? AND password=?", (username, hashed_password))
        # Fetch the matching account details if found
        account = self.cursor.fetchone()
        # Return the account if it exists, otherwise return None
        return account

    # Method to check and retrieve the account balance
    def check_balance(self, username):
        # Query the balance of the user with the given username
        self.cursor.execute(
            "SELECT balance FROM accounts WHERE username=?", (username,))
        # Fetch the balance result
        balance = self.cursor.fetchone()
        # Return the balance if found, otherwise return 0.0 as default
        return balance[0] if balance else 0.0

    # Method to deposit money into the account
    def deposit(self, username, amount):
        # Retrieve the current balance
        current_balance = self.check_balance(username)
        # Add the deposit amount to the current balance
        new_balance = current_balance + amount
        # Update the database with the new balance for the user
        self.cursor.execute(
            "UPDATE accounts SET balance=? WHERE username=?", (new_balance, username))
        # Commit the balance update to the database
        self.conn.commit()

    # Method to withdraw money from the account
    def withdraw(self, username, amount):
        # Retrieve the current balance
        current_balance = self.check_balance(username)
        # Check if there are sufficient funds for the withdrawal
        if amount > current_balance:
            return "Insufficient balance"
        # Subtract the withdrawal amount from the current balance
        new_balance = current_balance - amount
        # Update the database with the new balance
        self.cursor.execute(
            "UPDATE accounts SET balance=? WHERE username=?", (new_balance, username))
        # Commit the balance update to the database
        self.conn.commit()

    # Method to transfer money between accounts
    def transfer(self, sender_username, receiver_username, amount):
        # Retrieve the sender's current balance
        sender_balance = self.check_balance(sender_username)
        # Check if the sender has enough funds for the transfer
        if amount > sender_balance:
            return "Insufficient balance"

        # Retrieve the receiver's current balance
        receiver_balance = self.check_balance(receiver_username)
        # Calculate new balances for both sender and receiver
        new_sender_balance = sender_balance - amount
        new_receiver_balance = receiver_balance + amount

        # Update the sender's balance in the database
        self.cursor.execute("UPDATE accounts SET balance=? WHERE username=?",
                            (new_sender_balance, sender_username))
        # Update the receiver's balance in the database
        self.cursor.execute("UPDATE accounts SET balance=? WHERE username=?",
                            (new_receiver_balance, receiver_username))
        # Commit both balance updates to the database
        self.conn.commit()

    # Method to close the database connection when the application finishes
    def close(self):
        # Close the database connection
        self.conn.close()

# Main function that runs the bank application and provides user interface


def main():
    # Initialize a BankApp instance with the database name "bank.db"
    bank_app = BankApp("bank.db")

    while True:
        # Display the main menu options for the user
        print("\nBank Application")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        # Prompt user to choose an option from the menu
        choice = input("Select an operation: ")

        if choice == "1":
            # Option 1: Create a new account
            username = bank_app.user_already_exist()
            password = input("Enter a password: ")
            bank_app.create_account(username, password)

        elif choice == "2":
            # Option 2: Log in to an existing account
            username = input("Enter username: ")
            password = input("Enter password: ")
            account = bank_app.login(username, password)
            if account:
                print("Login successful.")
                # Once logged in, display account options to the user
                while True:
                    print("\n1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Transfer")
                    print("5. Logout")
                    action = input("Select an action: ")

                    if action == "1":
                        # Option 1: Check balance
                        balance = bank_app.check_balance(username)
                        print(f"Balance: ${balance:.2f}")

                    elif action == "2":
                        # Option 2: Deposit money
                        amount = float(input("Enter deposit amount: "))
                        bank_app.deposit(username, amount)
                        print("Deposit successful.")

                    elif action == "3":
                        # Option 3: Withdraw money
                        amount = float(input("Enter withdrawal amount: "))
                        result = bank_app.withdraw(username, amount)
                        if result == "Insufficient balance":
                            print(result)
                        else:
                            print("Withdrawal successful.")

                    elif action == "4":
                        # Option 4: Transfer money to another user
                        receiver = input("Enter the recipient's username: ")
                        amount = float(input("Enter transfer amount: "))
                        result = bank_app.transfer(username, receiver, amount)
                        if result == "Insufficient balance":
                            print(result)
                        else:
                            print("Transfer successful.")

                    elif action == "5":
                        # Option 5: Logout
                        print("Logged out.")
                        break

                    else:
                        print("Invalid action. Try again.")

            else:
                print("Login failed. Invalid username or password.")

        elif choice == "3":
            # Option 3: Exit the application
            print("Exiting the application.")
            bank_app.close()
            break

        else:
            print("Invalid choice. Try again.")


# Run the main function to start the application
if __name__ == "__main__":
    main()
