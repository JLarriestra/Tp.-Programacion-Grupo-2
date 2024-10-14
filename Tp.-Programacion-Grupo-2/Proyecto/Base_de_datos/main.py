import os
import modulo_funciones.ejecutar as ejecutar_mod
import modulo_funciones.equipo as equipo_mod
import modulo_funciones.instruc as instruc_mod
def main():
    pass
def equipo():
    equipo_mod.equipo()
def instrucciones():
    instruc_mod.instrucciones()
def ejecutar():
    ejecutar_mod.ejecutar()
def salir():
    print("Saliendo del programa...")
def menu():    
    repetir = True
    while repetir:
        os.system("cls")
        print("1- equipo")
        print("2- instrucciones")
        print("3- ejecutar")
        print("4- salir")
        try:
            op = int(input("ingrese un valor: "))
            
            if op == 1:
                equipo()
            elif op == 2:
               instrucciones()
            elif op == 3:
                ejecutar()
            elif op == 4:
                salir()
                repetir=False
            
            else:
                print("error")
                input("presione enter para continuar")
        except:
            print("error")
            input("presione enter para continuar")


    





menu()
if __name__ == "__main__":
    main()




    




