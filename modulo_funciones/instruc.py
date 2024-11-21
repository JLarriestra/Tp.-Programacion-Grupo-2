from modulo_funciones.utiles import limpiar_pantalla

def instrucciones():
    limpiar_pantalla()
    print("Sistema de precios y descuentos en la Uade.")
    print("En este programa, se mostrara información detallada sobre los precios y descuentos de los productos disponibles en la UADE.")
    print("Como por ejemplo: Alimentos, bebidas.")
    print("El objetivo es proporcionar una herramienta útil que permita a los estudiantes y profesores ver todas las promociones disponibles y ahorrar algo de dinero.")

    inicio = int(input("Presione 0 para volver al inicio: "))

    if inicio == 0:
        import main
    

