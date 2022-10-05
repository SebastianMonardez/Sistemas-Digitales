from hamming import *

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
        
        p_codificada= codificar_hamming(palabra)
        pass
    elif opcion == '2':


        (p_decodificada, p_error, p_corregida, pos_err) = decodificar_hamming(p_a_decodificar)
        if(pos_err == 0):
            print("\nDecodificacion Correcta sin ningun error")
        else:
            print(f"\nPalabra Con Error      {p_error}")
            print(f"Error en la posicion   N°{pos_err}")
            print(f"Palabra Ya Corregida   {p_corregida}")
            print(f"Palabra Decodificada   {p_decodificada}")
            pass

    elif opcion == '3':
        break
    else:
        print('Debes digitar un numero entre 1 y 3')
        print('=-='*20)

    
    