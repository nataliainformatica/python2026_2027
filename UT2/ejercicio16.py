""" 
Comprueba si una cadena de caracteres comienza por una subcadena
"""


cadena = input("Introduce la cadena ")
subcadena = input ("Introduce la subcadena ")
coincide = True
posicion = 0

if len(subcadena)  > len(cadena):
    coincide = False
else:
    while posicion <len(subcadena) :
        if cadena[posicion] != subcadena[posicion]:
            coincide = False
            break
        else:
            posicion +=1

if coincide:
    print ("La cadena comienza por la subcadena")
else:
    print("La cadena NO comienza por la subcadena")
        

