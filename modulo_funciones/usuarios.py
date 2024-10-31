from modulo_funciones.utiles import limpiar_pantalla, leer_archivo, escribir_archivo
import modulo_funciones.GLOBAL as g

def registrar_usuarios():
    limpiar_pantalla()
    usuarios = leer_archivo(g.ruta_usuarios)
    nuevo_usuario = input("Ingrese su nuevo nombre de usuario: ")
    
    cont = 0

    while cont < len(usuarios):
        usuario = usuarios[cont]
        if usuario['nombre'] == nuevo_usuario:
            print("El usuario ya existe")
            nuevo_usuario = input("Ingrese su nuevo nombre de usuario: ")
            cont = 0
        else:
            cont += 1

    nueva_contraseña = input("ingrese su nueva contraseña: ")

    usuario = {
        'id': len(usuarios) + 1,
        'nombre': nuevo_usuario,
        'contrasena': nueva_contraseña,
        "rol": "USUARIO"
    }

    usuarios.append(usuario)

    escribir_archivo(g.ruta_usuarios, usuarios)
    print("El usuario se ha creado correctamente")
    input()

def registrar_vendedores():
    limpiar_pantalla()
    usuarios = leer_archivo(g.ruta_usuarios)
    nuevo_usuario = input("Ingrese su nuevo nombre de vendedor: ")
    
    cont = 0

    while cont < len(usuarios):
        usuario = usuarios[cont]
        if usuario['nombre'] == nuevo_usuario:
            print("El vendedor ya existe")
            nuevo_usuario = input("Ingrese su nuevo nombre de vendedor: ")
            cont = 0
        else:
            cont += 1

    nueva_contraseña = input("ingrese su nueva contraseña: ")

    usuario = {
        'id': len(usuarios) + 1,
        'nombre': nuevo_usuario,
        'contrasena': nueva_contraseña,
        "rol": "VENDEDOR"
    }

    usuarios.append(usuario)

    escribir_archivo(g.ruta_usuarios, usuarios)
    print("El vendedor se ha creado correctamente")
    input()


def iniciar_sesion():
    print("--- Login ---\n")

    usuarios = leer_archivo(g.ruta_usuarios)

    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")


    usuario_encontrado = False
    cont = 0

    while not usuario_encontrado and cont < len(usuarios):
        usuario = usuarios[cont]
        if usuario['nombre'] == nombre_usuario and usuario['contrasena'] == contraseña:
            g.usuario = usuario
            usuario_encontrado = True
            print("Bienvenido")
        cont+=1

    if not usuario_encontrado:
        print("Usuario o Contraseña Incorrectas.")
        input()

def cerrar_sesion():
    g.usuario = {}
    
def registrarse():
    repetir = True
    while repetir:
        limpiar_pantalla()
        print("0- Volver atras")
        print("1- Registrarse como usuario")
        print("2- Registrarse como vendedor")
        
        try:
            op = int(input("Ingrese un valor: "))
            if op == 0:
                print("Saliendo...")
                repetir = False
            elif op == 1:
                registrar_usuarios()
            elif op == 2:
                registrar_vendedores()
            else:
                print("Esa opcion no existe, intente de nuevo.")
                input()
        except:
            print("Por favor, ingrese un número válido.")
            input()
