from paridad import *

def codificar_hamming(palabra):
    palabra = palabra.copy()
    
    insertar_paridad(palabra)
    calcular_paridad(palabra)
    return palabra

def decodificar_hamming(palabra):
    palabra = palabra.copy()
    pos_err = encontrar_error(palabra)
    if(pos_err >= 1):
        corregir_error(palabra, pos_err)
    palabra = remover_paridad(palabra)
    print(palabra)
    return palabra

def encontrar_error(palabra):
    p_verificadora = palabra.copy()
    calcular_paridad(p_verificadora)
    pos_err = 0
    for pos, (bit1, bit2) in enumerate(zip(palabra, p_verificadora), 1):
        if(bit1 != bit2):
            pos_err += pos
    return pos_err

def corregir_error(palabra, pos_err):
    indice_error = pos_err - 1
    if(palabra[indice_error] == 0):
        palabra[indice_error] = 1
    else:
        palabra[indice_error] = 0

def remover_paridad(palabra):
    bits_dato = []
    for ind, bit in enumerate(palabra):
        if ind not in indices_paridad(palabra): #Guardamos solo los bits de dato
            bits_dato.append(bit)
    return bits_dato