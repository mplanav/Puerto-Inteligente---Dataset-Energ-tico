# 📊 Análisis de Datos - Puerto Inteligente

El análisis de datos se encargará de **procesar, entender y predecir** el consumo energético del puerto.  
Se trabajará con **Python** para sacar KPIs, predicciones y reglas de optimización que se almacenarán en Firebase y serán consumidas por el frontend.

---

## 🔹 Objetivos principales
1. **KPIs** → métricas clave para evaluar la operación energética.  
2. **Análisis descriptivo** → patrones de consumo, correlaciones con clima y precios.  
3. **Predicción** → consumo y coste horario futuro.  
4. **Optimización** → recomendaciones automáticas para reducir costes y emisiones.  

---

## 🔹 Estructura de carpetas

analisis_datos/
│
├── notebooks/
│ ├── exploracion.ipynb # Exploración inicial del dataset
│ ├── correlaciones.ipynb # Clima vs consumo, precios vs consumo
│ └── forecasting.ipynb # Modelos de predicción (Prophet / ARIMA)
│
├── scripts/
│ ├── kpis.py # Cálculo de métricas clave
│ ├── forecast_model.py # Predicciones de consumo y precios
│ ├── optimization.py # Reglas básicas de optimización energética
│ └── export_firestore.py # Subida de resultados a Firebase
│
├── outputs/
│ ├── graficos/ # Imágenes generadas (consumo, solar, precios)
│ └── resultados.csv # Predicciones y recomendaciones exportadas
│
└── ANALISIS_DATOS.md # Este documento de referencia


---

## 🔹 Flujo de trabajo

1. **Carga y limpieza de datos**
   - Lectura de CSV con `pandas`.  
   - Normalización de columnas (`timestamp`, `consumo_kWh`, `solar_kWh`, `precio`, `clima`).  

2. **KPIs**
   - Consumo total, medio y máximo.  
   - % energía cubierta con solar.  
   - Coste energético total.  

3. **Análisis descriptivo**
   - Series temporales → consumo vs generación.  
   - Horas pico de consumo.  
   - Correlación clima ↔ consumo.  
   - Relación precio ↔ consumo.  

4. **Predicción**
   - Modelos con Prophet o ARIMA.  
   - Predicciones de 24h de consumo y costes.  

5. **Optimización**
   - Reglas básicas:
     - Cargar baterías cuando el precio es bajo.  
     - Vender excedente solar cuando el precio es alto.  
     - Posponer operaciones en horas caras.  

6. **Exportación**
   - Los resultados (KPIs, predicciones, recomendaciones) se guardan en Firestore.  
   - El frontend consume estos datos en tiempo real para visualización.  

---

## 🔹 Tecnologías usadas
- **pandas** → manipulación de datos.  
- **matplotlib / seaborn** → visualización.  
- **Prophet** → forecasting rápido.  
- **scikit-learn (opcional)** → modelos adicionales.  
- **Firebase Admin SDK** → subir resultados a Firestore.  

---

## ✅ Conclusión
La capa de análisis de datos convierte el dataset bruto en **información procesada y accionable**:  
- KPIs inmediatos,  
- predicciones futuras,  
- y recomendaciones para la toma de decisiones inteligentes en el puerto.
