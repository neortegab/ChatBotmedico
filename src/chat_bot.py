from utils import cargar_enfermedades
from model import Model

#  Clase que representa un chatbot de diagnóstico de enfermedades. Utiliza un modelo para predecir enfermedades basándose en los síntomas ingresados por el usuario.
class ChatBot:
    #Inicializa el chatbot cargando las enfermedades y el modelo de predicción.
    def __init__(self):
        #Carga las enfermedades mediante la función `cargar_enfermedades()` del módulo `utils` y crea una instancia de `Model` con la lista de enfermedades.
        self.enfermedades = cargar_enfermedades()
        self.model = Model(self.enfermedades)
    #Inicia el proceso de chat con el usuario.
    def iniciar_chat(self):
        #Solicita al usuario que ingrese sus síntomas y utiliza el modelo para identificar la enfermedad correspondiente. Luego imprime el resultado de la enfermedad.
        print("Bienvenido al Chatbot de Diagnóstico de Enfermedades.")
        sintomas_usuario = input("Por favor, describe tus síntomas separados por comas: ").split(',')
        enfermedad_predicha = self.model.predecir_enfermedad([sintoma.strip() for sintoma in sintomas_usuario])
        print(f"\nPodrías tener: {enfermedad_predicha}")
