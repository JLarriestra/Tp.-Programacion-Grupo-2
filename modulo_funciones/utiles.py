import os
import json

def limpiar_pantalla():
    if os.name == "nt": 
        os.system("cls")
    else:
        os.system("clear")

def leer_archivo(nombre):
    contenido = open(f"base_de_datos/{nombre}", "r")
    lineas = contenido.read()
    contenido.close()
	
    return json.loads(lineas)

def escribir_archivo(nombre, nuevo):
    parsedJSON = json.dumps(nuevo, indent=4) 
    contenido = open(f"base_de_datos/{nombre}", "w")
    contenido.write(parsedJSON)
    contenido.close()