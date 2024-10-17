from modulo_funciones.utiles import limpiar_pantalla, leer_archivo, escribir_archivo

def ver_productos():
    limpiar_pantalla()
    print(f"--- Mis Productos ---")
    print("")
    productos = leer_archivo("productos.json")

    for producto in productos:
        print(producto["nombre"], "-", "$",producto["precio"])
        if(producto["descripcion"] != ""):
            print(producto["descripcion"]) 
        if(producto["valoracion"] != ""):
            print("Valoración", producto["valoracion"])
        print()

def crear_productos():
    print(f"--- Crear Producto ---")
    nombre = input("Nombre: ")
    descripcion = input("Descripción: ");
    tipo = input("Tipo: ")
    marca = input("Marca: ")
    precio = input("Precio: ")

    productos = leer_archivo("productos.json")
    producto = {
        "id": len(productos) + 1,
        "nombre": nombre,
        "descripcion": descripcion,
        "tipo": tipo,
        "marca": marca,
        "precio": precio,
        "valoracion": ""
    }

    productos.append(producto)	
	
    escribir_archivo("productos.json", productos)

def admin():
    repetir = True
    while repetir:
        limpiar_pantalla()
        print("0- Volver atrás")
        print("1- Ver mis Productos")
        print("2- Crear Producto")
        print("3- Editar Producto")
        print("4- Borrar Producto")
        print("5- Ver mis pedidos")
        
        try:
            op = int(input("ingrese un valor: "))
            limpiar_pantalla()
            if op == 0:
                repetir = False
            elif op == 1:
                ver_productos()
            elif op == 2:
                crear_productos()
            elif op == 3:
               pass

            if op != 0:
                input()

        except:
            print("error")
