from itertools import count


def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    pass
    nombre = str(input("Ingresar tu nombre completo: "))
    email = str(input("Ingresar tu email: "))
    nota1 = int(input("Ingresar primera nota: "))
    nota2 = int(input("Ingresar segunda nota: "))
    nota3 = int(input("Ingresar tercera nota: "))
    nombre_l = nombre.lower().title().lstrip().rstrip()
    email_l = email.lower()
    cant_carac = len(nombre_l)
    espacio = (nombre_l.find(" "))
    inici = nombre_l[0] + nombre_l [espacio + 1]
    nombre_minus = nombre_l.lower()
    usuario = nombre_minus[espacio + 1:] + "." + nombre_minus[:espacio]
    cont_arr = "@" in email_l
    find_ = email_l.find("@")
    dom_e = email_l[find_ + 1:]
    nom_titl= nombre_l.title()
    nom_ = nom_titl.replace(" ","_")
    cant_a = nombre_l.count("a")
    nom_upp = nombre_l.upper()
    nom_inver = nom_upp[::-1]
    suma = nota1 + nota2 + nota3
    prom = suma / 3
    prom_ent =  suma // 3

    print("========================")
    print("    FICHA DEL ALUMNO")
    print("========================")
    print("Nombre: " + nom_titl)
    print("Email: " + email_l)
    print("Caracteres en nombre: " + str(cant_carac))
    print("Iniciales: " + inici)
    print("Usuario: " + usuario)
    print("Email valido: " + str(cont_arr))
    print("Dominio: " + dom_e)
    print("Nombre para archivo: " + nom_)
    print("Cantidad de a: " + str(cant_a))
    print("Codigo secreto: " + nom_inver)
    print("Nota 1: " + str(nota1))
    print("Nota 2: " + str(nota2))
    print("Nota 3: " + str(nota3))
    print("Suma: " + str(suma))
    print("Promedio: " + str(prom))
    print("Promedio entero: " + str(prom_ent))
    print("========================")



