def indices_paridad(palabra):
    pos = 1

    while(pos <= len(palabra)):
        yield(pos - 1) #pos-1 = indice
        pos *= 2 #Recorremos la palabra avanzando en potencias de 2

def insertar_paridad(palabra):
    for ind_paridad in indices_paridad(palabra):
        palabra.insert(ind_paridad, 0) #Indicamos la pos de los bits de paridad con un 0

def calcular_paridad(palabra):
    for i, ind_paridad in enumerate(indices_paridad(palabra)):
        suma = 0
        for j, bit in enumerate(palabra):
            pos_bin = bin(j + 1) #Pos del bit en binario (j+1 = pos)
            if(len(pos_bin) >= i+1): #i+1 = i-esimo bit de paridad a calcular
                if(pos_bin[-(i+1)] == '1'): #pos_bin[-(i+1)] i-esimo LSB de la posicion del bit 
                    suma += bit

        if(suma % 2 != 0):
            palabra[ind_paridad] = 1

palabra = [1, 1, 0, 0, 0, 0, 0, 1]

insertar_paridad(palabra)
calcular_paridad(palabra)
print(f"Palabra Codificada en Hamming: {palabra}")