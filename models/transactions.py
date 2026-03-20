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
    def __init__(self, amount, category, date=None, description=None):
        self.amount = amount
        self.category = category
        self.date = date if date else datetime.now()
        self.description = description

    def to_dict(self):
        return {
            'amount': self.amount,
            'category': self.category,
            'date': self.date,
            'description': self.description
        }

