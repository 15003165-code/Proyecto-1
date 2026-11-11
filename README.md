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

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
