from codificar_hamming import *

def encontrar_error(palabra):
    p_verificadora = palabra.copy()
    calcular_paridad(p_verificadora)
    indices_error = []
    for ind, (bit1, bit2) in enumerate(zip(palabra, p_verificadora)):
        if(bit1 != bit2):
            indices_error.append(ind)
    return indices_error

def corregir_error(palabra, indices_error):
    for ind in indices_error:
        if(palabra[ind] == 0):
            palabra[ind] = 1
        else:
            palabra[ind] = 0

def remover_paridad(palabra):
    bits_dato = []
    for ind, bit in enumerate(palabra):
        if ind not in indices_paridad(palabra): #Guardamos solo los bits de dato
            bits_dato.append(bit)
    return bits_dato

def decodificar_hamming(palabra):
    palabra = palabra.copy()
    indices_error = encontrar_error(palabra)
    if(len(indices_error) != 0):
        corregir_error(palabra, indices_error)
    palabra = remover_paridad(palabra)
    return palabra