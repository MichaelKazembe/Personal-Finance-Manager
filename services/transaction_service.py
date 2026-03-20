from config.firebase_config import db
from models.transactions import Transaction

#  Add Transaction
def add_transaction(amount, category, date=None, description=None):
    '''
    Function to add a new transaction to the Firestore database.
    
    :param amount: amount of the transaction
    :param category: category of the transaction
    :param date: date of the transaction
    :param description: Description of the transaction
    '''
    
    # Create a Transaction instance
    transaction = Transaction(amount, category, date, description)
    
    try:
        # Save the transaction to Firestore
        doc_ref = db.collection('Transactions').document()
        # Use auto-generated document ID
        doc_ref.set(transaction.to_dict())
        print("Transaction saved successfully.")
    except Exception as e:
        print("Failed to save transaction:", e)
        
        
# Get Transactions
def get_transactions():
    '''
    Function to retrieve all transactions from the Firestore database.
    
    :return: List of transactions
    '''
    try:
        # Retrieve all documents from the 'Transactions' collection
        docs = db.collection('Transactions').stream()
        # Convert documents to a list of transaction dictionaries
        transactions = []
        for doc in docs:
            transaction_data = doc.to_dict()
            # Include the document ID in the transaction data
            transaction_data['id'] = doc.id 
            # Append the transaction data to the list
            transactions.append(transaction_data)
        return transactions
    except Exception as e:
        print("Failed to retrieve transactions:", e)
        return []


# Update Transaction
def update_transaction(transaction_id, update_data):
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