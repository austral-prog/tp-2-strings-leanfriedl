def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    pass
    nombre = str(input("Ingrese nombre: "))
    apellido = str(input("Ingrese apellido: "))
    nom_ape = nombre + " " + apellido
    nom_min = nom_ape.lower()
    print(nom_min)
    nom_titl = nom_ape.title()
    print(nom_titl)
    nom_upp = nom_ape.upper()
    print(nom_upp)
    nom_tab = "\t" + nom_min
    print(nom_tab)

