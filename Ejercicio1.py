import pandas as pd

def diccionario_csv(filename):
    dicc= pd.read_csv(filename).to_dict()
    return dicc