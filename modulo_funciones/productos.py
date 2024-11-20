import modulo_funciones.GLOBAL as g
from modulo_funciones.utiles import limpiar_pantalla, leer_archivo
from modulo_funciones.reservas import agregar_reserva

colores = ['\033[32m', '\033[35m',  '\033[31m']

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

def obtener_marcas():
    usuarios = leer_archivo("usuarios.json")

    marcas = []

    for usuario in usuarios:
        if usuario["rol"] == "VENDEDOR":
            marcas.append(usuario["nombre"])
    
    return marcas

def ver_productos(marca, color):
    productos = leer_archivo("productos.json")

    reset = '\033[0m'

    texto = convertir_a_ascii_art(marca)

    print()
    print(f"{color}{texto}")
    print(f"{reset}")

    print("0. Regresar al menu principal")

    productos_por_marca = []

    for producto in productos:
        if(producto["marca"] == marca):
            productos_por_marca.append(producto)
        
    for i in range(len(productos_por_marca)):
        producto = productos_por_marca[i]
        print(f"{i + 1} {producto['nombre']} - {producto['precio']}")
        print(f"   {producto['descripcion']}")
        print(f"   Valoración: {producto['valoracion']}")

    opcion = int(input("Elige una opción: "))

    if opcion >= 1 and opcion <= len(productos_por_marca):
        producto = productos_por_marca[opcion - 1]
        limpiar_pantalla()
        
        print(f"\nHas seleccionado {producto['nombre']}.")

        print("\n¿Cómo te gustaría que fuera tu pedido?")
        print("1. Para llevar")
        print("2. Para consumo local")
        print("3. Para reservar")

        consumo = input("Elige una opción: ")
        completado = False

        if consumo == '1':
            print(f"Tu {producto['nombre']} será para llevar.")
            completado = True
        elif consumo == '2':
            print(f"Tu {producto['nombre']} será para consumo local.")
            completado = True
        elif consumo == '3':
            if g.usuario and g.usuario["rol"] == "USUARIO":
                print(f"Tu {producto['nombre']} ha sido reservado.")
                agregar_reserva(g.usuario["id"], producto)
                completado = True
            else: 
                print("No tienes permisos para reservar productos.")
                input()
        else:
            print("Opción incorrecta, intenta de nuevo.")
        
         
        if completado:
            naranja = '\033[33m'
            reset = '\033[0m'

            print(f"{naranja}")
            print("""
    _  ____                _                                          
    (_)/ ___|_ __ __ _  ___(_) __ _ ___   _ __   ___  _ __   ___ _   _ 
    | | |  _| '__/ _` |/ __| |/ _` / __| | '_ \ / _ \| '__| / __| | | |
    | | |_| | | | (_| | (__| | (_| \__ \ | |_) | (_) | |    \__ \ |_| |
    |_|\____|_|  \__,_|\___|_|\__,_|___/ | .__/ \___/|_|    |___/\__,_|
                                        |_|                           
    ___ ___  _ __ ___  _ __  _ __ __ _| |                            
    / __/ _ \| '_ ` _ \| '_ \| '__/ _` | |                            
    | (_| (_) | | | | | | |_) | | | (_| |_|                            
    \___\___/|_| |_| |_| .__/|_|  \__,_(_)                            
                        |_|                                             
    """)
            print(f"{reset}")
            input()
    

