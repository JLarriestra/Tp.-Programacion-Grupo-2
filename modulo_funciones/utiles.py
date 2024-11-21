import os
import json
import modulo_funciones.GLOBAL as g

def limpiar_pantalla():
    if os.name == "nt": 
        os.system("cls")
    else:
        os.system("clear")

def leer_archivo(nombre):
    contenido = open(f"base_de_datos/{nombre}", "r", encoding='utf-8')
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

def convertir_a_ascii_art(texto):
    texto = texto.upper()
    filas = [""] * 6  
    
    for letra in texto:
        if letra in g.abcedario:
            arte_ascii = g.abcedario[letra].split("\n")
            for i in range(6):
                filas[i] += arte_ascii[i + 1]
        else:
            for i in range(6):
                filas[i] += " " * 10
    
    return "\n".join(filas)