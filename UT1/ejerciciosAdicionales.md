# UT1. Ejercicios adicionales

## Introducción

Este documento recoge cinco ejercicios adicionales, de complejidad similar a la actividad práctica de la UT1, pensados para reforzar de forma individual o complementar dicha actividad. 

Cada ejercicio es un programa secuencial completo que combina todos los elementos trabajados en la unidad, sin usar ningún elemento del lenguaje que se estudie en unidades posteriores (estructuras selectivas o iterativas, funciones, indexación, clases...). Para cada uno se incluyen el enunciado, la solución comentada y un ejemplo de ejecución ya comprobado.


## Ejercicio 1: Propina y reparto de la cuenta en un restaurante

### Enunciado

Escribe un programa que pida por teclado el importe total de una cuenta de restaurante y el número de comensales, y que calcule y muestre: la propina (aplicando un porcentaje fijo, definido como constante), el total a pagar con propina incluida, y el importe que le corresponde pagar a cada comensal. El programa debe indicar además si el grupo es "grande" (a partir de un número de comensales también definido como constante).

### Solución

```python
"""
Calculadora de propina y reparto de la cuenta en un restaurante.

Programa secuencial que calcula la propina y el total a pagar entre un
grupo de comensales, a partir del importe de la cuenta y del número de
personas introducidos por teclado.
"""

# --- 1. Cabecera / importaciones ---
# Este programa no necesita importar ningún módulo adicional.

# --- 2. Declaraciones globales ---
NOMBRE_RESTAURANTE = "Casa Pepe"   # constante: literal de cadena
PORCENTAJE_PROPINA = 0.10          # constante: 10 % de propina habitual
COMENSALES_GRUPO_GRANDE = 6        # constante: umbral de "grupo grande"

# --- 3. Definición de funciones y clases ---
# Cuando se vean las funciones se extraería a una función, por ejemplo:
#
#     def calcular_reparto(importe, comensales):
#         ...

print("---", NOMBRE_RESTAURANTE, "---")
print("Calculadora de propina y reparto de la cuenta")
print()

importe_texto = input("Importe total de la cuenta, en euros: ")
comensales_texto = input("¿Cuántos comensales sois? ")

importe_cuenta = float(importe_texto)   # conversión explícita de str a float
comensales = int(comensales_texto)      # conversión explícita de str a int

es_grupo_grande = comensales >= COMENSALES_GRUPO_GRANDE   # operador relacional -> bool

propina = importe_cuenta * PORCENTAJE_PROPINA
total_con_propina = importe_cuenta + propina
importe_por_persona = total_con_propina / comensales

print()
print("Resumen de la cuenta")
print("Restaurante:", NOMBRE_RESTAURANTE)
print("Importe de la cuenta:", importe_cuenta, "€  (tipo:", type(importe_cuenta), ")")
print("Comensales:", comensales, "  (tipo:", type(comensales), ")")
print("Propina (10 %):", propina, "€")
print("Total con propina:", total_con_propina, "€")
print("Importe por persona:", importe_por_persona, "€")
print("¿Es un grupo grande (6 o más comensales)?", es_grupo_grande)

# --- 5. Punto de entrada y salida ---
# La ejecución comienza en la primera instrucción del cuerpo principal
# (el print de bienvenida) y termina al llegar a la última línea del
# archivo, tras mostrar el resumen de la cuenta.
```

### Ejemplo de ejecución

```
--- Casa Pepe ---
Calculadora de propina y reparto de la cuenta

Importe total de la cuenta, en euros: 50
¿Cuántos comensales sois? 5

Resumen de la cuenta
Restaurante: Casa Pepe
Importe de la cuenta: 50.0 €  (tipo: <class 'float'> )
Comensales: 5   (tipo: <class 'int'> )
Propina (10 %): 5.0 €
Total con propina: 55.0 €
Importe por persona: 11.0 €
¿Es un grupo grande (6 o más comensales)? False
```

## Ejercicio 2: Conversor de kilómetros a millas

### Enunciado

