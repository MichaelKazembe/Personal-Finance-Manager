'''
Docstring for models.transactions

Transactions module for Personal Finance Manager application.
This module defines the data model and operations related to financial transactions, 
including creating, retrieving, updating, and deleting transaction records in the 
Firestore database.
'''

from config.firebase_config import db
from datetime import datetime

# Transaction Model
class Transaction:
    '''
    Model for representing a financial transaction in the application.
    
    Attributes:
        document_id (str): Unique identifier for the transaction document in Firestore.
        amount (float): Amount of the transaction.
        category (str): Category of the transaction (e.g., "Groceries", "Transport").
        date (datetime): Date and time of the transaction.
        description (str): Optional description of the transaction.
    ''' 
    def __init__(self, transaction_id: str, amount: float, category: str, date=None, description=None):
        self.document_id = transaction_id
        self.amount = amount
        self.category = category
        self.date = date if date else datetime.now()
        self.description = description

    def to_dict(self):
        # Convert the Transaction instance to a dictionary for Firestore storage
        return {
            'amount': self.amount,
            'category': self.category,
            'date': self.date,
            'description': self.description
        }       
