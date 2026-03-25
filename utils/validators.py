# utils/validators.py

def validate_amount(amount):
    if amount <= 0:
        raise ValueError("Amount must be greater than 0")

def validate_type(tx_type):
    if tx_type not in ["income", "expense"]:
        raise ValueError("Type must be 'income' or 'expense'")


def format_currency(amount):
    return f"${amount:.2f}"
