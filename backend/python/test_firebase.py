import firebase_admin
import os
from firebase_admin import credentials, firestore

# load credentials
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # backend/
FIREBASE_KEY = os.path.join(BASE_DIR, "firebase", "serviceAccountKey.json")

cred = credentials.Certificate(FIREBASE_KEY)
firebase_admin.initialize_app(cred)

db = firestore.client()

# Test document
doc_ref = db.collection("test_collection").document("demo")
doc_ref.set({
    "message": "Hello, Firestore!"
})

print("Test document added to Firestore successfully.")