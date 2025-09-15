# 🛠 Backend - Puerto Inteligente

El backend del proyecto se construirá combinando **Firebase** y **scripts en Python**.  
El objetivo es conseguir **tiempo real, simplicidad y capacidad analítica avanzada**.

---

## 🔹 Arquitectura general

1. **Firebase**  
   - **Firestore**: almacenamiento en tiempo real de consumo, generación solar, clima y precios.  
   - **Cloud Functions**: lógica ligera (cálculo de KPIs simples, balance energético, alertas).  
   - **Realtime updates**: el frontend recibe datos en vivo directamente desde Firestore.  

2. **Python local (scripts / notebooks)**  
   - Lectura del dataset histórico (CSV).  
   - Procesamiento de datos avanzados y predicciones (ARIMA, Prophet, regresiones, optimización).  
   - Subida de resultados procesados a Firestore (para que el frontend los muestre como si fueran datos en vivo).  

---

## 🔹 Estructura de carpetas

backend/
│
├── firebase/
│ ├── firestore_schema.md # Esquema de colecciones y documentos
│ ├── cloud_functions/ # Funciones en Node.js para cálculos rápidos
│ │ ├── index.js
│ │ └── package.json
│ └── rules/ # Reglas de seguridad de Firestore
│
├── python/
│ ├── ingest_data.py # Script para subir CSV histórico a Firestore
│ ├── forecast_model.py # Predicción de consumo/coste con ML
│ ├── optimization.py # Algoritmos de optimización energética
│ └── utils/ # Funciones auxiliares (limpieza, KPIs)


---

## 🔹 Flujo de datos

1. **Ingesta**  
   - `ingest_data.py` sube el dataset horario a Firestore.  
   - Se simula el tiempo real insertando registros con retraso controlado.  

2. **Procesamiento simple**  
   - Cloud Functions calculan en tiempo real:
     - Balance energético (`consumo - generación`).  
     - Coste horario (`consumo * precio`).  
     - % renovable usado.  

3. **Procesamiento avanzado**  
   - Python entrena modelos de predicción (consumo, costes, producción solar).  
   - Los resultados se escriben en Firestore en colecciones como `predicciones/`.  

4. **Consumo en frontend**  
   - El dashboard React/Streamlit escucha Firestore en tiempo real.  
   - Muestra métricas actuales, gráficas históricas y predicciones.  

---

## 🔹 Resumen

- **Firebase** → gestiona la API y la base de datos en tiempo real.  
- **Cloud Functions** → reglas rápidas y cálculos ligeros.  
- **Python** → análisis avanzado, predicciones y optimización.  
- **Frontend** → consume directamente de Firestore para tiempo real.  

👉 Con esta arquitectura, el backend es **rápido de montar para la hackathon** y suficientemente **potente para mostrar análisis avanzados**.
