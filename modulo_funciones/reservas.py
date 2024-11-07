reservas = []

def agregar_reserva(producto):
    reservas.append(producto)

def mostrar_reservas():
    if not reservas:
        print("No hay reservas actualmente.")
    else:
        print("Lista de reservas:")
        for i, reserva in enumerate(reservas, 1):
            print(f"{i}. {reserva}")
