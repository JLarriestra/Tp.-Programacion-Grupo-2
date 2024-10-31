from modulo_funciones.utiles import limpiar_pantalla, leer_archivo

def mostrar_menu_principal():
    print("Bienvenido al menu principal:")
    print("0. Salir")
    print("1. Alimentos")
    print("2. Productos")

def ver_productos(marca):
    productos = leer_archivo("productos.json")

    print(f"\n--- Menu de {marca} ---")

    for producto in productos:
        if(producto["marca"] == marca):
            print(producto["nombre"], "-", "$",producto["precio"])
            if(producto["descripcion"] != ""):
                print(producto["descripcion"]) 
            if(producto["valoracion"] != ""):
                print("Valoración", producto["valoracion"])
            print()
    
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
    

def menu_alimentos():
    amarillo = '\033[93m'
    reset = '\033[0m'
    verde = '\033[32m'
    rosa = '\033[35m'
    
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
    print(f"{verde}1. Starbucks{reset}")
    print(f"{rosa}2. Rustica{reset}")
    
'''def menu_ropa_y_accesorios():
    print("\n--- Ropa y Accesorios ---")
    print("1. Bufanda - $10000")
    print("2. Remera - $30000")
    print("3. Regresar al menu de productos")

def menu_otros():
    print("\n--- Otros ---")
    print("1. Termos - $15000")
    print("2. Mates - $5000")
    print("3. Regresar al menu de productos")

    opcion = input("Elige una opción: ")
    
    if opcion == '3':
        limpiar_pantalla()
        manejar_menu_principal()
        
    elif opcion in ['1', '2']:
        producto = ["Termos", "Mates"][int(opcion) - 1]
        limpiar_pantalla()
        print(f"\nHas seleccionado {producto}.")
    
        
        print("\n¿Cómo te gustaría que fuera tu pedido?")
        print("1. Para llevar")
        print("2. Para consumo local")
        
        consumo = input("Elige una opción: ")
        
        if consumo == '1':
            print(f"Tu {producto} será para llevar.")
        elif consumo == '2':
            print(f"Tu {producto} será para consumo local.")
        else:
            print("Opción no válida. Por favor, elige 1 o 2.")
        
        print("\nGracias por su compra!")
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")

def menu_productos():
    print("\n--- Menu de Productos ---")
    print("1. Ropa y Accesorios")
    print("2. Otros")
    print("3. Regresar al menu principal")'''''

def manejar_menu_principal():
    repetir = True
    while repetir:
        menu_alimentos()
        opcion_alimento = input("Elige una opción: ")
        limpiar_pantalla()
        
        if opcion_alimento == '0':
            repetir = False
        elif opcion_alimento == '1':
            menu_starbucks()
        elif opcion_alimento == '2':
            menu_rustica()
        else:
            print("Opción incorrecta, intente de nuevo.")
            
        if opcion_alimento != '0':
            input()
        limpiar_pantalla()