def menu_alimentos(marcas):
    amarillo = '\033[93m'
    reset = '\033[0m'
    
    print(f"{amarillo}"
    """
███╗   ███╗███████╗███╗   ██╗██╗   ██╗    ██████╗ ███████╗                
████╗ ████║██╔════╝████╗  ██║██║   ██║    ██╔══██╗██╔════╝                
██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║    ██║  ██║█████╗                  
██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║    ██║  ██║██╔══╝                  
██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝    ██████╔╝███████╗                
╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝     ╚═════╝ ╚══════╝                
                                                                          
 █████╗ ██╗     ██╗███╗   ███╗███████╗███╗   ██╗████████╗ ██████╗ ███████╗
██╔══██╗██║     ██║████╗ ████║██╔════╝████╗  ██║╚══██╔══╝██╔═══██╗██╔════╝
███████║██║     ██║██╔████╔██║█████╗  ██╔██╗ ██║   ██║   ██║   ██║███████╗
██╔══██║██║     ██║██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║   ██║   ██║╚════██║
██║  ██║███████╗██║██║ ╚═╝ ██║███████╗██║ ╚████║   ██║   ╚██████╔╝███████║
╚═╝  ╚═╝╚══════╝╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚══════╝
""")
    print(f"{reset}")  

    print("0. Regresar al menu principal")  

    for i in range(len(marcas)):
        marca = marcas[i]
        print(f"{colores[i%len(colores)]}{i + 1}. {marca}{reset}")
    

def manejar_menu_principal():
    repetir = True
    while repetir:
        marcas = obtener_marcas()
        
        menu_alimentos(marcas)

        opcion_alimento = int(input("Elige una opción: "))
        
        limpiar_pantalla()
        
        if opcion_alimento == 0:
            repetir = False
        elif opcion_alimento >= 1 and opcion_alimento <= len(marcas):
            indice = opcion_alimento-1
            ver_productos(marcas[indice], colores[indice%len(colores)])
        else:
            print("Opción incorrecta, intente de nuevo.")
            
        limpiar_pantalla()


