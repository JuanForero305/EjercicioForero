""""
Leer 10 números negativos y convertirlos a positivos e imprimir la suma de dichos
números.
"""
# Inicializar suma
sumaPositivos = 0
# Leer 10 números negativos
for i in range(10):
 numero = int(input("Ingrese un número negativo: "))
 if numero < 0:
    sumaPositivos += abs(numero) # Convertir a positivo y sumar
# Imprimir la suma de los números convertidos
print(f"La suma de los números convertidos a positivos es: {sumaPositivos}")