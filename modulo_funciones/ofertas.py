import modulo_funciones.GLOBAL as g
from modulo_funciones.utiles import limpiar_pantalla, leer_archivo, convertir_a_ascii_art
from modulo_funciones.reservas import agregar_reserva

colores = ['\033[32m', '\033[35m',  '\033[31m']


def obtener_marcas():
    usuarios = leer_archivo("usuarios.json")

    marcas = []

    for usuario in usuarios:
        if usuario["rol"] == "VENDEDOR":
            marcas.append({"id": usuario["id"], "nombre": usuario["nombre"]})
    
    return marcas

def obtener_productos():
    productos = leer_archivo("productos.json")

    productos_obj = {}

    for producto in productos:
        productos_obj[producto["id"]] = producto

    return productos_obj

def ver_ofertas(marca, color):
    ofertas = leer_archivo("ofertas.json")
    productos = obtener_productos()
    
    ofertas_por_marca = []

    reset = '\033[0m'

    texto = convertir_a_ascii_art(marca["nombre"])

    print()
    print(f"{color}{texto}")
    print(f"{reset}")
    

    for oferta in ofertas:
        if(oferta["vendedor_id"] == marca["id"]):
            ofertas_por_marca.append(oferta)

    i = 1
    for oferta in ofertas_por_marca:
        descuento = ""
        nombres = []
        precio = 0
        for p in oferta["productos"]:
            precio += int(productos[p["id"]]['precio']) * p["cantidad"]

            if(p["cantidad"] > 1):
                nombres.append(f"{p['cantidad']} {productos[p['id']]['nombre']}")
            else:
                nombres.append(productos[p["id"]]["nombre"])

        if(oferta["descuento"] > 0):
            precio = precio - (precio * (oferta["descuento"]/100))
            descuento = f" {oferta['descuento']}%off"

        

        if(len(oferta["promo"]) > 0):
            precio = oferta["promo"][1] * precio


        nombre_final = " + ".join(nombres)


        promo = oferta["promo"]

        
        oferta["precio"] = precio

        if(len(promo) > 0):
            oferta["nombre"] = f"{promo[0]}x{promo[1]} {nombre_final}"
        else:
            if(len(oferta["productos"]) > 1):
                oferta["nombre"] = f"{nombre_final}"
            else:
                oferta["nombre"] = f"{nombre_final}{descuento}"
        print(f"{i}. {oferta['nombre']} - ${precio}")


        i+=1


    opcion = int(input("Elige una opción: "))

            
    if opcion >= 1 and opcion <= len(ofertas_por_marca):
        oferta = ofertas_por_marca[opcion - 1]
        limpiar_pantalla()
        
        print(f"\nHas seleccionado {oferta['nombre']}.")

        print("\n¿Cómo te gustaría que fuera tu pedido?")
        print("1. Para llevar")
        print("2. Para consumo local")
        print("3. Para reservar")

        consumo = input("Elige una opción: ")
        completado = False

        if consumo == '1':
            print(f"Tu {oferta['nombre']} será para llevar.")
            completado = True
        elif consumo == '2':
            print(f"Tu {oferta['nombre']} será para consumo local.")
            completado = True
        elif consumo == '3':
            if g.usuario and g.usuario["rol"] == "USUARIO":
                print(f"Tu {oferta['nombre']} ha sido reservado.")
                oferta_seleccionado = {
                    "id": oferta["id"],
                    "vendedor_id": oferta["vendedor_id"],
                    "nombre": oferta["nombre"],
                    "precio": oferta["precio"],
                    
                }
                agregar_reserva(g.usuario["id"], oferta_seleccionado)
                completado = True
            else: 
                print("No tienes permisos para reservar ofertas.")
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
    

