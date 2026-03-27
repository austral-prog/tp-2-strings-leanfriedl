def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    pass
    base = int(input("Base: "))
    altura = int(input("Altura: "))
    area = base * altura
    perimetro = (base * 2) + (altura * 2)
    print("Base: " + str(base))
    print("Altura: " + str(altura))
    print("Area: " + str(area))
    print("Perimetro: " + str(perimetro))

rectangle()