from config.firebase_config import db
from services.db import *
from services.transaction_service import *

# Example transactions
transaction1 = Transaction("transaction1", 100, "Groceries", "2025-03-20", "Bought groceries")
# transaction2 = Transaction("transaction2", 50, "Transport", "2025-03-19", "Bus fare")
# transaction3 = Transaction("transaction3", 200, "Entertainment", "2025-03-18", "Movie tickets")

# 

def main():
    # Example usage of the database functions
    
    # Adding a transactions
    # add_transaction(transaction1.document_id, transaction1.amount, transaction1.category, transaction1.date, transaction1.description)
    # add_transaction(transaction2.document_id, transaction2.amount, transaction2.category, transaction2.date, transaction2.description)
    # add_transaction(transaction3.document_id, transaction3.amount, transaction3.category, transaction3.date, transaction3.description)
    
    # Reading transaction
    transaction = get_transaction(transaction1.document_id)
    print(transaction)
    
    # Updating a transaction
    # update_transaction(transaction2.document_id, {'amount': 150})
    
    # Deleting a transaction
    # delete_transaction(transaction3)
        
if __name__ == "__main__":    
    main()