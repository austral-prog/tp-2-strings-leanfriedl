def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """
    pass
    nombre = str(input("Ingrese un nombre: "))
    nom_low = nombre.lower()
    busca_a = "a" in nom_low
    busca_e = "e" in nom_low
    busca_i = "i" in nom_low
    busca_o = "o" in nom_low
    busca_u = "u" in nom_low
    print("Contiene a: " + str(busca_a))
    print("Contiene e: " + str(busca_e))
    print("Contiene i: " + str(busca_i))
    print("Contiene o: " + str(busca_o))
    print("Contiene u: " + str(busca_u))

check_vowels()