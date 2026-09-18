# 📊 Proyecto ETL: Automatización y Análisis de Precios de Libros (Web Scraping)

¡Bienvenido a mi proyecto de automatización de datos! Este repositorio fue desarrollado como parte de mi camino como **Analista de Datos**. El objetivo es demostrar habilidades prácticas en el flujo completo de los datos: **Extracción (Scraping), Transformación (Limpieza y Validación)** y **Carga (Exportación de reportes estructurados)**.

El proyecto extrae información en tiempo real de la plataforma de simulación [*Books to Scrape*](https://toscrape.com).

---

## 🎯 Objetivos del Proyecto
*   **Automatizar la captura de datos:** Eliminar la recolección manual de información comercial mediante scripts automatizados en Python.
*   **Garantizar la calidad del dato (Data Cleaning):** Resolver problemas comunes de codificación de caracteres (`UTF-8`), eliminar ruido técnico (símbolos de moneda `£`) y transformar tipos de datos crudos a formatos numéricos (`float`) listos para el análisis.
*   **Generar Insights de valor:** Calcular métricas estadísticas clave del mercado (precios promedios, máximos y mínimos) para la toma de decisiones.

---

## 🏗️ Flujo del Ecosistema de Datos (Arquitectura)

Para mantener buenas prácticas de desarrollo y modularidad, el proyecto se divide en tres fases que reflejan el crecimiento de la solución:

1.  **Fase de Exploración (`market_price_scraper.py`):** Script inicial enfocado exclusivamente en la conexión HTTP y la inspección del árbol HTML (DOM) para extraer los primeros 20 productos de forma cruda.
2.  **Fase de Transformación (`market_data_cleaning.py`):** Implementación del análisis de datos con **Pandas**. Aquí aplico técnicas de limpieza, casteo de tipos de datos, análisis estadístico descriptivo básico y exportación en formato plano.
3.  **Fase de Producción (`run_market_pipeline.py`):** Un pipeline automatizado (Script robusto) que unifica la extracción y la transformación. Cuenta con control de errores (`try-except`) e introduce metadatos de auditoría como la **fecha exacta de monitoreo** (`Fecha_Monitoreo`).

---

## 🛠️ Stack Tecnológico Utilizado

*   **Python 3:** Lenguaje principal para la lógica del negocio.
*   **Requests:** Gestión y control de peticiones HTTP al servidor web.
*   **BeautifulSoup4:** Extracción, parseo y navegación de etiquetas HTML.
*   **Pandas:** Manipulación de DataFrames, limpieza de strings, análisis analítico-matemático y exportación.
*   **Datetime:** Inyección de marcas de tiempo para análisis de series temporales.

---

## 🚀 Instalación y Ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com
cd web_scraping
```

### 2. Instalar el entorno de librerías
Instala las dependencias necesarias ejecutando:
```bash
pip install requests beautifulsoup4 pandas
```

### 3. Ejecutar el Pipeline de Datos
Para correr el flujo completo y generar el reporte analítico automatizado, ejecuta en tu terminal:
```bash
python run_market_pipeline.py
```

---

## 📊 Entregables e Insights Generados

Al ejecutar el pipeline, el sistema procesa los datos y genera de forma automática el archivo **`reporte_precios_libros.csv`**, estructurado de la siguiente manera:

| Titulo | Precio | Fecha_Monitoreo |
| :--- | :--- | :--- |
| A Light in the Attic | 51.77 | 2026-09-18 |
| Tipping the Velvet | 53.74 | 2026-09-18 |
| ... | ... | ... |

### Métricas de Negocio impresas en consola:
El script realiza un análisis descriptivo inmediato del mercado, arrojando métricas clave como:
*   **Precio Promedio del Mercado** (utilizando funciones agregadas de Pandas).
*   **Identificación del Producto Estrella / Más Caro** (`idxmax()`).
*   **Identificación del Producto Más Económico** (`idxmin()`).

---
## 🎯 Próximos Pasos (Roadmap de Aprendizaje)
Como parte de mi crecimiento técnico, planeo expandir este proyecto implementando:
*   [ ] **Paginación automática:** Modificar el scraper para recorrer las 50 páginas del catálogo y extraer los 1,000 libros disponibles.
*   [ ] **Dashboard Visual:** Conectar el archivo `.csv` saliente a Power BI o Tableau para crear un reporte visual interactivo de los precios.
*   [ ] **Almacenamiento en Base de Datos:** Migrar la exportación de un archivo plano CSV a una base de datos relacional (SQLite / PostgreSQL).
