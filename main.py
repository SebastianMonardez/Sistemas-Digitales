from codificar_hamming import *
from decodificar_hamming import *

palabra = [1,1,0,0,0,0,0,1]
res_esperado = [0,1,1,0,1,0,0,1,0,0,0,1]

p_codificada = codificar_hamming(palabra)

if(p_codificada == res_esperado):
    print("Codificacion Correcta")
else:
    print("Codificacion Incorrecto")

p_codificada[11] = 0

p_decodificada = decodificar_hamming(p_codificada)

if(p_decodificada == palabra):
    print("Decodificacion Correcta")
else:
    print("Decodificacion Incorrecta")