Escribe un programa que pida por teclado el nombre de la persona que conduce y la distancia de un trayecto en kilómetros, y que calcule y muestre: la distancia equivalente en millas (usando el factor de conversión como constante) y el tiempo estimado del trayecto suponiendo una velocidad media fija. El programa debe indicar además si el trayecto es "largo" (a partir de una distancia mínima en kilómetros, también definida como constante).

### Solución

```python
"""
Conversor de kilómetros a millas para un viaje en coche.

Programa secuencial que, a partir del nombre de quien conduce y de la
distancia de un trayecto en kilómetros introducidos por teclado, calcula
la distancia equivalente en millas.
"""

# --- 1. Cabecera / importaciones ---
# Este programa no necesita importar ningún módulo adicional.

# --- 2. Declaraciones globales ---
KM_A_MILLAS = 0.621371        # constante: factor de conversión km -> millas
DISTANCIA_LARGA_KM = 100      # constante: umbral, en km, de "trayecto largo"

# --- 3. Definición de funciones y clases ---
# Cuando se vean las funciones, la conversión se extraería a una función, por ejemplo:
#
#     def km_a_millas(distancia_km):
#         ...

print("Conversor de kilómetros a millas")
print()

nombre_conductor = input("¿Cuál es tu nombre? ")
distancia_texto = input("¿Cuántos kilómetros tiene el trayecto? ")

distancia_km = float(distancia_texto)   # conversión explícita de str a float

es_trayecto_largo = distancia_km >= DISTANCIA_LARGA_KM   # operador relacional -> bool

distancia_millas = distancia_km * KM_A_MILLAS
velocidad_media_kmh = 90                                  # literal entero
tiempo_estimado_horas = distancia_km / velocidad_media_kmh

print()
print("Hola,", nombre_conductor)
print("Distancia:", distancia_km, "km  (tipo:", type(distancia_km), ")")
print("Distancia equivalente:", distancia_millas, "millas")
print("Tiempo estimado a", velocidad_media_kmh, "km/h:", tiempo_estimado_horas, "horas")
print("¿Es un trayecto largo (100 km o más)?", es_trayecto_largo)

# --- 5. Punto de entrada y salida ---
# La ejecución comienza en la primera instrucción del cuerpo principal
# (la petición del nombre) y termina al llegar a la última línea del
# archivo, tras mostrar el resultado de la conversión.
```

### Ejemplo de ejecución

```
Conversor de kilómetros a millas

¿Cuál es tu nombre? Inés
¿Cuántos kilómetros tiene el trayecto? 160

Hola, Inés
Distancia: 160.0 km  (tipo: <class 'float'> )
Distancia equivalente: 99.41936 millas
Tiempo estimado a 90 km/h: 1.7777777777777777 horas
¿Es un trayecto largo (100 km o más)? True
```

## Ejercicio 3: Calculadora del Índice de Masa Corporal (IMC)

### Enunciado

Escribe un programa que pida por teclado el peso (en kg) y la altura (en metros) de una persona, y que calcule y muestre su Índice de Masa Corporal (IMC), aplicando la fórmula `peso / altura²`. El programa debe indicar además si el resultado está dentro del rango considerado saludable, definiendo el límite inferior y el límite superior de ese rango como constantes.

### Solución

