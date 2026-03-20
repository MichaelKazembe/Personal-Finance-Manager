from config.firebase_config import db
from datetime import datetime

# Test connection
# def test_connection():
#     try:
#         # Attempt to retrieve a document from Firestore
#         doc_ref = db.collection('Transactions').document('transaction1')
#         doc = doc_ref.set({
#             'amount': 100,
#             'category': 'Groceries',
#             'date': datetime.now()
#         })
#         print("Connection successful, document created.")
#     except Exception as e:  
#         print("Connection failed:", e)
        
        
# Create Collection
def create_collection(collection_name):
    try:
        # Create a new document in the specified collection
        doc_ref = db.collection(collection_name).document('sample_doc')
        doc_ref.set({
            'field1': 'value1',
            'field2': 'value2',
            'timestamp': datetime.now()
        })
        print(f"Collection '{collection_name}' created with a sample document.")
    except Exception as e:
        print(f"Failed to create collection '{collection_name}':", e)
        
        
# Read from Collection
def read_collection(collection_name):
    try:
        # Retrieve all documents from the specified collection
        docs = db.collection(collection_name).stream()
        print(f"Documents in collection '{collection_name}':")
        for doc in docs:
            print(f"{doc.id} => {doc.to_dict()}")
    except Exception as e:
        print(f"Failed to read collection '{collection_name}':", e)
        
# Update Document
def update_document(collection_name, doc_id, update_data):
    try:
        # Update the specified document with new data
        doc_ref = db.collection(collection_name).document(doc_id)
        doc_ref.update(update_data)
        print(f"Document '{doc_id}' in collection '{collection_name}' updated successfully.")
    except Exception as e:
        print(f"Failed to update document '{doc_id}' in collection '{collection_name}':", e)
        
# Delete Document
def delete_document(collection_name, doc_id):
    try:
        # Delete the specified document from the collection
        doc_ref = db.collection(collection_name).document(doc_id)
        doc_ref.delete()
        print(f"Document '{doc_id}' in collection '{collection_name}' deleted successfully.")
    except Exception as e:
        print(f"Failed to delete document '{doc_id}' in collection '{collection_name}':", e)
        
# Delete Collection
def delete_collection(collection_name):
    try:
        # Retrieve all documents in the collection and delete them
        docs = db.collection(collection_name).stream()
        for doc in docs:
            doc.reference.delete()
        print(f"Collection '{collection_name}' and all its documents deleted successfully.")
    except Exception as e:
        print(f"Failed to delete collection '{collection_name}':", e)