'''
 
def menu_starbucks():
    verde = '\033[32m'
    reset = '\033[0m'
    
    print(f"{verde}"
    """
███████╗████████╗ █████╗ ██████╗ ██████╗ ██╗   ██╗ ██████╗██╗  ██╗███████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║   ██║██╔════╝██║ ██╔╝██╔════╝
███████╗   ██║   ███████║██████╔╝██████╔╝██║   ██║██║     █████╔╝ ███████╗
╚════██║   ██║   ██╔══██║██╔══██╗██╔══██╗██║   ██║██║     ██╔═██╗ ╚════██║
███████║   ██║   ██║  ██║██║  ██║██████╔╝╚██████╔╝╚██████╗██║  ██╗███████║
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝
""")
    print(f"{reset}")
    print("0. Regresar al menu principal")
    print("1. Latte - $1500")
    print("   Café espresso con leche vaporizada.")
    print("   Valoración: ☆☆☆☆")
    print("2. Capuccino - $1900")
    print("   Café espresso, leche vaporizada y abundante espuma de leche.")
    print("   Valoración: ☆☆☆☆☆")
    print("3. Flat White - $1500")
    print("   Shots de café ristretto con leche vaporizada que finaliza con un punto dibujado en la superficie.")
    print("   Valoración: ☆☆☆")
    print("4. Latte Macchiato - $2000")
    print("   Leche vaporizada con shots de café espresso que finaliza con un punto dibujado en la superficie.")
    print("   Valoración: ☆☆☆☆")
    opcion = input("Elige una opción: ")
    
    if opcion == '0':
        limpiar_pantalla()
        manejar_menu_principal()
    elif opcion in ['1', '2', '3', '4']:
        producto = ["Latte", "Capuccino", "Flat White", "Latte Macchiato"][int(opcion) - 1]
        limpiar_pantalla()

        print(f"\nHas seleccionado {producto}.")

        print("\n¿Cómo te gustaría que fuera tu pedido?")
        print("1. Para llevar")
        print("2. Para consumo local")
        print("3. Para reservar")

        consumo = input("Elige una opción: ")

        if consumo == '1':
            print(f"Tu {producto} será para llevar.")
        elif consumo == '2':
            print(f"Tu {producto} será para consumo local.")
        elif consumo == '3':
            print(f"Tu {producto} ha sido reservado.")
            agregar_reserva(producto)
        else:
            print("Opción incorrecta, intenta de nuevo.")
        naranja = '\033[33m'

        reset = '\033[0m'

        print(f"{naranja}")
        print("""
  _  ____                _                                          
 (_)/ ___|_ __ __ _  ___(_) __ _ ___   _ __   ___  _ __   ___ _   _ 
 | | |  _| '__/ _` |/ __| |/ _` / __| | '_ \ / _ \| '__| / __| | | |
 | | |_| | | | (_| | (__| | (_| \__ \ | |_) | (_) | |    \__ \ |_| |
 |_|\____|_|  \__,_|\___|_|\__,_|___/ | .__/ \___/|_|    |___/\__,_|
                                     |_|                           
   ___ ___  _ __ ___  _ __  _ __ __ _| |                            
  / __/ _ \| '_ ` _ \| '_ \| '__/ _` | |                            
 | (_| (_) | | | | | | |_) | | | (_| |_|                            
  \___\___/|_| |_| |_| .__/|_|  \__,_(_)                            
                    |_|                                             
""")
        print(f"{reset}")
        
def menu_rustica():
    purpura = '\033[35m'
    reset = '\033[0m'
    
    print(f"{purpura}"
    """
██████╗ ██╗   ██╗███████╗████████╗██╗ ██████╗ █████╗ 
██╔══██╗██║   ██║██╔════╝╚══██╔══╝██║██╔════╝██╔══██╗
██████╔╝██║   ██║███████╗   ██║   ██║██║     ███████║
██╔══██╗██║   ██║╚════██║   ██║   ██║██║     ██╔══██║
██║  ██║╚██████╔╝███████║   ██║   ██║╚██████╗██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝ ╚═════╝╚═╝  ╚═╝
""")
    print(f"{reset}")
    print("0. Regresar al menu principal")
    print("1. Alfajor XL - $1000")
    print("2. Cheesecake - $2500")
    print("3. Chocotorta - $3000")
    
    opcion = input("Elige una opción: ")
    
    if opcion == '0':
        limpiar_pantalla()
        manejar_menu_principal()
        
    elif opcion in ['1', '2', '3']:
        producto = ["Alfajor XL", "Cheesecake", "Chocotorta"][int(opcion) - 1]
        limpiar_pantalla()
        print(f"\nHas seleccionado {producto}.")
        
        print("\n¿Cómo te gustaría que fuera tu pedido?")
        print("1. Para llevar")
        print("2. Para consumo local")
        print("3. Para reservar")
        
        consumo = input("Elige una opción: ")
        
        if consumo == '1':
            print(f"Tu {producto} será para llevar.")
        elif consumo == '2':
            print(f"Tu {producto} será para consumo local.")
        elif consumo == '3':
            print(f"Tu {producto} ha sido reservado.")
            if(g.usuario):
                print(g.usuario["id"])
                print("producto",producto)
                input()
                agregar_reserva(g.usuario["id"], producto)
                input()
        else:
            print("Opción incorrecta, intente de nuevo.")
        naranja = '\033[33m'

        reset = '\033[0m'

        print(f"{naranja}")
        print("""
  _  ____                _                                          
 (_)/ ___|_ __ __ _  ___(_) __ _ ___   _ __   ___  _ __   ___ _   _ 
 | | |  _| '__/ _` |/ __| |/ _` / __| | '_ \ / _ \| '__| / __| | | |
 | | |_| | | | (_| | (__| | (_| \__ \ | |_) | (_) | |    \__ \ |_| |
 |_|\____|_|  \__,_|\___|_|\__,_|___/ | .__/ \___/|_|    |___/\__,_|
                                     |_|                           
   ___ ___  _ __ ___  _ __  _ __ __ _| |                            
  / __/ _ \| '_ ` _ \| '_ \| '__/ _` | |                            
 | (_| (_) | | | | | | |_) | | | (_| |_|                            
  \___\___/|_| |_| |_| .__/|_|  \__,_(_)                            
                    |_|                                             
""")
        print(f"{reset}")
    else:
        print("Opción incorrecta, intente de nuevo.")
    


'''