# ⚡ Puerto Inteligente - Dataset Energético

### Esto es un simulacro para la participación de una hackaton ###

## ✅ Confirmación del dataset como consumo energético de un puerto

El dataset contiene:

- **Consumo energético horario (kWh)** → refleja la demanda eléctrica del puerto.  
- **Producción solar local (kWh)** → representa la generación de paneles solares en el puerto.  
- **Clima (temperatura, viento, humedad)** → factores que afectan tanto al consumo como a la generación.  
- **Precio de electricidad (€/MWh)** → permite optimizar el coste energético.  

Estas estadísticas simulan un puerto real:

- **Consumo** → barcos atracados, grúas, refrigeración de contenedores, iluminación, oficinas portuarias.  
- **Solar** → posible instalación fotovoltaica del puerto.  
- **Clima** → impacta directamente en la operación (ej. más viento = barcos ajustan potencia).  
- **Precio** → clave para decidir cuándo consumir, almacenar o vender energía.  

---

## 🛠 Estructura del proyecto

### 🔧 Backend / Infraestructura
En el backend se implementará:

- **Ingesta de datos**: se recibirán en tiempo real los datos de consumo, generación solar, clima y precios.  
- **Almacenamiento**: los datos se guardarán en una base de datos tipo *TimescaleDB, InfluxDB o PostgreSQL*.  
- **Procesamiento de datos**:
  - Cálculo de KPIs: consumo neto, dependencia de la red, % de energía renovable usada.  
  - Balance energético: `consumo - generación`.  
  - Coste horario: `consumo * precio`.  
- **API**: se expondrá una API (Flask/FastAPI) que devolverá los datos procesados para el frontend y el análisis.

---

### 📊 Análisis de Datos
En esta capa se realizará:

- **Análisis descriptivo**:
  - Identificación de horas pico de consumo.  
  - Correlación entre clima y consumo (ej. frío aumenta consumo).  
  - Relación entre precios y consumo para optimización de costes.  
- **Predicción**:
  - Forecast de consumo horario mediante ARIMA, Prophet o regresión lineal.  
  - Predicción de costes energéticos según el mercado.  
  - Estimación de producción solar futura para planificación de uso.  
- **Optimización**:
  - Algoritmo que determina acciones automáticas:
    - Carga de baterías cuando el precio es bajo.  
    - Venta de energía solar excedente cuando el precio es alto.  
    - Posponer tareas no críticas (ej. carga de contenedores) a horas económicas.

---

### ⚙️ Automatización / Smart control
En esta capa se implementará:

- **Alertas automáticas**: notificación cuando el consumo supere un umbral o el precio sea elevado.  
- **Scheduling inteligente**: programación de operaciones del puerto basadas en las predicciones.  
- **Simulación de escenarios**:
  - Impacto de añadir más energía solar.  
  - Evaluación de introducir almacenamiento en baterías.  

Estas funcionalidades están alineadas con **VEO (automatización industrial)** y **Wärtsilä (operación eficiente)**.

---

### 🖥️ Frontend / Visualización
En el frontend se desarrollará un dashboard que mostrará:

- **Vista en tiempo real**: consumo actual, generación solar, coste instantáneo.  
- **Gráficos históricos**: consumo vs generación, coste horario, correlación clima ↔ consumo.  
- **Predicciones**: curvas de consumo esperado para las próximas 24h y costes previstos.  
- **Recomendaciones automáticas (semáforo)**:
  - 🟢 Verde → consumir normal.  
  - 🟡 Amarillo → mejor esperar.  
  - 🔴 Rojo → coste alto → ahorro o uso de batería.  

Tecnologías empleadas: **React + Chart.js/Recharts** o **Streamlit** para una solución rápida.

---

## 🚀 Conclusión
El proyecto implementará un sistema completo para un **puerto inteligente en Vaasa**:

- **Backend** → API con datos procesados.  
- **Análisis** → KPIs y predicciones de consumo/coste.  
- **Automatización** → reglas inteligentes para optimizar recursos y reducir emisiones.  
- **Frontend** → dashboard claro que muestre impacto real y recomendaciones de operación.
