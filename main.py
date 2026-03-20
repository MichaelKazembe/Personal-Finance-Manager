from config.firebase_config import db
from services.db import *
from services.transaction_service import *

# Create Transaction instances
transaction1 = Transaction(100, "Groceries", "2025-03-20", "Bought groceries")
transaction2 = Transaction(50, "Transport", "2025-03-19", "Bus fare")
transaction3 = Transaction(200, "Entertainment", "2025-03-18", "Movie tickets")

def main():
    # Example usage of the database functions
    
    # Adding a transactions
    add_transaction(transaction1.amount, transaction1.category, transaction1.date, transaction1.description)
    add_transaction(transaction2.amount, transaction2.category, transaction2.date, transaction2.description)
    add_transaction(transaction3.amount, transaction3.category, transaction3.date, transaction3.description)
    
    # Reading transactions
    transactions = get_transactions()
    print(transactions)
    
        
if __name__ == "__main__":    
    main()