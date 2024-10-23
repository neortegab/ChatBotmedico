import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
#Clase que representa un modelo de predicción de enfermedades basado en síntomas.
class Model:
    #Inicializa una instancia de la clase Model.
    def __init__(self, enfermedades):
        #Atributos:
        #enfermedades (list): Lista de enfermedades que contiene información sobre sus síntomas.
        #model (sklearn.pipeline.Pipeline): Modelo entrenado para predecir enfermedades basado en síntomas.
        self.enfermedades = enfermedades
        self.model = self.entrenar_modelo()
    # Entrena un modelo de clasificación utilizando el algoritmo Naive Bayes.
    def entrenar_modelo(self):
        # Crea un DataFrame a partir de los síntomas y nombres de las enfermedades,y entrena un modelo de clasificación que puede predecir la enfermedad
        #basándose en los síntomas ingresados
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
        
    #Predice la enfermedad basándose en los síntomas proporcionados por el usuario.
    def predecir_enfermedad(self, sintomas_usuario):
         #Args:
            #sintomas_usuario (list): Lista de síntomas ingresados por el usuario.
        sintomas_usuario = ' '.join(sintomas_usuario)
        prediccion = self.model.predict([sintomas_usuario])
            #Returns:
            #str: Nombre de la enfermedad predicha.
        return prediccion[0]
