import pickle

reservas = []

def agregar_reserva(producto):
    reservas.append(producto)
    guardar_reservas()

def guardar_reservas():
    with open('reservas.pkl', 'wb') as file:
        pickle.dump(reservas, file)
