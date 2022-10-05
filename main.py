from hamming import *

palabra = [1,1,0,0,0,0,0,1]
p_a_decodificar = [1,1,1,0,1,0,0,1,0,0,0,1]
print(f"Palabra Entregada      {palabra}")

p_codificada= codificar_hamming(palabra)
(p_decodificada, p_error, p_corregida, pos_err) = decodificar_hamming(p_a_decodificar)

if(pos_err == 0):
    print("\nDecodificacion Correcta sin ningun error")
else:
     print(f"\nPalabra Con Error      {p_error}")
     print(f"Error en la posicion   N°{pos_err}")
     print(f"Palabra Ya Corregida   {p_corregida}")
     print(f"Palabra Decodificada   {p_decodificada}")