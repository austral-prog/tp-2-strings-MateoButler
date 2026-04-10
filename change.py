def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass
    gasto = float(input("Ingresar Gasto:\n"))
    dinero_recibido = int(input("Dinero Recibido:\n"))
    vuelto_total = dinero_recibido-gasto
    pesos = int(vuelto_total)
    centavos = round((vuelto_total-pesos)*100)

    print("\nVuelto\n")
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)