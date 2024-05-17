"""
Desarrollar un programa que permita ingresar las coordenadas de n puntos en el plano, e informe:

a) En qué cuadrante se encuentra cada uno.

b) Determinar cuántos puntos se encuentran en el primer o tercer cuadrante.

c) Determinar cuál de todos los puntos cargados se encuentra a mayor distancia del origen de coordenadas.
"""

n = int(input("Ingresar cantidad de puntos a ingresar:"))
primer_cuadrante = 0
tercer_cuadrante = 0
mayor_distancia = None
mayor_coordenada = None

for i in range(n):
    x = int(input("Ingresar coordenada x:"))
    y = int(input("Ingresar coordenada y:"))
    
    if x > 0 and y > 0:
        print("El punto se encuentra en el primer cuadrante")
        primer_cuadrante += 1
    elif x > 0 and y < 0:
        print("El punto se encuentra en el cuarto cuadrante")
    elif x < 0 and y > 0:
        print("El punto se encuentra en el segundo cuadrante")
    elif x < 0 and y < 0:
        print("El punto se encuentra en el tercer cuadrante")
        tercer_cuadrante += 1
    else:
        print("El punto es el origen de coordenadas")

    distancia = (x*2 + y*2) ** 0.5
    
    if mayor_distancia is None or distancia > mayor_distancia:
        mayor_distancia = distancia
        mayor_coordenada = x, y

print("Cantidad de puntos en el primer cuadrante:", primer_cuadrante)
print("Cantidad de puntos en el tercer cuadrante:", tercer_cuadrante)
print(mayor_coordenada)
print(mayor_distancia)
