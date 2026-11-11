Proyecto 1 - EDA Predict Future Sales
==============================

Análisis exploratorio de datos (EDA) del dataset **Predict Future Sales** de Kaggle (ventas diarias de 1C Company,
enero 2013 a octubre 2015).

**Integrantes:** Brady Monroy (15003165) y Luis Rodolfo Rodriguez

## 📓 Notebook del análisis

### ➡️ [01_exploratory_data_analysis.ipynb](notebooks/01_exploratory_data_analysis.ipynb)

Si GitHub no muestra el notebook, se puede ver aquí:
[abrir en nbviewer](https://nbviewer.org/github/15003165-code/Proyecto-1/blob/main/notebooks/01_exploratory_data_analysis.ipynb)

| Sección | Contenido |
|---|---|
| 1 | Carga de librerías y datos |
| 2 | Comprensión inicial del dataset |
| 3 | Validación de la estructura de los datos |
| 4 | Valores faltantes y duplicados |
| 5 | Análisis descriptivo general |
| 6 | Exploración temporal |
| 7 | Análisis comparativo entre sucursales y productos |
| 8 | Visualizaciones clave |
| 9 | Autocorrelación (ACF) y autocorrelación parcial (PACF) |
| 10 | Insights y conclusiones del EDA |

## Cómo ejecutarlo

1. Descargar los archivos de
   [Kaggle](https://www.kaggle.com/competitions/competitive-data-science-predict-future-sales/data) y colocarlos en
   `data/raw/` (no se suben al repositorio).
2. Instalar las librerías: `pip install -r requirements.txt`
3. Abrir y ejecutar `notebooks/01_exploratory_data_analysis.ipynb`.

Organización del proyecto
------------

Estructura basada en la plantilla cookiecutter de ciencia de datos.

    ├── LICENSE            <- Licencia del proyecto.
    ├── Makefile           <- Comandos útiles como `make data` o `make train`.
    ├── README.md          <- Este archivo: descripción general del proyecto.
    ├── data               <- Datos del proyecto (no se suben a GitHub).
    │   ├── external       <- Datos de fuentes externas.
    │   ├── interim        <- Datos intermedios ya transformados.
    │   ├── processed      <- Datos finales, listos para el modelo.
    │   └── raw            <- Datos originales de Kaggle, sin modificar.
    │
    ├── docs               <- Documentación del proyecto (Sphinx).
    │
    ├── models             <- Modelos entrenados y sus predicciones.
    │
    ├── notebooks          <- Notebooks de Jupyter. Aquí está el EDA:
    │                         `01_exploratory_data_analysis.ipynb`.
    │
    ├── references         <- Material de referencia (enunciado del proyecto, diccionarios de datos).
    │
    ├── reports            <- Reportes generados (HTML, PDF, etc.).
    │   └── figures        <- Gráficas generadas para los reportes.
    │
    ├── requirements.txt   <- Librerías necesarias para ejecutar el proyecto.
    │
    ├── setup.py           <- Permite instalar el proyecto con `pip install -e .`
    ├── src                <- Código fuente del proyecto.
    │   ├── __init__.py    <- Convierte `src` en un módulo de Python.
    │   │
    │   ├── data           <- Scripts para descargar o generar los datos.
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts para crear variables para el modelo.
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts para entrenar modelos y hacer predicciones.
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts para crear gráficas.
    │       └── visualize.py
    │
    └── tox.ini            <- Configuración para ejecutar pruebas con tox.


--------

<p><small>Proyecto basado en la plantilla <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science</a>.</small></p>
