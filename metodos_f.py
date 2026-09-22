
def multiplicars(a,b):
    c = 0
    for i in range(b):
        c += a
    return c

def dividirs(a,b):

    c = 0
    if b ==0:
        return "No se puede dividir entre 0"
    while a >= b:
        a = a-b
        c += 1
    return c

def modulo(a,b):

    if b == 0:
        return "No se puede dividir entre 0"
    div = dividirs(a,b)
    resto = a - multiplicars(div,b)
    return resto

def raiz_entera(a):
    c=1

    while dividirs(a,c) >= 1:
        
        c += 1
