"""
Generar n numeros aleatorios entre el rango de 5000 y 450000,
por cada uno de ellos mostrar y generar el numero hexadecimal
"""

import random
random.seed(72)

n = int(input('Ingrese la cantidad de numeros a procesar: '))

for i in range(n):
    numero = random.randrange(5000, 450000)
    hexadecimal = ''
    # proceso de conversion hexadecimal
    valor = numero % 16
    siguiente = numero // 16
    digito = ''
    while valor > 0:
        if valor < 10:
            digito = str(valor)
        else:
            digito = chr(55 + valor)
        hexadecimal = digito + hexadecimal
        valor = siguiente % 16
        siguiente //= 16

    print('El numero ', numero, 'en hexadecimal es', hexadecimal)