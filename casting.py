def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""

    precio = int(input("Precio: "))
    descuento = float(input("Descuento: "))
    cantidad = int(input())
    total = (precio - descuento) * cantidad

    print(f"Precio con descuento: {precio-descuento}")
    print(f"Total: {total}")
