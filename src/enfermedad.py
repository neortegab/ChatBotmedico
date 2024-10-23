# Clase que representa una enfermedad.
class Enfermedad:
    #Inicializa una instancia de la clase Enfermedad.
    def __init__(self, nombre, tipo, sintomas):
        #Atributos:
        #nombre (str): El nombre de la enfermedad.
        #tipo (str): El tipo de enfermedad (por ejemplo, viral, bacteriana, etc.).
        #sintomas (list): Lista de síntomas asociados con la enfermedad.
        self.nombre = nombre
        self.tipo = tipo
        self.sintomas = sintomas
