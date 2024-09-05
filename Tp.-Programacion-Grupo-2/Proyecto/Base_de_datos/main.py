import os

def main():
    pass
def equipo():
    pass
def instrucciones():
    pass
def ejecutar():
    pass
def salir():
    pass
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
               import modulo_funciones.instruc
            elif op == 3:
                ejecutar()
            elif op == 4:
                salir()
            else:
                print("error")
            input()    
        except:
            print("error")
            input()


    





menu()
if __name__ == "__main__":
    main()




    




