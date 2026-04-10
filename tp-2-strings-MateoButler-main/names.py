def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    pass
    nombre = input()
    apellido = input()
    nombre_apellido = (nombre + " " + apellido)
    print(nombre_apellido.lower())
    print(nombre_apellido.title())
    print(nombre_apellido.upper())
    print("\t"+nombre_apellido.lower())
