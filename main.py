# main.py

from services.user_service import UserService
from services.transaction_service import TransactionService
from services.budget_service import BudgetService
from utils.validators import validate_amount, validate_type, format_currency

def calculate_balance(transactions):
    income = sum(t["amount"] for t in transactions if t["type"] == "income")
    expenses = sum(t["amount"] for t in transactions if t["type"] == "expense")
    return income - expenses

def add_transaction(user_id):
    try:
        amount = float(input("Amount: "))
        validate_amount(amount)
        category = input("Category: ")
        trans_type = input("Type (income/expense): ").lower()
        validate_type(trans_type)
        note = input("Note (optional): ")
        TransactionService.create_transaction(user_id, amount, category, trans_type, note)
        print("Transaction added!")
    except ValueError as e:
        print(f"Error: {e}")

def view_transactions(user_id):
    transactions = TransactionService.get_user_transactions(user_id)
    if not transactions:
        print("No transactions.")
        return
    print("\n--- Transactions ---")
    for i, t in enumerate(transactions, 1):
        print(f"{i}. Date: {t['date']} | Type: {t['type'].title()} | Category: {t['category']} | Amount: {format_currency(t['amount'])} | Note: {t.get('note', '')}")

def view_balance(user_id):
    transactions = TransactionService.get_user_transactions(user_id)
    balance = calculate_balance(transactions)
    print(f"Balance: {format_currency(balance)}")

def list_transactions_with_ids(user_id):
    transactions = TransactionService.get_user_transactions(user_id)
    if not transactions:
        print("No transactions.")
        return None
    print("\n--- Transactions (select by number) ---")
    for i, t in enumerate(transactions, 1):
        print(f"{i}. ID: {t['id']} | Date: {t['date']} | Type: {t['type'].title()} | Cat: {t['category'][:20]} | Amt: {format_currency(t['amount'])}")
    return transactions

def delete_transaction_ui(user_id):
    transactions = list_transactions_with_ids(user_id)
    if not transactions:
        return
    try:
        index = int(input("Select number to delete: ")) - 1
        if 0 <= index < len(transactions):
            tid = transactions[index]["id"]
            TransactionService.delete_transaction(tid)
            print("Transaction deleted!")
        else:
            print("Invalid selection.")
    except Exception as e:
        print(f"Error: {e}")

def edit_transaction_ui(user_id):
    transactions = list_transactions_with_ids(user_id)
    if not transactions:
        return
    try:
        index = int(input("Select number to edit: ")) - 1
        if 0 <= index < len(transactions):
            t = transactions[index]
            print(f"Editing: {format_currency(t['amount'])} {t['type']} {t['category']}")
            # Update fields
            new_amount = input(f"New amount ({t['amount']}): ") or t['amount']
            if new_amount:
                new_amount = float(new_amount)
                validate_amount(new_amount)
            new_category = input(f"New category ({t['category']}): ") or t['category']
            new_type = input(f"New type ({t['type']}): ") or t['type']
            if new_type:
                validate_type(new_type)
            new_note = input(f"New note ({t.get('note', '')}): ") or t.get('note', '')
            updates = {k: v for k, v in zip(['amount', 'category', 'type', 'note'], [new_amount, new_category, new_type, new_note]) if v != t.get(k)}
            TransactionService.update_transaction(t["id"], **updates)
            print("Transaction updated!")
        else:
            print("Invalid selection.")
    except Exception as e:
        print(f"Error: {e}")


def transactions_menu(user_id):
    while True:
        print("\n--- Transactions ---")
        print("1. Add")
        print("2. View All")
        print("3. View Balance")
        print("4. Edit")
        print("5. Delete")
        print("6. Back")
        opt = input("Choose: ")
        if opt == "1":
            add_transaction(user_id)
        elif opt == "2":
            view_transactions(user_id)
        elif opt == "3":
            view_balance(user_id)
        elif opt == "4":
            edit_transaction_ui(user_id)
        elif opt == "5":
            delete_transaction_ui(user_id)
        elif opt == "6":
            break
        else:
            print("Invalid.")

def add_budget(user_id):
    category = input("Category: ")
    limit = float(input("Limit: "))
    BudgetService.create_budget(user_id, category, limit)
    print("Budget set!")

def view_budgets(user_id):
    budgets = BudgetService.get_user_budgets(user_id)
    if not budgets:
        print("No budgets.")
        return
    print("\n--- Budgets ---")
    for i, b in enumerate(budgets, 1):
        print(f"{i}. Category: {b['category']} | Limit: {format_currency(b['limit'])} | ID: {b['id']}")

def delete_budget_ui(user_id):
    budgets = BudgetService.get_user_budgets(user_id)
    if not budgets:
        print("No budgets.")
        return
    print("\n--- Budgets ---")
    for i, b in enumerate(budgets, 1):
        print(f"{i}. {b['category']} ${b['limit']:.2f}")
    try:
        index = int(input("Select number to delete: ")) - 1
        if 0 <= index < len(budgets):
            bid = budgets[index]["id"]
            BudgetService.delete_budget(bid)
            print("Budget deleted!")
        else:
            print("Invalid.")
    except:
        print("Error.")

def edit_budget_ui(user_id):
    budgets = BudgetService.get_user_budgets(user_id)
    if not budgets:
        return
    print("\n--- Budgets ---")
    for i, b in enumerate(budgets, 1):
        print(f"{i}. {b['category']} ${b['limit']:.2f} | ID: {b['id']}")
    try:
        index = int(input("Select number to edit: ")) - 1
        if 0 <= index < len(budgets):
            b = budgets[index]
            new_category = input(f"New category ({b['category']}): ") or b['category']
            new_limit = input(f"New limit ({b['limit']}): ") or b['limit']
            if new_limit:
                new_limit = float(new_limit)
            updates = {}
            if new_category != b['category']:
                updates['category'] = new_category
            if 'new_limit' in locals() and new_limit != b['limit']:
                updates['limit'] = new_limit
            if updates:
                BudgetService.update_budget(b["id"], **updates)
                print("Budget updated!")
            else:
                print("No changes.")
        else:
            print("Invalid.")
    except Exception as e:
        print(f"Error: {e}")

def budgets_menu(user_id):
    while True:
        print("\n--- Budgets ---")
        print("1. Set Budget")
        print("2. View")
        print("3. Edit")
        print("4. Delete")
        print("5. Back")
        opt = input("Choose: ")
        if opt == "1":
            add_budget(user_id)
        elif opt == "2":
            view_budgets(user_id)
        elif opt == "3":
            edit_budget_ui(user_id)
        elif opt == "4":
            delete_budget_ui(user_id)
        elif opt == "5":
            break
        else:
            print("Invalid.")

# Main application loop
def main():
    print("=== Finance Manager ===")

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            email = input("Email: ")
            password = input("Password: ")
            try:
                user = UserService.register(email, password)
                print(f"User {user.email} created!")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "2":
            email = input("Email: ")
            password = input("Password: ")
            try:
                user = UserService.login(email, password)
                user_id = user['localId']
                while True:
                    print("\n1. Transactions")
                    print("2. Budgets")
                    print("3. Logout")
                    action = input("Choose: ")
                    if action == "1":
                        transactions_menu(user_id)
                    elif action == "2":
                        budgets_menu(user_id)
                    elif action == "3":
                        break
                    else:
                        print("Invalid.")
            except Exception as e:
                print(f"Login error: {e}")
        else:
            break

if __name__ == "__main__":
    main()
