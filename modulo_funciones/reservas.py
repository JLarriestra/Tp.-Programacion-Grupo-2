from modulo_funciones.utiles import limpiar_pantalla, leer_archivo, escribir_archivo


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
    reservas = leer_archivo("reservas.json")

    print("--- Mis Reservas ---\n")

    i = 0
    while len(reservas) > i:
        id = reservas[i]["usuario_id"]
        
        if(usuario_id == id):
            num = reservas[i]["id"]
            producto = reservas[i]["producto"]
            nombre = producto["nombre"]
            precio = producto["precio"]
            print(f"Reserva #{num}")
            print(f"Nombre: {nombre}")
            print(f"Precio: ${precio}")
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