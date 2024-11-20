

def of_starbucks():
    limpiar_pantalla()
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


def menu_of():
    repetir = True
    while repetir:
        op = int(input("Elige una opción: "))
        
        try:
            if op == 0:
                repetir = False
            elif op == 1:
                of_starbucks()
            elif op == 2:
                of_rustica()
            elif op == 3:
                of_nescafe()
            else:
                print("Opción incorrecta, intente de nuevo.")
        except:
            print("Opción incorrecta, intente de nuevo.")
        
            
