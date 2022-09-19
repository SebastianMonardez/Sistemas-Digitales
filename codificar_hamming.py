def indices_paridad(palabra):
    pos = 1

    while(pos <= len(palabra)):
        yield(pos - 1) #pos-1 para trabajar con vectores
        pos *= 2 #Recorremos la palabra avanzando en potencias de 2

def insertar_paridad(palabra):
    for indice in indices_paridad(palabra):
        palabra.insert(indice, 0) #Indicamos con un 0 la pos de los bits de paridad

def calcular_paridad(palabra):
    for bit_index in indices_paridad(palabra):
        inicio = bit_index
        bloques = []

        while(inicio < len(palabra)):
            bloque = palabra[inicio : inicio + bit_index + 1]
            bloques.extend(bloque) #Extend a dif de insert permite agregar varios elementos al final
            inicio += 2 * (bit_index + 1)

        #Si resto=0 paridad impar -> añadimos 1
        #Si resto=1 paridad par -> añadimos 0
        #Se añade en la pos 0 del bloque porque cada bloque
        #empieza con el bit de paridad que se va a calcular
        bloques[0] = sum(bloques) % 2

        palabra[bit_index] = bloques[0] #Reemplazamos los bits de paridad calculados en sus respectivas posiciones
        #print(bloques)

palabra = [1, 1, 0, 0, 0, 0, 0, 1] #Caracter 'A' en EBCDIC

print(f"Palabra Original: {palabra}")
insertar_paridad(palabra)
calcular_paridad(palabra)
print(f"Palabra Codificada en Hamming: {palabra}")