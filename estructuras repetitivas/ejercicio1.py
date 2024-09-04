"""
leer 20 numeros e imprimir cuantos son positivos,cuantos negativos y cuantos neutros
"""
# Inicializar contadores
positivoContador = 0
negativoContador = 0
neutrosContador = 0
# Leer 20 números
for i in range(20):
 numero = int(input("Ingrese un número: "))
 if numero > 0:
     positivoContador += 1
 elif numero < 0:
      negativoContador += 1
 else:
     neutrosContador += 1
# Imprimir resultados
print(f"Positivos: {positivoContador }")
print(f"Negativos: {negativoContador}")
print(f"Neutros: {neutrosContador }")