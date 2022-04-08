import pandas as pd

def diccionario_csv(filename):
    dicc= pd.read_csv(filename).to_dict()
    return dicc


def sin_pandas(filename):
    lista=[]
    archivo = (filename, "r")
    for linea in archivo:
        lista.append(dict(linea))

    archivo.close()
    del lista[0]
    return lista
