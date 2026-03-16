from config.firebase_config import db
from datetime import datetime

# Test connection
def test_connection():
    try:
        # Attempt to retrieve a document from Firestore
        doc_ref = db.collection('FinanceManagerDB').document('transaction1')
        doc = doc_ref.set({
            'amount': 100,
            'category': 'Groceries',
            'date': datetime.now()
        })
        print("Connection successful, document created.")
    except Exception as e:  
        print("Connection failed:", e)
        
        