from modulo_funciones.utiles import limpiar_pantalla
def equipo ():
    repetir= True
    limpiar_pantalla()
    print("los integrantes del equipo son:")
    print("Juan Pedro Larriestra") 
    print("Ariel Blas Condorpocco")    
    print("Bautista Zucchi")
    print("Facundo Soto")
    print("Franco Di Meo")
    
    inicio = int(input("Presione 0 para volver al inicio: "))
    
    if inicio == 0:
        import main