def menu_ofertas(marcas):
    amarillo = '\033[93m'
    reset = '\033[0m'
    
    print(f"{amarillo}"
    """
 ██████╗ ███████╗███████╗██████╗ ████████╗ █████╗ ███████╗
██╔═══██╗██╔════╝██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔════╝
██║   ██║█████╗  █████╗  ██████╔╝   ██║   ███████║███████╗
██║   ██║██╔══╝  ██╔══╝  ██╔══██╗   ██║   ██╔══██║╚════██║
╚██████╔╝██║     ███████╗██║  ██║   ██║   ██║  ██║███████║
 ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝
""")
    print(f"{reset}")  

    print("0. Regresar al menu principal")  

    for i in range(len(marcas)):
        marca = marcas[i]
        print(f"{colores[i%len(colores)]}{i + 1}. {marca['nombre']}{reset}")
    


def menu_of():
    repetir = True
    while repetir:
        marcas = obtener_marcas()
        
        menu_ofertas(marcas)

        opcion_alimento = int(input("Elige una opción: "))
        
        limpiar_pantalla()
        
        if opcion_alimento == 0:
            repetir = False
        elif opcion_alimento >= 1 and opcion_alimento <= len(marcas):
            indice = opcion_alimento-1
            ver_ofertas(marcas[indice], colores[indice%len(colores)])
        else:
            print("Opción incorrecta, intente de nuevo.")
            
        limpiar_pantalla()

