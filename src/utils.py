#Utiliza la biblioteca pandas para leer el archivo 'enfermedades.json' y crea instancias de la clase Enfermedad para cada entrada en el archivo.
import pandas as pd
from enfermedad import Enfermedad

def cargar_enfermedades():
    # Cargar el archivo JSON utilizando pandas
    df = pd.read_json('enfermedades.json')
    enfermedades = []
    
    # Iterar a través de cada fila del DataFrame
    for index, row in df['enfermedades'].items():
        enfermedad = Enfermedad(row['nombre'], row['tipo'], row['sintomas'])
        enfermedades.append(enfermedad)
    #Returns:
        #list: Lista de instancias de la clase Enfermedad.
    return enfermedades
