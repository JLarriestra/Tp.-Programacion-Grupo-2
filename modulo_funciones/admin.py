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

def obtener_productos(usuario):
    productos = leer_archivo("productos.json")

    productos_obj = {}

    for producto in productos:
        if producto["vendedor_id"] == usuario["id"]:
            productos_obj[producto["id"]] = producto

    return productos_obj

def ver_mis_ofertas():
      if g.usuario and g.usuario["rol"] == "VENDEDOR":
        mostrar = True
    
        while mostrar:
            limpiar_pantalla()
            print(f"--- Mis Ofertas ---")
            print("")
            ofertas = leer_archivo("ofertas.json")
            productos = obtener_productos(g.usuario)
            
            n = 1

            tabla = [["ID", "Nombre", "Descuento", "Promo", "Precio"]]
            
            contenido = {}

            for oferta in ofertas:
                if oferta["vendedor_id"] == g.usuario["id"]:
                    contenido[n] = oferta
                    descuento = ""
                    nombres = []
                    precio = 0

                    for p in oferta["productos"]:
                        precio += int(productos[p["id"]]['precio']) * p["cantidad"]

                        if(p["cantidad"] > 1):
                            nombres.append(f"{p['cantidad']} {productos[p['id']]['nombre']}")
                        else:
                            nombres.append(productos[p["id"]]["nombre"])


                    if(oferta["descuento"] > 0):
                        precio = precio - (precio * (oferta["descuento"]/100))
                        descuento = f"{oferta['descuento']}%"
                    else:
                        descuento = "0%"

                    if(len(oferta["promo"]) > 0):
                        precio = oferta["promo"][1] * precio

                        
                    nombre_final = " + ".join(nombres)


                    promo = oferta["promo"]
                   
                    if(len(promo) > 0):
                        tabla.append([n, nombre_final, descuento, f"{promo[0]}x{promo[1]}", f"{precio}"])
                    else:
                        tabla.append([n, nombre_final, descuento, 0, f"{precio}"])

                    n += 1

            imprimir_tabla(tabla)
        
            print()
           
            try:
                print("0- Volver atras")
                
                id = int(input("Seleccionar opción: "))
                
                if(id != 0):
                    if id in contenido:
                        ver_oferta(contenido[id])
                    else:
                        print("No existe la oferta")
                        input()
                else: 
                    mostrar = False
            except:
                print("Por favor, ingrese un número válido.")
                input()


def ver_oferta(oferta):
    repetir = True
    
    id = oferta["id"]

    while repetir:
        limpiar_pantalla()

        descuento = ""
        nombres = []
        precio = 0

        productos = obtener_productos(g.usuario)

        for p in oferta["productos"]:
            precio += int(productos[p["id"]]['precio']) * p["cantidad"]

            if(p["cantidad"] > 1):
                nombres.append(f"{p['cantidad']} {productos[p['id']]['nombre']}")
            else:
                nombres.append(productos[p["id"]]["nombre"])


        if(oferta["descuento"] > 0):
            precio = precio - (precio * (oferta["descuento"]/100))
            descuento = f"{oferta['descuento']}%"
        else:
            descuento = "0%"

        if(len(oferta["promo"]) > 0):
            precio = oferta["promo"][1] * precio

                        
        nombre_final = " + ".join(nombres)


        promo = oferta["promo"]


        print("ID:", id)
        print("Nombre:", nombre_final)
        print("Descuento:", descuento)
        if(len(promo) > 0):
            print("Promo:", f"{promo[0]}x{promo[1]}")
        else:
            print("Promo:", 0)
        
        print("Precio:", precio)
                   
        
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
                bool = editar_oferta(id)
                if bool:
                    repetir = False
            elif op == 2:
                pass
                bool = borrar_oferta(id)
                if bool:
                    repetir = False
            else:
                print("Opción incorrecta, intente de nuevo.")
                input()
    
        except:
            print("Por favor, ingrese un número válido.")
            input()

