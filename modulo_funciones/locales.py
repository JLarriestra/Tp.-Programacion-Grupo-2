from modulo_funciones.utiles import limpiar_pantalla, leer_archivo, escribir_archivo, imprimir_tabla
import modulo_funciones.GLOBAL as g

def validar_local(name):
    local = input(name)
    while local == "":
        print("Ingresar de nuevo")
        local = input(name)
    return local

def ver_local(local, mostrar = False):
    repetir = True;

    id = local["id"]

    while repetir:
        limpiar_pantalla()
        print("--- Detalles del Local ---")
        print("")

        print("Nombre:", local["nombre"])
        print("Dirección:", local["direccion"])

        print("")

        try:
            print("0- Volver atras")
            if mostrar:
                print("1- Editar")
                print("2- Borrar") 

            op = int(input("ingrese un valor: "))

            if op == 0:
                repetir = False
          
            elif mostrar and op == 1:
                bool =  editar_local(id)
                if bool:
                    repetir = False
            elif mostrar and op == 2:
                bool = borrar_local(id)
                if bool:
                    repetir = False
                        
            else:
                print("Opción incorrecta, intente de nuevo.")
                input()
        except:
            print("Por favor, ingrese un número válido.")
            input()

def ver_locales():
    repetir = True;

    while repetir:
        limpiar_pantalla()
        print("--- Locales ---")
        print("")

        locales = leer_archivo("locales.json")

        n = 1
 
        for local in locales:
            print(n,"-", local["nombre"])
            print(local["direccion"])
            print()
            n += 1

        try:
            print("0- Volver atras")
            id = int(input("Seleccionar nunmero del local: "))
            if(id != 0):
                ver_local(locales[id - 1])
            else:
                repetir = False
        except:
            print("Por favor, ingrese un número válido.")
            input()

def ver_mis_locales():
    if g.usuario and g.usuario["rol"] == "VENDEDOR":
        repetir = True
        
        while repetir:
            limpiar_pantalla()
            print("--- Mis Locales ---")
            print("")

            locales = leer_archivo("locales.json")

            contenido = {}
            n = 1

            tabla = [["ID", "Nombre", "Dirección"]]
    
            for local in locales:
                if local["vendedor_id"] == g.usuario["id"]:
                    contenido[n] = local
                    tabla.append([n, local["nombre"], local["direccion"]])
                    n += 1

            imprimir_tabla(tabla)
        
            print()

            try:
                print("0- Volver atras")
                id = int(input("Seleccionar numero del local: "))
                if(id != 0):
                    ver_local(contenido[id], True)
                    pass
                else:
                    repetir = False
            except:
                print("Por favor, ingrese un número válido.")
                input()
    
def crear_local():
    if g.usuario and g.usuario["rol"] == "VENDEDOR":
        limpiar_pantalla()
        print(f"--- Crear Local ---")
        print()
        
        nombre = validar_local("Nombre: ")
        direccion = validar_local("Direccción: ");

        locales = leer_archivo("locales.json")
        local = {
            "id": len(locales) + 1,
            "nombre": nombre,
            "direccion": direccion,
            "vendedor_id": g.usuario["id"]
        }

        locales.append(local)
        
        escribir_archivo("locales.json", locales)

def editar_local(id):
    limpiar_pantalla()
    print(f"--- Editar Local ---")
    print()

    encontrado = False
    i = 0
    locales = leer_archivo("locales.json")
    
    while not encontrado and len(locales) > i:
        local = locales[i]
        if(local["id"] == id):
            nombre = input(f"Nombre ({local['nombre']}): ")
            direccion = input(f"Dirección ({local['direccion']}): ");
    
            if(nombre):
                local["nombre"]= nombre
            if(direccion):
                local["direccion"]= direccion
            

            print("Editado con exito")
            encontrado = True
        
        i += 1

    escribir_archivo("locales.json", locales)
    return encontrado

def borrar_local(id):
    limpiar_pantalla()
    bool = False
    encontrado = False
    i = 0
    locales = leer_archivo("locales.json")

    while not encontrado and len(locales) > i:
        local = locales[i]
        
        if(local["id"] == id):
            confirmar = input("¿Estas seguro de borrarlo? (Si/No) ")

            if confirmar == "Si" or confirmar == "si":
                del locales[i]
                print("Borrado con exito")
                bool = True
            encontrado = True
        i += 1
    
    escribir_archivo("locales.json", locales)

    return bool