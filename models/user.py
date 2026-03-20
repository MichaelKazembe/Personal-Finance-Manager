'''
Docstring for models.user
'''

from config.firebase_config import db

# User Model
class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email
        }

    def save(self):
        try:
            # Save the user to Firestore
            doc_ref = db.collection('Users').document(self.user_id)
            doc_ref.set(self.to_dict())
            print("User saved successfully.")
        except Exception as e:
            print("Failed to save user:", e)