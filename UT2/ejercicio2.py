"""
Implementa un validador de contraseñas. Ésta se debe leer por teclado y debemos comprobar que cumple determinadas características:

Tiene entre 8 y 20 caracteres.
Tiene alguna letra mayúscula y alguna letra minúscula.
Tiene algún carácter raro entre $ % _ *
Tiene algún número
Implementa el código que mostrará si se cumplen los requisitos de contraseña válida o no.

"""


longitud = True
mayuscula = False
miniscula = False
numero = False
especial = False
longitud_password =0


password = input("Introduce la contraseña a validar")


# len(password)
for caracter in password:
    # comprobar todas los requisitos
    longitud_password += 1
    #longitud_password = longitud_password +1
    # no se puede hacer en python  longitud_password ++


    if caracter >='A' and caracter <='Z':
        mayuscula = True
    # if 'A' <= caracter <='Z'

    if caracter >='a' and caracter <='z':
        miniscula = True
    if caracter >='0' and caracter <='9':
        numero = True   
    if caracter == '$' or caracter == '%'or caracter == '_' or caracter == '*':
        especial = True

if longitud_password < 8 or longitud_password >20:
    longitud_password = False    


if not mayuscula:
    print ("Debe contener al menos una letra mayúscula")
if not miniscula:
    

"""

if longitud and mayuscula and miniscula and numero and especial:
    print("ES VAĹIDA")
else: 
        print("NO ES VAĹIDA")
"""