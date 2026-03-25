# models/transactions.py
"""
Transaction Model Module

This module defines the Transaction class which represents a financial transaction
in the Personal Finance Manager application. Transactions can be either income or
expense types and include support for date formatting and serialization.
"""

from datetime import datetime


class Transaction:
    """
    Transaction model class representing a financial transaction.
    
    Attributes:
        amount (float): The monetary value of the transaction
        category (str): The category of the transaction (e.g., "Food", "Transport")
        user_id (str): The ID of the user who made the transaction
        type (str): The type of transaction - either "income" or "expense"
        note (str): Optional notes or description about the transaction
        date (str): The date and time when the transaction was created
    """
    def __init__(self, amount, category, user_id, type, note=""):
        """
        Initialize a new Transaction instance.
        
        Args:
            amount (float): The monetary value of the transaction
            category (str): The transaction category (e.g., "Food", "Transport", "Utilities")
            user_id (str): The unique identifier of the user making the transaction
            type (str): The transaction type - "income" or "expense"
            note (str, optional): Additional notes about the transaction. Defaults to empty string.
        """
        self.amount = amount
        self.category = category
        self.user_id = user_id
        self.type = type  # "income" or "expense"
        self.note = note
        # Automatically set the transaction date to the current date and time
        self.date = datetime.today().strftime('%d %b %Y, %H:%M')

    def to_dict(self):
        """
        Convert the Transaction object to a dictionary for storage or serialization.
        
        Returns:
            dict: A dictionary containing all transaction attributes:
                - amount: The transaction amount
                - category: The transaction category
                - user_id: The user's ID
                - type: The transaction type (income/expense)
                - note: Optional notes about the transaction
                - date: The formatted date and time
        """
        return {
            "amount": self.amount,
            "category": self.category,
            "user_id": self.user_id,
            "type": self.type,
            "note": self.note,
            "date": self.date
        }

    @classmethod
    def format_date(cls, date_input):
        """
        Format a date from various input formats to a standardized string format.
        
        Handles multiple date formats including:
        - Firebase Firestore timestamp objects (dict with _seconds and _nanoseconds)
        - Custom stored format (e.g., "25 Mar 2026, 14:30")
        - ISO format strings (e.g., "2026-03-25T14:30:00Z")
        
        Args:
            date_input: The date to format. Can be:
                - dict: Firebase Firestore timestamp with _seconds and _nanoseconds keys
                - str: Date string in custom or ISO format
        
        Returns:
            str: The formatted date string in format '%d %b %Y, %H:%M' (e.g., "25 Mar 2026, 14:30")
                 Returns current datetime if parsing fails
        """
        if isinstance(date_input, dict):
            # Handle Firebase Firestore timestamp objects
            if '_seconds' in date_input and '_nanoseconds' in date_input:
                dt = datetime.fromtimestamp(date_input['_seconds'] + date_input['_nanoseconds'] / 10**9)
            else:
                # Fallback to current time if dict format is unexpected
                dt = datetime.now()
        else:
            try:
                # Try custom format first (from storage)
                dt = datetime.strptime(date_input, '%d %b %Y, %H:%M')
            except ValueError:
                try:
                    # Handle ISO string format
                    dt = datetime.fromisoformat(date_input.replace('Z', '+00:00'))
                except ValueError:
                    # Fallback to current time if all parsing attempts fail
                    dt = datetime.now()
        return dt.strftime('%d %b %Y, %H:%M')