```python
"""
Calculadora del Índice de Masa Corporal (IMC).

Programa secuencial que calcula el IMC de una persona a partir de su peso
y su altura introducidos por teclado, e indica si el resultado está dentro
del rango considerado saludable.
"""

# --- 1. Cabecera / importaciones ---
# Este programa no necesita importar ningún módulo adicional.

# --- 2. Declaraciones globales ---
IMC_MINIMO_SALUDABLE = 18.5   # constante: límite inferior del rango saludable
IMC_MAXIMO_SALUDABLE = 24.9   # constante: límite superior del rango saludable

# --- 3. Definición de funciones y clases ---
# Cuando se vean las funciones, se extraería a una función, por ejemplo:
#
#     def calcular_imc(peso, altura):
#         ...

print("Calculadora del Índice de Masa Corporal (IMC)")
print()

peso_texto = input("Introduce tu peso, en kg: ")
altura_texto = input("Introduce tu altura, en metros (por ejemplo, 1.70): ")

peso = float(peso_texto)       # conversión explícita de str a float
altura = float(altura_texto)   # conversión explícita de str a float

imc = peso / altura ** 2       # operadores aritméticos: división y potencia

es_saludable = imc >= IMC_MINIMO_SALUDABLE and imc <= IMC_MAXIMO_SALUDABLE   # relacional + lógico

print()
print("Peso:", peso, "kg  (tipo:", type(peso), ")")
print("Altura:", altura, "m  (tipo:", type(altura), ")")
print("Tu IMC es:", imc)
print("Rango saludable de referencia:", IMC_MINIMO_SALUDABLE, "-", IMC_MAXIMO_SALUDABLE)
print("¿Tu IMC está dentro del rango saludable?", es_saludable)

# --- 5. Punto de entrada y salida ---
# La ejecución comienza en la primera instrucción del cuerpo principal
# (la petición del peso) y termina al llegar a la última línea del
# archivo, tras mostrar el resultado del cálculo.
```

### Ejemplo de ejecución

```
Calculadora del Índice de Masa Corporal (IMC)

Introduce tu peso, en kg: 68
Introduce tu altura, en metros (por ejemplo, 1.70): 1.70

Peso: 68.0 kg  (tipo: <class 'float'> )
Altura: 1.7 m  (tipo: <class 'float'> )
Tu IMC es: 23.529411764705884
Rango saludable de referencia: 18.5 - 24.9
¿Tu IMC está dentro del rango saludable? True
```

## Ejercicio 4: Coste de combustible de un trayecto

### Enunciado

Escribe un programa que pida por teclado la distancia de un trayecto en km, el consumo medio del vehículo (en litros cada 100 km) y el precio del combustible (en euros por litro), y que calcule y muestre: los litros de combustible necesarios y el coste total del trayecto. El programa debe indicar además si el precio introducido está por debajo de un precio medio de referencia, definido como constante.

### Solución

```python
"""
Calculadora del coste de combustible de un trayecto en coche.

Programa secuencial que calcula cuánto combustible se necesita y cuánto
cuesta un trayecto, a partir de la distancia, el consumo medio del
vehículo y el precio del combustible introducidos por teclado.
"""

# --- 1. Cabecera / importaciones ---
# Este programa no necesita importar ningún módulo adicional.

# --- 2. Declaraciones globales ---
PRECIO_MEDIO_REFERENCIA = 1.65   # constante: precio medio de referencia (€/litro)

# --- 3. Definición de funciones y clases ---
# Cuando se vean las funciones, el cálculo se extraería a una función, por ejemplo:
#
#     def calcular_coste_trayecto(distancia, consumo, precio_litro):
#         ...

print("Calculadora del coste de combustible de un trayecto")
print()

distancia_texto = input("Distancia del trayecto, en km: ")
consumo_texto = input("Consumo medio del vehículo, en litros cada 100 km: ")
precio_texto = input("Precio del combustible, en euros por litro: ")

distancia_km = float(distancia_texto)   # conversión explícita de str a float
consumo_medio = float(consumo_texto)    # conversión explícita de str a float
precio_litro = float(precio_texto)      # conversión explícita de str a float

conviene_repostar_fuera = precio_litro < PRECIO_MEDIO_REFERENCIA   # operador relacional -> bool

litros_necesarios = distancia_km * consumo_medio / 100
coste_total = litros_necesarios * precio_litro

print()
print("Distancia:", distancia_km, "km  (tipo:", type(distancia_km), ")")
print("Consumo medio:", consumo_medio, "l/100km")
print("Precio del combustible:", precio_litro, "€/l")
print("Litros necesarios:", litros_necesarios, "l")
print("Coste total del trayecto:", coste_total, "€")
print("Precio medio de referencia:", PRECIO_MEDIO_REFERENCIA, "€/l")
print("¿Conviene repostar aquí (precio por debajo de la referencia)?", conviene_repostar_fuera)

# --- 5. Punto de entrada y salida ---
# La ejecución comienza en la primera instrucción del cuerpo principal
# (la petición de la distancia) y termina al llegar a la última línea
# del archivo, tras mostrar el coste del trayecto.
```

