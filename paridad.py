def indices_paridad(palabra):
    pos = 1
    while(pos <= len(palabra)):
        yield(pos - 1) #pos-1 = indice
        pos *= 2 #Recorremos la palabra avanzando en potencias de 2

def insertar_paridad(palabra):
    for ind_p in indices_paridad(palabra):
        palabra.insert(ind_p, 0) #Indicamos con un 0 la pos de los bits de paridad

def calcular_paridad(palabra):
    for i, ind_p in enumerate(indices_paridad(palabra)):
        cant_1 = 0
        for ind_bit, bit in enumerate(palabra):
            if(ind_bit in indices_paridad(palabra)): continue #Para el calculo no se considera las pos de los bits de paridad
            pos_bit = bin(ind_bit+1) #Pos en binario del j-esimo bit (ind_bit+1 = pos)
            if(pos_bit[-(i+1)] == '1'): #pos_bin[-(i+1)] = i-esimo LSB de la pos del bit
                cant_1 += bit

        palabra[ind_p] = cant_1 % 2 #Calculo bit paridad