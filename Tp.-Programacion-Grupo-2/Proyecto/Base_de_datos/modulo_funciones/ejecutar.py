import os
def ejecutar():
    repetir = True
    while repetir:
        os.system("cls")
        print("1- comidas y bebidas")
        print("2- aparcamiento ")
        print("3- teatro")
        print("4- salir")
        try:
            op = int(input("ingrese un valor: "))

            if op == 1:
               
               pass
            elif op == 2:
               pass
            elif op == 3:
                pass
            elif op == 4:
                import main
                repetir=False
                
                
            else:
                print("error")
        
        except:
            print("error")
