A = True
import json

def cargar_usuario(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
        return None

def guardar_usuarios(ruta_archivo, datos):
    with open(ruta_archivo, 'w') as archivo:
        json.dump(datos, archivo, indent = 4)

def registrar_usuarios(ruta_archivo):
    usuarios = cargar_usuario(ruta_archivo)
    nuevo_usuario = input("Ingrese su nuevo nombre de usuario:")
    nueva_contraseña = input("ingrese su nueva contraseña")
    while nuevo_usuario in usuarios:
        print("El usuario ya existe")
        nuevo_usuario = input("Ingrese su nuevo nombre de usuario: ")
    usuarios["usuarios"][nuevo_usuario] = nueva_contraseña
    guardar_usuarios(ruta_archivo,usuarios)
    print("El usuario se ha creado correctamente")

def iniciar_sesion(ruta_archivo):
    usuarios = cargar_usuario(ruta_archivo)
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if nombre_usuario in usuarios["usuarios"] and usuarios["usuarios"][nombre_usuario] == contraseña:
        print("Bienvenido")
    else:
        print("Usuario o Contraseña Incorrectas.")
    
def login_():
    global A
    ruta_archivos = 'Proyecto/base_de_datos/usuarios.json'
    while A:
        print("1- Iiniciar sesion.")
        print("2- Crear nuevo usuario")
        print("3- Sair")
        op = int(input("Ingrese uno de los numeros de las respectivas opciones: "))
        if op == 1:
            iniciar_sesion(ruta_archivos)
        elif op == 2:
            registrar_usuarios(ruta_archivos)
        elif op == 3:
            print("Saliendo...")
            A = False
        else:
            print("Esa opccion no existe, intente de nuevo.")

login_()