'''
def menu_of():
    repetir = True
    amarillo = '\033[93m'
    reset = '\033[0m'
    verde = '\033[32m'
    rosa = '\033[35m'
    rojo = '\033[91m'
    while repetir:
       
        print(f"{amarillo}"

"""
 ██████╗ ███████╗███████╗██████╗ ████████╗ █████╗ ███████╗
██╔═══██╗██╔════╝██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔════╝
██║   ██║█████╗  █████╗  ██████╔╝   ██║   ███████║███████╗
██║   ██║██╔══╝  ██╔══╝  ██╔══██╗   ██║   ██╔══██║╚════██║
╚██████╔╝██║     ███████╗██║  ██║   ██║   ██║  ██║███████║
 ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝
       """)
        print(f"{reset}")
        print("0. Regresar al menu principal")  
        print(f"{verde}1. Starbucks{reset}")
        print(f"{rosa}2. Rustica{reset}")
        print(f"{rojo}3. Nescafe{reset}")
        op = int(input("Elige una opción: "))
        try:
            if op == 0:
                repetir = False
            elif op == 1:
                limpiar_pantalla()
                of_starbucks()
            elif op == 2:
                limpiar_pantalla()
                of_rustica()
            elif op == 3:
                limpiar_pantalla()
                of_nescafe()
            else:
                limpiar_pantalla()
                print("Opción incorrecta, intente de nuevo.")
        except:
            limpiar_pantalla()
            print("Opción incorrecta, intente de nuevo.")


    

def of_starbucks():

    limpiar_pantalla()
    a = True
    while a == True:
        
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
        print("0. VOlver atras")
        print("1. Desayuno - 5000")
        print("   Flath White + 2 medialunas")
        print("2. 50% de descuento en caeteria")
        print("3. Gran desayuno - 9500")
        print("   2 Latte + 4 medialinas")
        try:
            op = int(input("Eligue una opcion: "))
            if op == 0:
                limpiar_pantalla()
                a = False
            elif op in [1, 2, 3]:
                producto = ["Desayuno", "50% en cafeteria", "Gran Desayuno"][int(op) - 1]
                limpiar_pantalla()

                print(f"Has seleccionado {producto}.")

                print("¿Cómo te gustaría que fuera tu pedido?")
                print("1. Para llevar")
                print("2. Para consumo local")
                print("3. Para reservar")

                consumo = int(input("Elige una opción: "))

                if consumo == 1:
                    print(f"Tu {producto} será para llevar.")
                elif consumo == 2:
                    print(f"Tu {producto} será para consumo local.")
                elif consumo == 3:
                    print(f"Tu {producto} ha sido reservado.")
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
        except:
            print("opcion incorrecta, intente de nuevo")
def of_nescafe():
    limpiar_pantalla()
    a = True
    while a == True:
        
        rojo = '\033[91m'
        reset = '\033[0m'
    
        print(f"{rojo}"
"""
███╗   ██╗███████╗███████╗ ██████╗ █████╗ ███████╗███████╗
████╗  ██║██╔════╝██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝
██╔██╗ ██║█████╗  ███████╗██║     ███████║█████╗  █████╗  
██║╚██╗██║██╔══╝  ╚════██║██║     ██╔══██║██╔══╝  ██╔══╝  
██║ ╚████║███████╗███████║╚██████╗██║  ██║██║     ███████╗
╚═╝  ╚═══╝╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚══════╝
       """)
        print(f"{reset}")
    
        print("0. VOlver atras")
        print("1. Desayuno - 5000")
        print("   Flath White + 2 medialunas")
        print("2. 50% de descuento en caeteria")
        print("3. Gran desayuno - 9500")
        print("   2 Latte + 4 medialinas")
        try:
            op = int(input("Eligue una opcion: "))
            if op == 0:
                limpiar_pantalla()
                a = False
            elif op in [1, 2, 3]:
                producto = ["Desayuno", "50% en cafeteria", "Gran Desayuno"][int(op) - 1]
                limpiar_pantalla()

                print(f"Has seleccionado {producto}.")

                print("¿Cómo te gustaría que fuera tu pedido?")
                print("1. Para llevar")
                print("2. Para consumo local")
                print("3. Para reservar")

                consumo = int(input("Elige una opción: "))

                if consumo == 1:
                    print(f"Tu {producto} será para llevar.")
                    a = False
                elif consumo == 2:
                    print(f"Tu {producto} será para consumo local.")
                    a = False
                elif consumo == 3:
                    print(f"Tu {producto} ha sido reservado.")
                    a = False
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
        except:
            print("opcion incorrecta, intente de nuevo")

def of_rustica():
    marca = {"id": 3}
    ver_ofertas(marca)
    return
    limpiar_pantalla()
    a = True
    while a == True:
        
        rosa = '\033[35m'
        reset = '\033[0m'
        print(f"{rosa}"
"""
██████╗ ██╗   ██╗███████╗████████╗██╗ ██████╗ █████╗ 
██╔══██╗██║   ██║██╔════╝╚══██╔══╝██║██╔════╝██╔══██╗
██████╔╝██║   ██║███████╗   ██║   ██║██║     ███████║
██╔══██╗██║   ██║╚════██║   ██║   ██║██║     ██╔══██║
██║  ██║╚██████╔╝███████║   ██║   ██║╚██████╗██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝ ╚═════╝╚═╝  ╚═╝
""")
        print(f"{reset}")
        print("0. VOlver atras")
        print("1. 2x1 Alfajor XL - $1600")
        print("2. Cheesecake 20%off - $2000")
        print("3. Chocotorta + Cheescake - $4600")
        try:
            op = int(input("Eligue una opcion: "))
            if op == 0:
                limpiar_pantalla()
                a = False
            elif op in [1, 2, 3]:
                producto = ["2x1 Alfajor XL", "Chescake 20% off", "Chocotorta + Cheescake"][int(op) - 1]
                limpiar_pantalla()

                print(f"Has seleccionado {producto}.")

                print("¿Cómo te gustaría que fuera tu pedido?")
                print("1. Para llevar")
                print("2. Para consumo local")
                print("3. Para reservar")

                consumo = int(input("Elige una opción: "))

                if consumo == 1:
                    print(f"Tu {producto} será para llevar.")
                elif consumo == 2:
                    print(f"Tu {producto} será para consumo local.")
                elif consumo == 3:
                    print(f"Tu {producto} ha sido reservado.")
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
        except:
            print("opcion incorrecta, intente de nuevo")
'''
