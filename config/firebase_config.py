# config/firebase_config.py

import firebase_admin
from firebase_admin import credentials, firestore
import pyrebase
import json

# Initialize Firebase Admin SDK with service account credentials
cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore client
db = firestore.client()

# Load Firebase configuration from config.json for Pyrebase
with open("config/config.json") as f:
    firebase_config = json.load(f)

# Initialize Pyrebase for authentication and real-time database operations
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()