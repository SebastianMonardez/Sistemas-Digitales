def indices_paridad(palabra):
    pos = 1

    while(pos <= len(palabra)):
        yield(pos - 1) #pos-1 = indice
        pos *= 2 #Recorremos la palabra avanzando en potencias de 2

def insertar_paridad(palabra):
    for ind_paridad in indices_paridad(palabra):
        palabra.insert(ind_paridad, 0) #Indicamos con un 0 la pos de los bits de paridad

def calcular_paridad(palabra):     
    for ind_paridad in indices_paridad(palabra):
        pos_paridad = ind_paridad + 1
        bloques = []
        for ind_act in range(ind_paridad, len(palabra), 2 * pos_paridad):
            bloque = palabra[ind_act : ind_act + pos_paridad]
            bloques.extend(bloque)
        
        #Si resto != 0 paridad impar -> añadimos un 1
        #En caso contrario no añadimos nada (ya tiene un 0 marcando la posicion de paridad)
        #Se añade en la pos 0 del bloque porque cada bloque
        #empieza con el bit de paridad que se va a calcular
        if(sum(bloques) % 2 != 0):
            palabra[ind_paridad] = 1

palabra = [1, 1, 0, 0, 0, 0, 0, 1]

insertar_paridad(palabra)
calcular_paridad(palabra)
print(f"Palabra Codificada en Hamming: {palabra}")