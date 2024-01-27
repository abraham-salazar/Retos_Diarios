"""
/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
"""

def anagrama(palabra1, palabra2):
    if len(palabra1) == len(palabra2) and palabra1 != palabra2:
        a = "".join(sorted(palabra1))
        b = "".join(sorted(palabra2))    
        if a == b:
            resul = True
        else:
            resul = False
    else:
        resul = False
    print(resul)
                
palabra1 = input("Ingrese la palabra 1: ")
palabra2 = input("Ingrese la palabra 2: ")
anagrama(palabra1, palabra2)
