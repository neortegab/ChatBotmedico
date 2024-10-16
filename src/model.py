import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

class Model:
    def __init__(self, enfermedades):
        self.enfermedades = enfermedades
        self.model = self.entrenar_modelo()

    def entrenar_modelo(self):
        # Crear DataFrame para los síntomas
        sintomas = []
        nombres = []
        
        for enfermedad in self.enfermedades:
            nombres.append(enfermedad.nombre)
            sintomas.append(' '.join(enfermedad.sintomas))

        # Crear un DataFrame con los síntomas y nombres
        df = pd.DataFrame({'sintomas': sintomas, 'nombre': nombres})

        # Crear un modelo de clasificación usando Naive Bayes
        modelo = make_pipeline(CountVectorizer(), MultinomialNB())
        modelo.fit(df['sintomas'], df['nombre'])
        return modelo

    def predecir_enfermedad(self, sintomas_usuario):
        sintomas_usuario = ' '.join(sintomas_usuario)
        prediccion = self.model.predict([sintomas_usuario])
        return prediccion[0]
