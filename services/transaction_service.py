# services/transaction_service.py
"""
Transaction Service Module

This module provides database operations for managing user transactions.
It handles CRUD operations (Create, Read, Update, Delete) for transaction records
stored in Firebase Firestore, including date formatting utilities.
"""

from config.firebase_config import db
from models.transaction import Transaction


class TransactionService:
    """Service class for managing transaction-related database operations."""

    @staticmethod
    def create_transaction(user_id, amount, category, trans_type, note=""):
        """
        Create a new transaction record for a user.
        
        Args:
            user_id (str): The ID of the user making the transaction
            amount (float): The transaction amount
            category (str): The transaction category (e.g., "Food", "Transport")
            trans_type (str): The type of transaction ("income" or "expense")
            note (str, optional): Additional notes about the transaction. Defaults to empty string.
        """
        transaction = Transaction(amount, category, user_id, trans_type, note)
        db.collection("transactions").add(transaction.to_dict())

    @staticmethod
    def get_user_transactions(user_id):
        """
        Retrieve all transactions for a specific user.
        
        Args:
            user_id (str): The ID of the user
            
        Returns:
            list: A list of transaction dictionaries with formatted dates and document IDs
        """
        docs = db.collection("transactions") \
            .where("user_id", "==", user_id) \
            .stream()

        transactions = []

        for doc in docs:
            data = doc.to_dict()
            data["id"] = doc.id

            # Format date to human-readable format
            if "date" in data:
                data["date"] = Transaction.format_date(data["date"])

            transactions.append(data)

        return transactions
    
    @staticmethod
    def delete_transaction(transaction_id):
        """
        Delete a transaction from the database.
        
        Args:
            transaction_id (str): The transaction document ID to delete
        """
        db.collection("transactions").document(transaction_id).delete()

    @staticmethod
    def get_transaction(tid):
        """
        Retrieve a specific transaction by its ID.
        
        Args:
            tid (str): The transaction document ID
            
        Returns:
            dict: The transaction data with formatted date and ID, or None if not found
        """
        doc = db.collection("transactions").document(tid).get()
        if doc.exists:
            data = doc.to_dict()
            if "date" in data:
                data["date"] = Transaction.format_date(data["date"])
            data["id"] = tid
            return data
        return None

    @staticmethod
    def update_transaction(tid, **kwargs):
        """
        Update specific fields of an existing transaction.
        
        Args:
            tid (str): The transaction document ID
            **kwargs: Fields to update (e.g., amount=100, category="Food", note="Updated note")
        """
        db.collection("transactions").document(tid).update(kwargs)
