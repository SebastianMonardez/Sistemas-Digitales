with open("ebcdic.txt", 'r') as datos:
    matriz = []
    for linea in datos:
        matriz.append(linea.strip().split(","))

def encontrar_bits(caracter):
    for i in matriz:
        if(i[0] == caracter):
            return [int(i) for i in i[1]]

def encontrar_caracter(bits):
    for i in matriz:
        if(i[1] == bits):
            return i[0]