def crear_oferta():
     if g.usuario and g.usuario["rol"] == "VENDEDOR":
       
        ofertas = leer_archivo("ofertas.json")
        productos = obtener_productos(g.usuario)

        repetir = True

        while repetir:
            try:
                limpiar_pantalla()
                print(f"--- Crear Oferta ---")
                print()
            
                print("Tipos de ofertas:")
                print()
                print("0- Volver atras")
                print("1- Combo")
                print("2- Descuento")
                print("3- Promo")
                opcion = int(input("Seleccionar opción: "))

                if opcion == 0:
                    repetir = False
                else:
                    if(opcion >= 1 and opcion <= 3):
                        productos_ofertas = []
                        mostrar = True

                        while mostrar:                                    
                            limpiar_pantalla()
                            contenido = {}
                            
                            tabla = [["ID", "Nombre", "Descripción", "Precio", "Tipo"]]
                            n = 1

                            for producto in productos.values():
                                contenido[n] = producto
                                tabla.append([n, producto["nombre"], producto["descripcion"], producto["precio"], producto["tipo"]])
                                n += 1

                            imprimir_tabla(tabla)
                
                            print()
                    
                            print("0- Volver atras")
                            id = int(input("Seleccionar ID del producto: "))
                            if(id != 0):
                                if id in contenido:
                                    producto_id = contenido[id]["id"]
                                    if opcion == 1:
                                        cantidad = int(input("Cantidad: "))
                                        precio = 0

                                        productos_ofertas.append({"id": producto_id, "cantidad": cantidad})
                                        precio += int(productos[producto_id]['precio']) * cantidad
                                        desea = input("¿Desea agregar otro producto? (S/N): ")
                                        if desea == "S":
                                            mostrar = True
                                        else:
                                            mostrar = False
                                            descuento = int(input("¿Cuál es el descuento por todos los productos seleccionados? "))

                                            precio = precio - (precio * (descuento/100))

                                            oferta = {
                                                "id": len(ofertas) + 1,
                                                "vendedor_id": g.usuario["id"],
                                                "productos": productos_ofertas,
                                                "descuento": descuento,
                                                "promo": []
                                            }

                                            ofertas.append(oferta)
                                            
                                            escribir_archivo("ofertas.json", ofertas)
                                    elif opcion == 2:
                                        precio = 0

                                        producto = [{"id": producto_id, "cantidad": 1 }]
                                        precio += int(productos[producto_id]['precio'])

                                        descuento = int(input("¿Cuál es el descuento? "))

                                        precio = precio - (precio * (descuento/100))

                                        mostrar = False

                                        oferta = {
                                            "id": len(ofertas) + 1,
                                            "vendedor_id": g.usuario["id"],
                                            "productos": producto,
                                            "descuento": descuento,
                                            "promo": []
                                        }

                                        ofertas.append(oferta)
                                        
                                        escribir_archivo("ofertas.json", ofertas)
                                    elif opcion == 3:
                                        precio = 0

                                        producto = [{"id": producto_id, "cantidad": 1 }]
                                        precio += int(productos[producto_id]['precio'])

                                        
                                        llevar = int(input("Cantidad para llevar: "))
                                        pagar = int(input("Cantidad para pagar: "))

                                        mostrar = False
                                        
                                        oferta = {
                                            "id": len(ofertas) + 1,
                                            "vendedor_id": g.usuario["id"],
                                            "productos": producto,
                                            "descuento": 0,
                                            "promo": [llevar, pagar]
                                        }

                                        ofertas.append(oferta)
                                        
                                        escribir_archivo("ofertas.json", ofertas)
                                else:
                                    print("No existe el producto")
                                    input()
                            else: 
                                mostrar = False

            except:
                print("Por favor, ingrese un número válido.")
                input()
       
def editar_oferta(id):
    limpiar_pantalla()
    print(f"--- Editar Oferta ---")
    print()

    encontrado = False
    i = 0
    ofertas = leer_archivo("ofertas.json")
    productos = obtener_productos(g.usuario)
    
    while not encontrado and len(ofertas) > i:
        oferta = ofertas[i]
        if(oferta["id"] == id):
            promo = oferta["promo"]
            if(len(promo)>0):
                llevar = int(input(f"Cantidad para llevar ({promo[0]}): "))
                if(llevar):
                    oferta["promo"][0] = llevar

                pagar = int(input(f"Cantidad para pagar ({promo[1]}): "))
                if(pagar):
                    oferta["promo"][1] = pagar
            else:
                for producto in oferta["productos"]:
                    print(f"Producto: {productos[producto['id']]['nombre']}")
                    cantidad = int(input(f"Cantidad ({producto['cantidad']}): "))

                    if(cantidad):
                        producto["cantidad"]= cantidad
                
                descuento = int(input(f"Descuento ({oferta['descuento']}): "))
        
                if(descuento):
                    oferta["descuento"] = descuento
                    

            print("Editado con exito")
                                

            encontrado = True
        i += 1

    escribir_archivo("ofertas.json", ofertas)
    return encontrado

def borrar_oferta(id):
    limpiar_pantalla()
    bool = False
    encontrado = False
    i = 0
    ofertas = leer_archivo("ofertas.json")

    while not encontrado and len(ofertas) > i:
        oferta = ofertas[i]
        
        if(oferta["id"] == id):
            confirmar = input("¿Estas seguro de borrarlo? (Si/No) ")
            if confirmar == "Si" or confirmar == "si":
                del ofertas[i]
                print("Borrado con exito")
                bool = True
            encontrado = True
        i += 1
    
    escribir_archivo("ofertas.json", ofertas)

    return bool


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
        print("6- Ver mis Ofertas")
        print("7- Crear Oferta")
        
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
            elif op == 6:
                ver_mis_ofertas()
            elif op == 7:
                crear_oferta()
            else:
                print("Opción incorrecta, intente de nuevo.")
                input()

        except:
            print("error")
