

def aprobados_suspensos(lista):
    aprobados = []
    suspensos = []
    for dicc in lista:
        list(dicc)
        if dicc[2]>=75 and ((dicc[3],dicc[4],dicc[7],dicc[8])>=(4,4,4,4)) and dicc[-1]>=5:
            
