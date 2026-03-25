# config/firebase_config.py

import firebase_admin
from firebase_admin import credentials, firestore
import pyrebase

cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore client
db = firestore.client()

firebase_config = {
  "apiKey": "AIzaSyBnS-GeAUpQ8zF3nLk40_AHHW57_UB-rJ8",
  "authDomain": "financemanagerdb.firebaseapp.com",
  "databaseURL": "https://financemanagerdb-default-rtdb.firebaseio.com",
  "projectId": "financemanagerdb",
  "storageBucket": "financemanagerdb.firebasestorage.app",
  "messagingSenderId": "268336752613",
  "appId": "1:268336752613:web:80dc2dd5bde248845d310c"
}

# Initialize Pyrebase for authentication and real-time database operations
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()