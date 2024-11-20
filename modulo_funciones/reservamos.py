import pickle

def mostrar_reservas():
    try:
        with open('reservas.pkl', 'rb') as file:
            reservas = pickle.load(file)
            if not reservas:
                print("No hay reservas actualmente.")
            else:
                print("Lista de reservas:")
                for i, reserva in enumerate(reservas, 1):
                    print(f"{i}. {reserva}")
            input("0. Regresar al menu principal")  
    except FileNotFoundError:
        print("No se encontraron reservas")
        input("0. Regresar al menu principal ")  