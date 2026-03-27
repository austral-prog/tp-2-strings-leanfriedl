from gettext import find
from operator import and_


def string_methods():
    """Demuestra el uso de métodos de string: strip, lstrip, rstrip, upper, lower,
    title, find, replace, count, operador in, slicing con paso, reverso,
    f-strings y strings multilínea.
    """
    nombre = "   Grace Hopper   "
    frase = "Python es un gran lenguaje de programacion"
    multilinea = """Linea 1 
    Linea 2
    Linea 3"""
    st1 = nombre.strip()
    ls1 = nombre.lstrip()
    rs1 = nombre.rstrip()
    upp2 = frase.upper()
    low2 = frase.lower()
    titl2 = frase.title()
    f3 = frase.find("gran")
    f4 = frase.replace("programacion", "desarrollo")
    f5 = frase.count("a")
    fp6 = "Python" in frase
    fj6 = "Java" in frase
    f7 = frase[0:6]
    f8 = frase[0:6:2]
    f9 = frase[0:6][::-1]
    n10 = f"{nombre.strip()} sabe Python"
    print("Strip: "+ st1)
    print("Lstrip: "+ ls1)
    print("Rstrip: "+ rs1)
    print("Upper: "+ upp2)
    print("Lower: " + low2)
    print("Title: "+ titl2)
    print("Find: "+ str(f3))
    print("Replace: "+ f4)
    print("Count: "+ str(f5))
    print("Contiene Python: "+ str(fp6))
    print("Contiene Java: "+ str(fj6))
    print("Slice: "+ f7)
    print("Paso: "+ f8)
    print("Reverso: "+ f9)
    print("Formato: "+ n10)
    print("Linea 1")
    print("Linea 2")
    print("Linea 3")

