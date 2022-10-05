with open("ebcdic.txt") as citas:
    matriz = []
    for linea in citas:
        campos = linea.strip()[1:-1].replace('','').split(",")
        matriz.append(campos)

print(matriz)