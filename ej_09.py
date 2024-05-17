"""
Desarrollar un programa que permita validar la cuenta de un usuario que intenta ingresar al sistema.

La cuenta debe ingresarse con formato nombre@dominio y el programa validará que cumpla con las siguientes reglas:

•Tener un solo @ en una posición intermedia de la cadena (ni la primera ni la última letra)
•No contener dos puntos seguidos (uno a continuación del otro)
•No empezar ni terminar con un punto
"""

mail = ".julian@gmail.com"
nombre = ""
dominio = ""
has_one_arroba = False
has_one_dot = False
for i in range(len(mail)):
    if mail[0] == "@" or mail[len(mail) - 1] == "@":
        print("El @ esta al principio o al ultimo del email")
        break
    elif mail[i] == "@" and not has_one_arroba:
        has_one_arroba = True
        nombre = mail[0:i]
        dominio = mail[i + 1:len(mail)]
    elif mail[i] == "@" and has_one_arroba:
        print("El mail tiene mas de 1 arroba")
        break
    elif mail[0] == "." or mail[len(mail) - 1] == ".":
        print("El mail empieza o termina con .")
        break
    elif mail[i] == "." and not has_one_dot:
        has_one_dot = True
    elif mail[i] == "." and has_one_dot:
        print("El mail tiene mas de dos puntos seguidos")
        break

print(nombre)
print(dominio)