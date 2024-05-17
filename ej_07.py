"""
Desarrollar un programa que permita generar 8 números aleatorios entre 1 y 100.
Se deberá establecer cuál fue el mayor de los números pares y el menor de los números impares en el conjunto.


Por ejemplo, en una secuencia de números: 8, 15, 9, 2, 27, 18, 6, 33;
el mayor de los pares sería el número 18 y el menor de los impares el número 9.
"""

import random

random.seed(76)
mayor = None
menor = None
secuencia = ""
for i in range(8):
    num = random.randint(1, 100)
    secuencia = str(num) + " " + secuencia

    if num % 2 == 0 and (mayor is None or num > mayor):
        mayor = num
    elif num % 2 == 1 and (menor is None or num < menor):
        menor = num

print(secuencia)

print("Menor impar:", menor)
print("Mayor par:", mayor)