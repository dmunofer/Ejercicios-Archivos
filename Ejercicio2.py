def añadir_nota(lista):
    for dicc in lista:
        list(dicc)
        nota = dicc[3]*0.3 + dicc[4]*0.3+ dicc[-2]*0.6
        nota.append(dicc)
        dict(dicc)
    return lista