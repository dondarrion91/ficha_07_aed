n = int(input("Cantidad de barcos a cargar:"))
total_veleros = 0
total_lanchas = 0
mayor_velero = None
nombre_mayor_velero = None
total_montos = 0
total = 0

for i in range(n):
    tipo = None

    nombre = input("Nombre del barco:")
    while tipo is None or tipo not in (1, 2):
        tipo = int(input("Tipo de barco(1 velero, 2 lancha):"))

    monto = int(input("Monto a pagar:"))
    
    if tipo == 1:
        total_veleros += monto

        if mayor_velero is None or monto > mayor_velero:
            mayor_velero = monto
            nombre_mayor_velero = nombre
    else:
        total_lanchas += monto

    total_montos += monto
    total += 1
    
    tipo = None

promedio = total_montos / total

porcentaje_veleros = (total_veleros * 100) / total_montos
porcentaje_lanchas = (total_lanchas * 100) / total_montos

print("Total anual veleros:", total_veleros)
print("Total anual lanchas:", total_lanchas)

print("Nombre mayor velero:", nombre_mayor_velero)
print("Monto mayor velero:", mayor_velero)

print("Promedio:", promedio)

print("Porcentaje de veleros:", porcentaje_veleros)
print("Porcentaje de lanchas:", porcentaje_lanchas)