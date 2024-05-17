"""
Ingresar por teclado los sueldos de un vendedor, correspondientes al primer semestre del año y luego:

a) Calcular su aguinaldo, sabiendo que es la mitad del sueldo más alto del período.

b) Determinar en qué mes recibió el sueldo más bajo del período.

c) Informar el sueldo promedio del semestre.
"""

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio")
mas_alto = None
mas_bajo = None
acumulado = 0

for mes in meses:
    sueldo = int(input("Ingresar el sueldo del mes de " + mes))
    
    if mas_alto is None and mas_bajo is None:
        mas_bajo = sueldo, mes
        mas_alto = sueldo, mes

    if sueldo > mas_alto[0]:
        mas_alto = sueldo, mes
    
    if sueldo < mas_bajo[0]:
        mas_bajo = sueldo, mes

    acumulado += sueldo

aguinaldo = mas_alto[0] / 2
promedio = acumulado / len(meses)

print("Aguinaldo a cobrar:", aguinaldo)
print("Sueldo mas bajo:", mas_bajo[0], "en", mas_bajo[1])
print("Sueldo promedio:", promedio)