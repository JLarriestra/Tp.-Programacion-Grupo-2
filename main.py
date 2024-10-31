import modulo_funciones.GLOBAL as g
from modulo_funciones.utiles import limpiar_pantalla
from modulo_funciones.equipo import equipo
from modulo_funciones.instruc import instrucciones
# from modulo_funciones.login import login, cerrar_sesion
from modulo_funciones.admin import admin
from modulo_funciones.productos import manejar_menu_principal
from modulo_funciones.locales import ver_locales
from modulo_funciones.usuarios import iniciar_sesion, registrarse, cerrar_sesion

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
            if(g.usuario["rol"] == "VENDEDOR"):
                print("5- Administar")
            else:
                print("5- Ver mis reservas")
            print("6- Cerrar sessión")
        else:
            print("5- Login")
            print("6- Registrarse")
     
        try:
            op = int(input("ingrese un valor: "))
            limpiar_pantalla()
            if op == 0:
                repetir = False
            elif op == 1:
                manejar_menu_principal()
            elif op == 3:
                ver_locales()
            elif op == 5:
                if(g.usuario):
                    if(g.usuario["rol"] == "VENDEDOR"):
                        admin()
                    else:
                        pass
                else:
                    iniciar_sesion()
            elif op == 6:
                if(g.usuario):
                    cerrar_sesion()
                else:
                    registrarse()
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




    




