from modulo_funciones.utiles import limpiar_pantalla, leer_archivo, escribir_archivo


def obtener_marcas():
    usuarios = leer_archivo("usuarios.json")

    marcas = {}

    for usuario in usuarios:
        if usuario["rol"] == "VENDEDOR":
            marcas[usuario["id"]] = usuario
    
    return marcas


def agregar_reserva(usuario_id, producto):
    reservas = leer_archivo("reservas.json")
    reserva = {
        "id": len(reservas) + 1,
        "usuario_id": usuario_id,
        "vendedor_id": producto["vendedor_id"],
        "producto":{
            "id": producto["id"],
            "nombre": producto["nombre"],
            "precio": producto["precio"]
        },
    }
    reservas.append(reserva)	
    escribir_archivo("reservas.json", reservas)


def mostrar_reservas(usuario_id):
    limpiar_pantalla()
    reservas = leer_archivo("reservas.json")
    marcas = obtener_marcas()

    print("--- Mis Reservas ---\n")

    i = 0
    while len(reservas) > i:
        id = reservas[i]["usuario_id"]
        
        if(usuario_id == id):
            num = reservas[i]["id"]
            vendedor_id = reservas[i]["vendedor_id"]
            producto = reservas[i]["producto"]
            nombre = producto["nombre"]
            precio = producto["precio"]
            print(f"Reserva #{num}")
            print(f"Nombre: {nombre}")
            print(f"Precio: ${precio}")
            print(f"Marca: {marcas[vendedor_id]['nombre']}")
            print()
        i+=1
    input()


'''
    def obtener_estado(estado):
    estados = {
        1: "progreso",
        2: "retirar",
        3: "entregado"
    }

    return estados[estado]
'''
