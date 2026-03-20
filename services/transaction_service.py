from config.firebase_config import db
from models.transactions import Transaction

#  Add Transaction
def add_transaction(transaction_id, amount, category, date=None, description=None):
    '''
    Function to add a new transaction to the Firestore database.
    
    :param transaction_id: ID of the transaction
    :param amount: amount of the transaction
    :param category: category of the transaction
    :param date: date of the transaction
    :param description: Description of the transaction
    '''
    
    # Create a Transaction instance
    transaction = Transaction(transaction_id, amount, category, date, description)
    
    try:
        # Save the transaction to Firestore
        doc_ref = db.collection('Transactions').document(transaction_id)
        # Use the provided document ID as the document reference
        doc_ref.set(transaction.to_dict())
        print("Transaction saved successfully.")
    except Exception as e:
        print("Failed to save transaction:", e)
        
        
# Get Transaction
def get_transaction(transaction_id: str):
    '''
    Function to retrieve a specific transaction from the Firestore database.
    
    :param transaction_id: ID of the transaction to retrieve
    :return: Transaction data or None if not found
    '''
    try:
        # Retrieve the specific document from the 'Transactions' collection
        doc_ref = db.collection('Transactions').document(transaction_id)
        doc = doc_ref.get()
        # Check if the document exists and return its data
        if doc.exists:
            # Include the document ID in the transaction data
            transaction_data = doc.to_dict()
            transaction_data['id'] = doc.id
            return transaction_data
        else:
            print(f"Transaction with ID '{transaction_id}' not found.")
            return None
    # Handle exceptions and print error message
    except Exception as e:
        print(f"Failed to retrieve transaction with ID '{transaction_id}':", e)
        return None


# Get All Transactions
def get_transactions():
    '''
    Function to retrieve all transactions from the Firestore database.
    
    :return: List of transaction data
    '''
    try:
        # Retrieve all documents from the 'Transactions' collection
        docs = db.collection('Transactions').stream()
        transactions = []
        for doc in docs:
            transaction_data = doc.to_dict()
            transaction_data['id'] = doc.id  # Include document ID in the data
            transactions.append(transaction_data)
        return transactions
    except Exception as e:
        print("Failed to retrieve transactions:", e)
        return []

# Update Transaction
def update_transaction(transaction_id: str, update_data: dict):
    '''
    Function to update an existing transaction in the Firestore database.
    
    :param transaction_id: ID of the transaction to update
    :param update_data: Dictionary containing the fields to update
    '''
    try:
        # Update the specified document with new data
        doc_ref = db.collection('Transactions').document(transaction_id)
        doc_ref.update(update_data)
        print(f"Transaction '{transaction_id}' updated successfully.")
    except Exception as e:
        print(f"Failed to update transaction '{transaction_id}':", e)
        

# Delete Transaction
def delete_transaction(transaction_id: str):
    '''
    Function to delete a transaction from the Firestore database.
    
    :param transaction_id: ID of the transaction to delete
    '''
    try:
        # Delete the specified document from the collection
        doc_ref = db.collection('Transactions').document(transaction_id)
        doc_ref.delete()
        print(f"Transaction '{transaction_id}' deleted successfully.")
    except Exception as e:
        print(f"Failed to delete transaction '{transaction_id}':", e)