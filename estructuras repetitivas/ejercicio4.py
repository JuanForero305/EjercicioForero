"""
Calcular e imprimir la tabla de multiplicar de un número cualquiera, el cual se
digitará por teclado. Imprimir el multiplicando, el multiplicador y el producto.
"""
# Leer el número para la tabla de multiplicar
numero = int(input("Ingrese un número para la tabla de multiplicar: "))
# Calcular e imprimir la tabla de multiplicar
for i in range(5, 11):
 producto = numero * i
 print(f"{numero} x {i} = {producto}")