### Ejemplo de ejecución

```
Calculadora del coste de combustible de un trayecto

Distancia del trayecto, en km: 300
Consumo medio del vehículo, en litros cada 100 km: 6
Precio del combustible, en euros por litro: 1.50

Distancia: 300.0 km  (tipo: <class 'float'> )
Consumo medio: 6.0 l/100km
Precio del combustible: 1.5 €/l
Litros necesarios: 18.0 l
Coste total del trayecto: 27.0 €
Precio medio de referencia: 1.65 €/l
¿Conviene repostar aquí (precio por debajo de la referencia)? True
```

## Ejercicio 5: Meses necesarios para un objetivo de ahorro

### Enunciado

Escribe un programa que pida por teclado un objetivo de ahorro (en euros) y la cantidad que se puede ahorrar cada mes, y que calcule y muestre: el número exacto de meses necesarios (con decimales), el número de meses completos necesarios y el dinero que faltaría ahorrar en el último mes. El programa debe indicar además si el objetivo se cumple en un año o menos, definiendo el número de meses de un año como constante.

### Solución

```python
"""
Calculadora de meses necesarios para alcanzar un objetivo de ahorro.

Programa secuencial que calcula cuántos meses completos (y cuánto dinero
sobrante en el último mes) se necesitan para alcanzar un objetivo de
ahorro, a partir de la cantidad objetivo y del ahorro mensual introducidos
por teclado.
"""

# --- 1. Cabecera / importaciones ---
# Este programa no necesita importar ningún módulo adicional.

# --- 2. Declaraciones globales ---
MESES_EN_UN_ANIO = 12       # constante: número de meses de un año

# --- 3. Definición de funciones y clases ---
# Cuando se vean las funciones, el cálculo se extraería a una función, por ejemplo:
#
#     def calcular_meses_ahorro(objetivo, ahorro_mensual):
#         ...

print("Calculadora de meses necesarios para un objetivo de ahorro")
print()

objetivo_texto = input("¿Cuál es tu objetivo de ahorro, en euros? ")
ahorro_texto = input("¿Cuánto puedes ahorrar cada mes, en euros? ")

objetivo_ahorro = float(objetivo_texto)   # conversión explícita de str a float
ahorro_mensual = float(ahorro_texto)      # conversión explícita de str a float

meses_exactos = objetivo_ahorro / ahorro_mensual         # división -> float
meses_completos = objetivo_ahorro // ahorro_mensual       # división entera
dinero_ultimo_mes = objetivo_ahorro % ahorro_mensual       # módulo (resto)

se_cumple_en_un_anio = meses_exactos <= MESES_EN_UN_ANIO   # operador relacional -> bool

print()
print("Objetivo de ahorro:", objetivo_ahorro, "€  (tipo:", type(objetivo_ahorro), ")")
print("Ahorro mensual:", ahorro_mensual, "€  (tipo:", type(ahorro_mensual), ")")
print("Meses necesarios (exacto):", meses_exactos)
print("Meses completos necesarios:", meses_completos)
print("Dinero que faltaría ahorrar en el último mes:", dinero_ultimo_mes, "€")
print("¿Se cumple el objetivo en un año o menos?", se_cumple_en_un_anio)

# --- 5. Punto de entrada y salida ---
# La ejecución comienza en la primera instrucción del cuerpo principal
# (la petición del objetivo de ahorro) y termina al llegar a la última
# línea del archivo, tras mostrar el resultado del cálculo.
```

### Ejemplo de ejecución

```
Calculadora de meses necesarios para un objetivo de ahorro

¿Cuál es tu objetivo de ahorro, en euros? 1000
¿Cuánto puedes ahorrar cada mes, en euros? 120

Objetivo de ahorro: 1000.0 €  (tipo: <class 'float'> )
Ahorro mensual: 120.0 €  (tipo: <class 'float'> )
Meses necesarios (exacto): 8.333333333333334
Meses completos necesarios: 8.0
Dinero que faltaría ahorrar en el último mes: 40.0 €
¿Se cumple el objetivo en un año o menos? True
```

---
