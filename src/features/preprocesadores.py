"""Transformadores propios para el pipeline de Predict Future Sales.

Nota: en las clases no se definió una clase Mapper; el mapeo se hizo con un
diccionario y OrdinalEncoder. Esta es una versión propia, sencilla, que sigue
la misma idea de clase (fit/transform de scikit-learn).
"""
from sklearn.base import BaseEstimator, TransformerMixin


class Mapper(BaseEstimator, TransformerMixin):
    """Reemplaza los valores de una o más columnas usando un diccionario.

    Parameters
    ----------
    mappings : dict
        {columna: {valor_original: valor_nuevo}}
    unknown_value : str
        Valor que se pone si aparece algo que no está en el diccionario.
        Los valores vacíos (NaN) se dejan vacíos para que los impute el
        siguiente paso del pipeline.
    """

    def __init__(self, mappings, unknown_value="Otro"):
        self.mappings = mappings
        self.unknown_value = unknown_value

    def fit(self, X, y=None):
        # No aprende nada de los datos: el diccionario ya viene definido
        return self

    def transform(self, X):
        X = X.copy()
        for columna, diccionario in self.mappings.items():
            vacios = X[columna].isnull()                  # guardar dónde hay vacíos
            X[columna] = X[columna].map(diccionario)      # traducir con el diccionario
            X[columna] = X[columna].fillna(self.unknown_value)  # valores desconocidos
            X.loc[vacios, columna] = None                 # devolver los vacíos originales
        return X
