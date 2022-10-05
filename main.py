from codificar_hamming import *
from decodificar_hamming import *

palabra = [1,1,0,0,0,0,0,1]
res_esperado = [0,1,1,0,1,0,0,1,0,0,1,1]

print(f"palabra entregada {palabra}")


p_codificada= codificar_hamming(palabra)
if(p_codificada == res_esperado):
    print("Codificacion Correcta")
else:
    print("Codificacion Incorrecto")


(p_decodificada, p_error, p_corregida, pos_err) = decodificar_hamming(res_esperado)

if(pos_err !=0):
    print("Decodificacion Correcta sin ningun error")
else:
     print(f"Palabra mala {p_error}")
     print(f"Hay un error en la posicion {pos_err}")
     print(f"Palabra corregida {p_corregida}")
     print(f"Palabra decodificada {p_decodificada}")