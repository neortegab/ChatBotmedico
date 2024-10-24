from fastapi import FastAPI
from pydantic import BaseModel
from src.utils import cargar_enfermedades
from src.model import Model

# Inicializar FastAPI
app = FastAPI()

# Definir un modelo de datos para la solicitud
class SintomasRequest(BaseModel):
    question: str

# Chatbot para diagnóstico
class ChatBot:
    def __init__(self):
        self.enfermedades = cargar_enfermedades()
        self.model = Model(self.enfermedades)

    def predecir_enfermedad(self, sintomas_usuario):
        # Predecir enfermedad basada en síntomas
        enfermedad_predicha = self.model.predecir_enfermedad(sintomas_usuario)
        return enfermedad_predicha

# Instancia del chatbot
chatbot = ChatBot()

# Ruta para el diagnóstico
@app.post("/diagnostico")
async def diagnostico(sintomas_request: SintomasRequest):
    sintomas_usuario = sintomas_request.question.split(' y ')
    sintomas_usuario = [sintoma.strip() for sintoma in sintomas_usuario]
    enfermedad_predicha = chatbot.predecir_enfermedad(sintomas_usuario)
    return {"answer": f"Tienes {enfermedad_predicha}"}

# Ejecutar con: uvicorn main:app --reload
