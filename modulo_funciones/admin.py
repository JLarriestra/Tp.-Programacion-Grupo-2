from modulo_funciones.utiles import limpiar_pantalla, leer_archivo, escribir_archivo, imprimir_tabla
from modulo_funciones.locales import ver_mis_locales, crear_local
import modulo_funciones.GLOBAL as g

def validar_producto(name):
    producto = input(name)
    while producto == "":
        print("Ingresar de nuevo")
        producto = input(name)
    return producto

def ver_producto(producto):
    repetir = True;

    id = producto["id"]

    while repetir:
        limpiar_pantalla()

        print("ID:", id)
        print("Nombre:", producto["nombre"])
        print("Descripción:", producto["descripcion"])
        print("Precio:", producto["precio"])
        print("Tipo:", producto["tipo"])

        print()
        print("0- Volver")
        print("1- Editar")
        print("2- Borrar")
        print()


        try:
            op = int(input("ingrese un valor: "))
        
            if op == 0:
                repetir = False
            elif op == 1:
                bool = editar_producto(id)
                if bool:
                    repetir = False
            elif op == 2:
                bool = borrar_producto(id)
                if bool:
                    repetir = False
            else:
                print("Opción incorrecta, intente de nuevo.")
                input()
    
        except:
            print("Por favor, ingrese un número válido.")
            input()


def ver_mis_productos():
    if g.usuario and g.usuario["rol"] == "VENDEDOR":
        mostrar = True
    
        while mostrar:
            limpiar_pantalla()
            print(f"--- Mis Productos ---")
            print("")
            productos = leer_archivo("productos.json")
            
            contenido = {}
            n = 1

            tabla = [["ID", "Nombre", "Descripción", "Precio", "Tipo"]]

            for producto in productos:
                if producto["vendedor_id"] == g.usuario["id"]:
                    contenido[n] = producto
                    tabla.append([n, producto["nombre"], producto["descripcion"], producto["precio"], producto["tipo"]])
                    n += 1

            imprimir_tabla(tabla)
        
            print()

            try:
                print("0- Volver atras")
                id = int(input("Seleccionar ID del producto: "))
                if(id != 0):
                    if id in contenido:
                        ver_producto(contenido[id])
                    else:
                        print("No existe el producto")
                        input()
                else: 
                    mostrar = False
            except:
                print("Por favor, ingrese un número válido.")
                input()


def crear_producto():
    if g.usuario and g.usuario["rol"] == "VENDEDOR":
        limpiar_pantalla()
        print(f"--- Crear Producto ---")
        print()
        
        nombre = validar_producto("Nombre: ")
        descripcion = input("Descripción: ");
        tipo = validar_producto("Tipo: ")
        marca = validar_producto("Marca: ")
        precio = validar_producto("Precio: ")

        productos = leer_archivo("productos.json")
        producto = {
            "id": len(productos) + 1,
            "nombre": nombre,
            "descripcion": descripcion,
            "tipo": tipo,
            "marca": marca,
            "precio": precio,
            "valoracion": "",
            "vendedor_id": g.usuario["id"]
        }

        productos.append(producto)	
        
        escribir_archivo("productos.json", productos)

def editar_producto(id):
    limpiar_pantalla()
    print(f"--- Editar Producto ---")
    print()

    encontrado = False
    i = 0
    productos = leer_archivo("productos.json")
    
    while not encontrado and len(productos) > i:
        producto = productos[i]
        if(producto["id"] == id):
            nombre = input(f"Nombre ({producto['nombre']}): ")
            descripcion = input(f"Descripción ({producto['descripcion']}): ");
            tipo = input(f"Tipo ({producto['tipo']}): ")
            marca = input(f"Marca ({producto['marca']}): ")
            precio = input(f"Precio ({producto['precio']}): ")
    
            if(nombre):
                producto["nombre"]= nombre
            if(descripcion):
             producto["descripcion"]= descripcion
            if(tipo):
                producto["tipo"]= tipo
            if(marca):
                producto["marca"]= marca
            if(precio):
                producto["precio"]= precio

            print("Editado con exito")
            encontrado = True
        i += 1

    escribir_archivo("productos.json", productos)
    return encontrado

def borrar_producto(id):
    limpiar_pantalla()
    bool = False
    encontrado = False
    i = 0
    productos = leer_archivo("productos.json")

    while not encontrado and len(productos) > i:
        producto = productos[i]
        
        if(producto["id"] == id):
            confirmar = input("¿Estas seguro de borrarlo? (Si/No) ")
            if confirmar == "Si" or confirmar == "si":
                del productos[i]
                print("Borrado con exito")
                bool = True
            encontrado = True
        i += 1
    
    escribir_archivo("productos.json", productos)

    return bool

def ver_mis_reservas():
    if g.usuario and g.usuario["rol"] == "VENDEDOR":
        mostrar = True
    
        while mostrar:
            limpiar_pantalla()
            print(f"--- Mis Reservaciones ---")
            print("")
            reservas = leer_archivo("reservas.json")
            usuarios = leer_archivo("usuarios.json")
            usuarios_obj = {}

            for usuario in usuarios:
                usuarios_obj[usuario["id"]] = usuario["nombre"]
            
            n = 1

            tabla = [["ID", "Usuario", "Nombre", "Precio"]]

            for reserva in reservas:
                if reserva["vendedor_id"] == g.usuario["id"]:
                    tabla.append([n, usuarios_obj[reserva["usuario_id"]], reserva["producto"]["nombre"], reserva["producto"]["precio"]])
                    n += 1

            imprimir_tabla(tabla)
        
            print()
           
            try:
                print("0- Volver atras")
                id = int(input("Seleccionar opción: "))
                if(id != 0):
                   pass
                else: 
                    mostrar = False
            except:
                print("Por favor, ingrese un número válido.")
                input()

def admin():
    repetir = True
    while repetir:
        limpiar_pantalla()
        print("0- Volver atrás")
        print("1- Ver mis Productos")
        print("2- Crear Producto")
        print("3- Ver mis Locales")
        print("4- Crear Local")
        print("5- Ver mis Reservas")
        
        try:
            op = int(input("ingrese un valor: "))
            limpiar_pantalla()
            if op == 0:
                repetir = False
            elif op == 1:
                ver_mis_productos()
            elif op == 2:
                crear_producto()
            elif op == 3:
                ver_mis_locales()
            elif op == 4:
                crear_local()
            elif op == 5:
                ver_mis_reservas()
            else:
                print("Opción incorrecta, intente de nuevo.")
                input()

        except:
            print("error")
