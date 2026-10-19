#materiales de https://plataforma.josedomingo.org/pledin/cursos/programacion_python3/

#Ejercicio 1
# Escribir un programa que pregunte al usuario su nombre, y luego lo salude.

nombre=input("Dime tu nombre:")
print("Hola",nombre)
#Ejercicio 2
# Calcular el perímetro y área de un rectángulo dada su base y su altura.

base=float(input("Introduce la base:"))
altura=float(input("Introduce la altura:"))
perimetro = 2 * base * altura
area = base * altura
print("El perimetro es", perimetro, "y el area es", area)
#Ejercicio 3
# Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

import math
cateto1 = float(input("Introduce el cateto 1:"))
cateto2 = float(input("Introduce el cateto 2:"))
hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)
print("La hipotenusa es",hipotenusa)
#Ejercicio 4
# Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.

num1 = float(input("Introduce el número 1:"))
num2 = float(input("Introduce el número 2:"))
print("La suma es", num1+num2)
print("La resta es", num1-num2)
print("La multiplicación es", num1*num2)
print("La división es", num1/num2)

#Ejercicio 5
# Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
fahrenheit = float(input("Introduce la temperatura en ºF:"))
celcius = (fahrenheit - 32) * 5 / 9
print("La temperatura es", celcius, "ºC")

#Ejercicio 6
# Calcular la media de tres números pedidos por teclado

num1 = float(input("Introduce el número 1:"))
num2 = float(input("Introduce el número 2:"))
num3 = float(input("Introduce el número 3:"))
media = (num1 + num2 +num3) / 3
print("La media es:", media)

# Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a 
# cuantas horas y minutos corresponde.

minutos = int(input("Introduce la cantidad de minutos:"))
res_horas = minutos // 60
res_min = minutos % 60
print(res_horas,"horas y",res_min,"minutos.")
