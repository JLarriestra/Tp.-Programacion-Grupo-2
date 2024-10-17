import modulo_funciones.GLOBAL as g
from modulo_funciones.utiles import limpiar_pantalla
from modulo_funciones.equipo import equipo
from modulo_funciones.instruc import instrucciones
from modulo_funciones.login import login, cerrar_sesion
from modulo_funciones.admin import admin
from modulo_funciones.productos import manejar_menu_principal

def ejecutar():
    repetir = True
    while repetir:
        limpiar_pantalla()
        print("0- Volver al inicio")
        print("1- Ver productos")
        print("2- Ver descuentos")
        print("3- ver locales")
        print("4- Buscar")
        if(g.usuario):
            print("5- Administar")
            print("6- Cerrar sessión")
        else:
            print("5- Login")
     
        try:
            op = int(input("ingrese un valor: "))
            limpiar_pantalla()
            if op == 0:
                repetir = False
            elif op == 1:
                manejar_menu_principal()
            elif op == 5:
                if(g.usuario):
                    admin()
                else:
                    login()
            elif op == 6:
                cerrar_sesion()
        except:
            print("error")
        
def menu():
    repetir = True
    while repetir:
        limpiar_pantalla()
        print("1- equipo")
        print("2- instrucciones")
        print("3- ejecutar")
        print("4- salir")
        try:
            op = int(input("ingrese un valor: "))
            limpiar_pantalla()
            if op == 1:
                equipo()
            elif op == 2:
                instrucciones()
            elif op == 3:
                ejecutar()
            elif op == 4:
                repetir = False
            else:
                print("error")
        except:
            print("error")



if __name__ == "__main__":
    menu()




    




