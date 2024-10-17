def mostrar_menu_principal():
    print("Bienvenido al menu principal:")
    print("1. Alimentos")
    print("2. Productos")
    print("3. Salir")
    
def menu_starbucks():
    print("\n--- Menu de Starbucks ---")
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
    print("5. Regresar al menu principal")

def menu_rustica():
    print("\n--Menu de Rustica ---")
    print("1. Alfajor XL - $1000")
    print("2. Cheesecake - $2500")
    print("3. Chocotorta - $3000")
    print("4. Regresar al menu principal")

def menu_alimentos():
    print("\n--- Menu de Alimentos ---")
    print("1. Starbucks")
    print("2. Rustica")
    print("3. Regresar al menu principal")

def menu_ropa_y_accesorios():
    print("\n--- Ropa y Accesorios ---")
    print("1. Bufanda - $10000")
    print("2. Remera - $30000")
    print("3. Regresar al menu de productos")

def menu_otros():
    print("\n--- Otros ---")
    print("1. Termos - $15000")
    print("2. Mates - $5000")
    print("3. Regresar al menu de productos")

def menu_productos():
    print("\n--- Menu de Productos ---")
    print("1. Ropa y Accesorios")
    print("2. Otros")
    print("3. Regresar al menu principal")

def manejar_menu_principal():
    while True:
        mostrar_menu_principal()
        opcion = input("Elige una opción: ")

        if opcion == '1':
            while True:
                menu_alimentos()
                opcion_alimento = input("Elige una opción: ")
                
                # A completar, no olvidar o muerte!
                if opcion_alimento == '1':
                    while True:
                        menu_starbucks()
                        opcion_starbucks = input("Elige una bebida de Starbucks: ")
                        
                        if opcion_starbucks == '1':
                            print("Seleccionaste Latte.")
                            print("   Café espresso con leche vaporizada.")
                            print("   Valoración: ☆☆☆☆")
                        elif opcion_starbucks == '2':
                            print("Seleccionaste Capuccino.")
                            print("   Café espresso, leche vaporizada y abundante espuma de leche.")
                            print("   Valoración: ☆☆☆☆☆")
                        elif opcion_starbucks == '3':
                            print("Seleccionaste Flat White.")
                            print("   Shots de café ristretto con leche vaporizada que finaliza con un punto dibujado en la superficie.")
                            print("   Valoración: ☆☆☆")
                        elif opcion_starbucks == '4':
                            print("Seleccionaste Latte Macchiato.")
                            print("   Leche vaporizada con shots de café espresso que finaliza con un punto dibujado en la superficie.")
                            print("   Valoración: ☆☆☆☆")
                        elif opcion_starbucks == '5':
                            break  
                        else:
                            print("Opcion incorrecta, intente de nuevo.")
                
                elif opcion_alimento == '2':
                    while True:
                        menu_rustica()
                        opcion_rustica = input("Elige una opcion de Rustica: ")
                        
                        if opcion_rustica == '1':
                            print("Seleccionaaste Alfajor XL.")
                        elif opcion_rustica == '2':
                            print("Seleccionaste Cheesecake.")
                        elif opcion_rustica == '3':
                            print("Seleccionaste Chocotorta.")
                        elif opcion_rustica == '4':
                            break  
                        else:
                            print("Opcion incorrecta, intente de nuev.")
                
                elif opcion_alimento == '3':
                    break  
                else:
                    print("Opcion incorrecta, intente de nuevo.")
        
        elif opcion == '2':
            while True:
                menu_productos()
                opcion_producto = input("Elige una opcion: ")
                
                if opcion_producto == '1':
                    while True:
                        menu_ropa_y_accesorios()
                        opcion_ropa = input("Elige un producto: ")
                        
                        if opcion_ropa == '1':
                            print("Seleccionaste Bufanda.")
                        elif opcion_ropa == '2':
                            print("Seleccionaste Remera.")
                        elif opcion_ropa == '3':
                            break  
                        else:
                            print("Opcion incorrecta, intente de nuevo.")
                
                elif opcion_producto == '2':
                    while True:
                        menu_otros()
                        opcion_otros = input("Elige un producto de Otros: ")
                        
                        if opcion_otros == '1':
                            print("Seleccionaste Termos.")
                        elif opcion_otros == '2':
                            print("Seleccionaste Mates.")
                        elif opcion_otros == '3':
                            break  
                        else:
                            print("Opcion incorrecta, intente de nuevo.")
                
                elif opcion_producto == '3':
                    break  
                else:
                    print("Opcion incorrecta, intente de nuevo.")
        
        elif opcion == '3':
            print("Adios")
            break
        else:
            print("Opcion incorrecta, intente de nuevo.")


manejar_menu_principal()


#Opiniones
#Encuesta
#Estetica(?)
#Ubicacion
#Cambiar el break
#Marcar errores
#Limpiar cada vez que elija una opcion