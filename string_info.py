def string_info():
    """Dada la palabra 'Programacion', imprime su longitud, primera y última letra,
    la palabra repetida 3 veces y decorada con '***'.
    """
    palabra = "Programacion"
    long =  len(palabra)
    pri_le = palabra[0]
    ult_le = palabra[-1]
    pala_re = palabra + palabra + palabra
    pala_de = "***" + palabra + "***"
    print("Palabra: " + palabra)
    print("Longitud: " + str(long))
    print("Primera letra: " + pri_le)
    print("Ultima letra: " + ult_le)
    print("Repetida: " + pala_re)
    print("Decorada: " + pala_de)

string_info()