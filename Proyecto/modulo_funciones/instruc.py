import os

def instrucciones():
    os.system("cls")
    print("Sistema de precios y descuentos en la Uade.")
    print("En este programa, se mostrara información detallada sobre los precios y descuentos de los productos y servicios disponibles en la UADE.")
    print("Como por ejemplo: Alimentos, bebidas, impresión, fotocopiado, costo de aparcamiento, entre otros.")
    print("El objetivo es proporcionar una herramienta útil que permita a los estudiantes y profesores ver todo lo que tiene para ofrecer nuestra universidad, y además ver todas las promociones disponibles y ahorrar algo de dinero.")

    inicio = int(input("Presione 0 para volver al inicio: "))

    if inicio == 0:
        import main
    

