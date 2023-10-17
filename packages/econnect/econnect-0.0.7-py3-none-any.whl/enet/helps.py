def len_recarga(recarga):
    c = 0
    recarga = str(recarga)
    for a in recarga:
        c += 1
    if c < 12:
        return 'menor_12'
    elif c > 16:
        return 'mayor_16'
    else:
        return True

def insertar_numero(numero, orden):
    numero = int(numero)
    orden = str(orden)
    if numero == 1:
        orden = 'recargar cuenta'
    try:
        if numero == 1:
            return True
        else:
            return False
    except:
        return False

