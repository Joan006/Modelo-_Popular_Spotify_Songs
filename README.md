# Modelo de Machine Learning para Canciones Populares de Spotify

## Descripción del Proyecto

Este proyecto tiene como objetivo desarrollar un modelo de machine learning utilizando un dataset de canciones populares de Spotify. El dataset contiene diversas características de las canciones, como el número de streams, características musicales (bpm, energía, valencia, etc.), y su presencia en diferentes listas de reproducción y charts.

### Objetivos del Proyecto

1. **Análisis Exploratorio de Datos (EDA)**:
   - Realizar un análisis exploratorio para entender la distribución y las relaciones entre las diferentes características del dataset.

2. **Preprocesamiento de Datos**:
   - Manejar los valores faltantes mediante imputación.
   - Convertir características categóricas en variables numéricas.
   - Escalar las características numéricas para preparar los datos para el modelado.

3. **Modelado Predictivo**:
   - Desarrollar y evaluar diferentes modelos de machine learning para predecir la popularidad de las canciones y su inclusión en charts específicos.

4. **Evaluación del Modelo**:
   - Utilizar métricas de evaluación adecuadas para validar la efectividad de los modelos desarrollados.

### Estructura del Proyecto

- `data/`: Directorio para almacenar el dataset.
- `notebooks/`: Notebooks de Jupyter para análisis y experimentación.
- `scripts/`: Scripts de Python para preprocesamiento y modelado.
- `models/`: Directorio para almacenar los modelos entrenados.
- `reports/`: Reportes y visualizaciones generadas durante el análisis.

### Estado del Proyecto

- **Estado Actual**: En proceso
- **Próximos Pasos**:
  - Completar la etapa de preprocesamiento de datos.
  - Desarrollar y evaluar varios modelos de machine learning.
  - Refinar y optimizar los modelos seleccionados.

## Requisitos

Para ejecutar los scripts y notebooks de este proyecto, necesitarás tener instaladas las siguientes dependencias:

```sh
pip install pandas numpy scikit-learn matplotlib seaborn imbalanced-learn
