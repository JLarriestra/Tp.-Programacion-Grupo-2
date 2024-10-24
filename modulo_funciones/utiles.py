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
    parsedJSON = json.dumps(nuevo, ensure_ascii=False, indent=4) 
    contenido = open(f"base_de_datos/{nombre}", "w",  encoding='utf-8')
    contenido.write(parsedJSON)
    contenido.close()

def imprimir_tabla(datos):
    ancho_columna = []

    for col in range(len(datos)):
        for item in range(len(datos[col])):
            if len(datos[col]) > len(ancho_columna): ancho_columna.append(0)
            max_ancho = max(ancho_columna[item], len(str(datos[col][item])))
            ancho_columna[item] = max_ancho

    linea_separadora = []

    for ancho in ancho_columna:
        linea_separadora.append('-'*(ancho+2))
    
    linea_separadora = "+".join(linea_separadora)

    print('+' + linea_separadora + '+')
    
    for fila in datos:
        contenido = []
        for i in range(len(fila)):
            espacio = " " * (ancho_columna[i] - len(str(fila[i])))
            contenido.append(f' {str(fila[i]) + espacio} ')
        print('|' + '|'.join(contenido) + '|')
        print('+' + linea_separadora + '+')