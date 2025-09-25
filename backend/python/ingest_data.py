import pandas as pd
import firebase_admin
import os
from firebase_admin import credentials, firestore

# === CONFIGURACIÓN FIREBASE ===
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # backend/
FIREBASE_KEY = os.path.join(BASE_DIR, "firebase", "serviceAccountKey.json")

cred = credentials.Certificate(FIREBASE_KEY)
firebase_admin.initialize_app(cred)

db = firestore.client()

# === CARGA DEL CSV === 
CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "simulated_vaasa_energy_dataset.csv")
df = pd.read_csv(CSV_PATH)


# === SUBIDA A FIRESTORE ===
collection_name = "energy_data"

for _, row in df.iterrows():
    doc_id = row['timestamp']  # Usar timestamp como ID del documento
    doc_ref = db.collection(collection_name).document(str(doc_id))
    doc_ref.set({
        "consumption_kWh": float(row['consumption_kWh']),
        "solar_generation_kWh": float(row['solar_generation_kWh']),
        "temperature_C": float(row['temperature_C']),
        "wind_speed_mps": float(row['wind_speed_mps']),
        "humidity_pct": float(row['humidity_pct']),
        "electricity_price_EUR_MWh": float(row['electricity_price_EUR_MWh'])
    })

print("Datos subidos a Firestore con éxito.")
