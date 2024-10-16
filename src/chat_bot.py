from utils import cargar_enfermedades
from model import Model

class ChatBot:
    def __init__(self):
        self.enfermedades = cargar_enfermedades()
        self.model = Model(self.enfermedades)

    def iniciar_chat(self):
        print("Bienvenido al Chatbot de Diagnóstico de Enfermedades.")
        sintomas_usuario = input("Por favor, describe tus síntomas separados por comas: ").split(',')

        enfermedad_predicha = self.model.predecir_enfermedad([sintoma.strip() for sintoma in sintomas_usuario])

        print(f"\nPodrías tener: {enfermedad_predicha}")
