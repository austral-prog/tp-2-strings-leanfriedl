def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    pass
    precio = int(input("Precio por unidad: "))
    descuento = float(input("Descuento: "))
    cantidad = float(input("Cantidad de unidades: "))

    print("Precio: " + str(precio))
    print("Descuento: " + str(descuento))
    precio_desc = precio - descuento
    print("Precio con descuento: " + str(precio_desc))
    precio_total = precio_desc * cantidad
    print("Total: " + str(precio_total))

casting()


