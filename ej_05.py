"""
Escribir un programa que permita leer la cantidad de números enteros ingresados por el usuario y calcular lo siguiente:

a) El segundo menor

b) El promedio de los números positivos.

c) El mayor de los números negativos.
"""

n = int(input("Cantidad de numeros enteros:"))
menor = None
segundo_menor = None
positivos = 0
count_positivos = 0
mayor_negativos = None

for i in range(n):
    numero = int(input("Ingresar número entero:"))

    if menor is None or (numero < menor):
        segundo_menor = menor
        menor = numero
    elif segundo_menor is None or (numero < segundo_menor):
        segundo_menor = numero

    if numero >= 0:
        positivos += numero
        count_positivos += 1
    elif (mayor_negativos is None) or numero > mayor_negativos:
        mayor_negativos = numero

promedio_positivos = positivos / count_positivos

print("Menor:", menor)
print("Segundo Menor:", segundo_menor)
print("Promedio positivos:", promedio_positivos)
print("Mayor de los negativos", mayor_negativos)