import pandas as pd
import numpy as np
import random

# Configuración del dataset simulado
np.random.seed(42)
n_hours = 24 * 14  # 2 semanas de datos horarios
time_index = pd.date_range(start="2025-09-01", periods=n_hours, freq="H")

# Generar consumo energético simulado (kWh)
# Patrón: más consumo en horas de la tarde/noche, menos de madrugada
base_consumption = []
for ts in time_index:
    hour = ts.hour
    if 0 <= hour < 6:
        value = np.random.normal(20, 5)
    elif 6 <= hour < 12:
        value = np.random.normal(35, 8)
    elif 12 <= hour < 18:
        value = np.random.normal(45, 10)
    else:
        value = np.random.normal(55, 12)
    base_consumption.append(max(value, 5))

# Producción solar simulada (kWh)
# Solo durante el día (6h - 20h), con picos al mediodía
solar_generation = []
for ts in time_index:
    hour = ts.hour
    if 6 <= hour <= 20:
        peak = np.sin((hour - 6) / 14 * np.pi) * 30
        noise = np.random.normal(0, 3)
        solar_generation.append(max(0, peak + noise))
    else:
        solar_generation.append(0)

# Datos meteorológicos (temperatura, viento, humedad)
temperature = 10 + 10*np.sin(np.linspace(0, 3*np.pi, n_hours)) + np.random.normal(0, 2, n_hours)
wind_speed = np.random.normal(5, 2, n_hours)  # m/s
humidity = np.random.normal(70, 10, n_hours)  # %

# Precios de electricidad (€/MWh) simulados con picos en la tarde
electricity_price = []
for ts in time_index:
    hour = ts.hour
    base = 50
    if 18 <= hour <= 22:
        price = np.random.normal(120, 15)
    elif 8 <= hour <= 16:
        price = np.random.normal(70, 10)
    else:
        price = np.random.normal(40, 8)
    electricity_price.append(max(price, 10))

# Construir DataFrame
df = pd.DataFrame({
    "timestamp": time_index,
    "consumption_kWh": base_consumption,
    "solar_generation_kWh": solar_generation,
    "temperature_C": temperature,
    "wind_speed_mps": wind_speed,
    "humidity_pct": humidity,
    "electricity_price_EUR_MWh": electricity_price
})

# Guardar dataset
file_path = "simulated_vaasa_energy_dataset.csv"
df.to_csv(file_path, index=False)

import caas_jupyter_tools
caas_jupyter_tools.display_dataframe_to_user("Simulated Vaasa Energy Dataset", df.head(50))

file_path
