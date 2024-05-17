"""
La final de una carrera de ciclistas tiene n competidores (n se ingresa por teclado).

Desarrollar un programa que permita cargar, por cada competidor, nombre y tiempo de carrera. Luego se pide:

a) Determinar y mostrar el nombre del ganador de la carrera.

b) Ingresar por teclado el tiempo record registrado para dicha carrera. 
Determinar si el tiempo del ganador es menor al tiempo record, mostrar un mensaje.

c) Calcular y mostrar el tiempo promedio entre todos los ciclistas.
"""

record = int(input("Ingresar tiempo record"))
n = int(input("Cantidad de competidores:"))
ganador = None
tiempo_ganador = 0
acumulado_tiempo = 0

for i in range(n):
    nombre_participante_actual = input("Nombre del participante: ")
    tiempo_participante_actual = int(input("Tiempo del participante: "))
    
    # A
    if (ganador is None or tiempo_participante_actual > tiempo_ganador):
        tiempo_ganador = tiempo_participante_actual
        ganador = nombre_participante_actual

    # C
    acumulado_tiempo += tiempo_participante_actual

if tiempo_ganador < record:
    print("El ganador logro romper el record", record)

promedio = acumulado_tiempo / n


print("Ganador:", ganador)
print("Tiempo:", tiempo_ganador)

print("Promedio:", promedio)
