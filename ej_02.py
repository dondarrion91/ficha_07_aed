"""
Cargar por teclado dos números, e imprimir los números impares que se encuentran comprendidos entre ellos,
en forma ascendente y descendente.
"""

num1 = int(input("numero 1:"))
num2 = int(input("numero 2:"))

asc = ""
desc = ""

for i in range(num2, num1 - 1, -1):
    if i % 2 == 1:
        desc += str(i)

for i in range(num1, num2 + 1):
    if i % 2 == 1:
        asc += str(i)

print(asc)
print(desc)