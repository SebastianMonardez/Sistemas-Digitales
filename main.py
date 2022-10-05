from hamming import *
from ebcdic import *

menu = """
"Bienvenidos al progama Codigo Hammming, llene los campos que usted
prefiera a continuacion seleccionando un numero del 1 al 3:
[1] Codificar
[2] Decodificar
[3] Salir Del Programa  
""" 

opcion=0
while opcion != 3:
    print(menu)
    opcion = input('Digita una opcion entre 1 y 3: ')


    if opcion == '1':
        palabra = input("Ingrese un caracter: ").upper()
        palabra = encontrar_bits(palabra)
        p_codificada= codificar_hamming(palabra)
    elif opcion == '2':
        palabra = input("Ingrese una palabra (12 bits): ").upper()
        (p_decodificada, p_error, p_corregida, pos_err) = decodificar_hamming(palabra)
        if(pos_err == 0):
            print("\nDecodificacion Correcta sin ningun error")
        else:
            print(f"\nPalabra Con Error      {p_error}")
            print(f"Error en la posicion   N°{pos_err}")
            print(f"Palabra Ya Corregida   {p_corregida}")
            print(f"Palabra Decodificada   {p_decodificada}")
        palabra = encontrar_bits(p_decodificada)
        print(f"Tu caracter es: {palabra}")
    elif opcion == '3':
        break
    else:
        print('Debes digitar un numero entre 1 y 3')
        print('=-='*20)