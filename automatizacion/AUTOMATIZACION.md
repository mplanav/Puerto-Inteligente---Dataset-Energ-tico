# ⚙️ Automatización / Smart Control - Puerto Inteligente

La capa de **automatización** convierte los datos y predicciones en **acciones inteligentes**:  
alertas, recomendaciones y simulación de escenarios para optimizar el consumo energético del puerto.

---

## 🔹 Objetivos principales
1. Detectar condiciones críticas → consumo alto, precios caros, baja generación.  
2. Lanzar alertas en tiempo real.  
3. Recomendar acciones para reducir costes y emisiones.  
4. Simular escenarios de infraestructura (más solar, baterías).  

---

## 🔹 Estructura de carpetas

automatizacion/
│
├── scripts/
│ ├── reglas_alertas.py # Detección de condiciones críticas
│ ├── recomendaciones.py # Motor de reglas para sugerir acciones
│ ├── simulacion.py # Escenarios tipo "what-if"
│ └── export_firestore.py # Subida de resultados a Firebase
│
├── outputs/
│ ├── alertas.json # Últimas alertas generadas
│ ├── recomendaciones.json # Acciones sugeridas
│ └── escenarios.json # Resultados de simulaciones
│
└── AUTOMATIZACION.md # Este documento de referencia


---

## 🔹 Funcionalidades principales

### 1. Alertas en tiempo real
- **Consumo alto** → si `consumo_kWh > umbral`.  
- **Precio alto** → si `precio > X €/MWh`.  
- **Alta energía renovable** → si `solar / consumo > 40%`.  

Las alertas se guardan en Firebase para mostrarse en el dashboard.  

---

### 2. Recomendaciones automáticas
Un motor de reglas simple genera sugerencias como:  
- "Posponer carga de contenedores a la madrugada (02:00-04:00)".  
- "Usar energía solar entre 10:00-15:00".  
- "Reducir consumo en horas de precio alto".  

👉 Se representa con un sistema de **semáforo energético**:  
- 🟢 Verde = consumo normal.  
- 🟡 Amarillo = considerar posponer tareas.  
- 🔴 Rojo = evitar consumo alto o usar baterías.  

---

### 3. Simulación de escenarios (what-if analysis)
Permite explorar opciones estratégicas:  
- Añadir más solar (ej. +20%).  
- Introducir baterías (ej. 200 kWh).  
- Cambiar perfil de precios.  

Se muestran los resultados comparando **coste actual vs coste simulado**.  

---

## 🔹 Flujo de trabajo

1. **Entrada** → datos procesados del análisis (`consumo, solar, precio`).  
2. **Evaluación de reglas** → generación de alertas y recomendaciones.  
3. **Simulación opcional** → escenarios alternativos de infraestructura.  
4. **Exportación** → resultados almacenados en Firebase.  
5. **Frontend** → dashboard en tiempo real con alertas, semáforo y escenarios.  

---

## 🔹 Tecnologías usadas
- **Python** → scripts para reglas y simulaciones.  
- **Firebase Firestore** → almacenamiento en tiempo real de alertas y recomendaciones.  
- **Frontend (React/Streamlit)** → visualización de alertas y simulaciones.  

---

## ✅ Conclusión
La capa de automatización aporta el **factor diferencial**:  
- El puerto no solo ve datos, sino que recibe **alertas y recomendaciones inteligentes**.  
- Se pueden probar **escenarios futuros** que muestran impacto real.  
- Conecta directamente con las necesidades de **VEO (automatización industrial)** y **Wärtsilä (operación eficiente)**.
