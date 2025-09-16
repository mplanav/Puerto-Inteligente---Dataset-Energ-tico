# 🖥️ Frontend / Visualización - Puerto Inteligente

El **frontend** será la capa encargada de mostrar en tiempo real:  
- el consumo energético del puerto,  
- las predicciones futuras,  
- y las recomendaciones inteligentes generadas por la automatización.  

El objetivo es que el dashboard sea **claro, visual y fácil de entender**, incluso para alguien no técnico.

---

## 🔹 Objetivos principales
1. Mostrar **datos en tiempo real** de consumo, generación y costes.  
2. Visualizar **gráficos históricos** y predicciones.  
3. Presentar **alertas y recomendaciones** con un sistema de semáforo.  
4. Permitir **comparar escenarios simulados**.  

---

## 🔹 Estructura de carpetas

frontend/
│
├── src/
│ ├── components/
│ │ ├── RealTimeCard.jsx # Vista de datos en tiempo real
│ │ ├── Charts.jsx # Gráficos históricos y predicciones
│ │ ├── AlertsPanel.jsx # Alertas en tiempo real
│ │ ├── Recommendations.jsx # Semáforo energético y consejos
│ │ └── Scenarios.jsx # Comparación de escenarios simulados
│ │
│ ├── services/
│ │ └── firebase.js # Conexión con Firebase Firestore
│ │
│ ├── pages/
│ │ └── Dashboard.jsx # Página principal del dashboard
│ │
│ ├── App.jsx # Configuración principal
│ └── index.js # Entrada del proyecto
│
├── public/
│ └── index.html
│
└── FRONTEND.md # Este documento de referencia


---

## 🔹 Vistas principales

### 1. **Vista en tiempo real**
- Consumo actual (kWh).  
- Producción solar actual.  
- Precio instantáneo.  
👉 Se presenta como tarjetas numéricas grandes con colores.  

---

### 2. **Gráficos históricos**
- Consumo vs generación solar (últimas 24h).  
- Coste horario.  
- Clima vs consumo.  

👉 Representados con **líneas y barras interactivas** (Chart.js / Recharts).  

---

### 3. **Predicciones**
- Curva de consumo esperado (24h futuras).  
- Costes energéticos previstos.  
👉 Gráfico en área/línea con valores proyectados.  

---

### 4. **Alertas y recomendaciones**
- Panel lateral con **alertas recientes**.  
- Sistema de **semáforo energético**:  
  - 🟢 Verde = consumo normal.  
  - 🟡 Amarillo = posponer algunas tareas.  
  - 🔴 Rojo = precio alto → ahorrar/usar baterías.  

---

### 5. **Escenarios simulados**
- Comparación **actual vs simulado** (ej. con +20% solar o baterías).  
- Visualización de diferencia en **coste total y emisiones**.  

---

## 🔹 Flujo de datos
1. **Firebase Firestore** almacena datos procesados, predicciones y recomendaciones.  
2. El **frontend escucha en tiempo real** los cambios.  
3. Los **componentes del dashboard** actualizan métricas, gráficos y alertas instantáneamente.  

---

## 🔹 Tecnologías usadas
- **React** → framework principal.  
- **Chart.js / Recharts** → gráficos interactivos.  
- **Firebase SDK** → conexión en tiempo real con la base de datos.  
- **TailwindCSS** → diseño rápido y limpio.  
- **(Opcional) Streamlit** → si se quiere un prototipo aún más rápido.  

---

## ✅ Conclusión
El **frontend** es la capa visible del sistema y será el **gancho visual** para el jurado:  
- Muestra métricas clave y predicciones en tiempo real.  
- Presenta alertas y recomendaciones de manera intuitiva.  
- Permite explorar escenarios futuros de forma visual.  

Un dashboard atractivo y funcional hará que el proyecto destaque frente a la competencia.
