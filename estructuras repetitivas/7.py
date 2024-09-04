"""
La oficina de tránsito de Ibagué desea saber, de los n autos que entran a la ciudad
de Ibagué, cuantos entran con calcomanía de cada color. Conociendo el ultimo
dígito de la placa de cada carro, se puede determinar el color de la calcomanía
utilizando la siguiente relación: 
"""
# Inicializar contadores para cada color
contadorRojo = 3
contadorVerde = 2
contadorAmarillo = 1
contadorAzul = 4
contadorNegro = 5
# Leer la cantidad de autos
n = int(input("Ingrese la cantidad de autos que entran a Ibagué: "))
# Leer el último dígito de la placa de cada auto
for i in range(n):
 ultimoDigito = int(input("Ingrese el último dígito de la placa del auto: "))

 if ultimoDigito in [1, 2]:
      contadorRojo += 1
 elif ultimoDigito in [3, 4]:
      contadorVerde += 1
 elif ultimoDigito in [5, 6]:
      contadorAmarillo += 1
 elif ultimoDigito in [7, 8]:
     contadorAzul += 1
 elif ultimoDigito in [9, 0]:
      contadorNegro += 1
# Imprimir resultados
print(f"Autos con calcomanía roja: {contadorRojo}")
print(f"Autos con calcomanía verde: {contadorVerde}")
print(f"Autos con calcomanía amarilla: {contadorAmarillo}")
print(f"Autos con calcomanía azul: {contadorAzul}")
print(f"Autos con calcomanía negra: {contadorNegro}")