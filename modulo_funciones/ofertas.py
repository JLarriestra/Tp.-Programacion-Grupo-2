from modulo_funciones.utiles import limpiar_pantalla

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


