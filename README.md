# ⚡ Puerto Inteligente - Dataset Energético

## ✅ Confirmación del dataset como consumo energético de un puerto

El dataset contiene:

- **Consumo energético horario (kWh)** → la demanda eléctrica del puerto.  
- **Producción solar local (kWh)** → si el puerto tiene paneles solares.  
- **Clima (temperatura, viento, humedad)** → factores que afectan tanto a consumo como a generación.  
- **Precio de electricidad (€/MWh)** → permite optimizar costes.  

👉 Sí, tiene sentido asumir que son estadísticas de un puerto real:

- **Consumo** → barcos atracados, grúas, refrigeración de contenedores, iluminación, oficinas portuarias.  
- **Solar** → posible instalación fotovoltaica del puerto.  
- **Clima** → impacta en la operación (ej. más viento = barcos ajustan potencia).  
- **Precio** → clave para decidir cuándo consumir, almacenar o vender energía.  

---

## 🛠 Qué podrías hacer en cada capa

### 🔧 Backend / Infraestructura
- **Ingesta de datos**: recibir en tiempo real consumo, generación y clima (en la demo se puede simular con este CSV).  
- **Almacenamiento**: una base de datos tipo *TimescaleDB, InfluxDB o PostgreSQL*.  
- **Procesamiento**:
  - KPIs: consumo neto, dependencia de la red, % renovable usado.  
  - Balance energético: `consumo - generación`.  
  - Coste horario: `consumo * precio`.  

👉 En la hackathon basta con un **API simple** (Flask/FastAPI) que devuelva datos procesados para impresionar.

---

### 📊 Análisis de Datos
**Análisis descriptivo**  
- Horas pico de consumo → cuándo el puerto es más intensivo.  
- Correlación clima ↔ consumo → ej. frío aumenta consumo.  
- Relación precios ↔ consumo → optimización de costes.  

**Predicción**  
- Forecast de consumo (ARIMA, Prophet, regresión lineal).  
- Predicción de costes energéticos según el mercado.  
- Predicción de producción solar para planificar uso.  

**Optimización**  
- Algoritmo que recomiende acciones:  
  - Cargar baterías cuando el precio es bajo.  
  - Vender excedente solar cuando el precio es alto.  
  - Posponer tareas no críticas (ej. carga de contenedores) a horas baratas.  

---

### ⚙️ Automatización / Smart control
- **Alertas**: notificar cuando el consumo supera cierto umbral o el precio es demasiado alto.  
- **Scheduling inteligente**: programar operaciones del puerto en base al forecast.  
- **Simulación de escenarios**:  
  - ¿Qué pasa si añadimos más solar?  
  - ¿Qué pasa si introducimos almacenamiento en baterías?  

👉 Esto conecta directamente con **VEO (automatización industrial)** y **Wärtsilä (operación eficiente)**.

---

### 🖥️ Frontend / Visualización
Un dashboard atractivo marca la diferencia. Ideas de vistas:  

- **Vista en tiempo real**: consumo actual, generación solar, coste instantáneo.  
- **Gráficos históricos**: consumo vs generación, coste horario, correlación clima ↔ consumo.  
- **Predicciones**: curva de consumo esperado para las próximas 24h, costes previstos.  
- **Recomendaciones automáticas (semáforo)**:  
  - 🟢 Verde = consumir normal.  
  - 🟡 Amarillo = mejor esperar.  
  - 🔴 Rojo = coste alto → ahorrar o usar batería.  

👉 Tecnologías posibles:  
- Web rápida en **React + Chart.js/Recharts**.  
- O un dashboard rápido en **Streamlit**.  

---

## 🚀 Conclusión
Sí, este dataset tiene sentido como **consumo energético de un puerto en Vaasa**.  
Con él puedes cubrir todo el stack de una hackathon:  

- **Backend** → API con datos procesados.  
- **Análisis** → KPIs + predicciones de consumo/coste.  
- **Automatización** → reglas inteligentes para reducir costes y emisiones.  
- **Frontend** → dashboard claro que muestre *impacto real* y recomendaciones.  
