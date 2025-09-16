import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore

# === CONFIGURACIÓN FIREBASE ===
# Descarga tu archivo de credenciales desde Firebase Console
# y guárdalo en la carpeta backend/firebase/ con el nombre "serviceAccountKey.json"

cred = credentials.Certificate("..firebase/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# === CARGA DEL CSV === 
df = pd.read_csv(simulated_vaasa_energy_dataset.csv)

# === SUBIDA A FIRESTORE ===
collection_name = "energy_data"

for _, row in df.iterrows():
    doc_id = row['timestamp'] # Usar timestamp como ID del documento
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