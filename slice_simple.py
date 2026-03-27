def slice_simple():
    """Dado el texto 'Awesome', imprime distintos substrings
    usando slicing y lower().
    """
    texto = "Awesome"
    text_low = texto.lower()
    text_1 = text_low[0:3]
    text_2 = texto[2:5]
    print(text_1)
    print(text_2)
    print(text_low)

