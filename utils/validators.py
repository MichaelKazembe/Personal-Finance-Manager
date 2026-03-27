# utils/validators.py
'''Validators Module
This module provides utility functions for validating transaction data and formatting currency.
'''

def validate_amount(amount):
    '''Validate that the amount is a positive number.
    Args:        amount (float): The amount to validate
    Raises:        ValueError: If the amount is not greater than 0
    '''
    if amount <= 0:
        raise ValueError("Amount must be greater than 0")

def validate_type(tx_type):
    '''Validate that the transaction type is either "income" or "expense".
    Args:        tx_type (str): The transaction type to validate
    Raises:        ValueError: If the transaction type is not "income" or "expense"
    '''
    if tx_type not in ["income", "expense"]:
        raise ValueError("Type must be 'income' or 'expense'")


def format_currency(amount):
    '''Format a number as currency.
    Args:        amount (float): The amount to format
    Returns:        str: The formatted currency string
    '''
    return f"${amount:.2f}"
