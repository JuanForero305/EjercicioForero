"""
Calcular la cantidad de hombres y mujeres presentes en un salón de clases con un
total de n personas.
"""
# Inicializar contadores
contadorHombres = 0
contadorMujeres = 0
# Leer la cantidad de personas
n = int(input("Ingrese la cantidad total de personas en el salón: "))
# Leer el sexo de cada persona
for i in range(n):
 sexo = input("Ingrese el sexo de la persona (Masculino para hombre, Femenino para mujer): ").upper()
 if sexo == 'Masculino':
     contadorHombres += 1
 elif sexo == 'Femenino':
     contadorMujeres += 1
# Imprimir resultados
print(f"Cantidad de hombres: {contadorHombres}")
print(f"Cantidad de mujeres: {contadorMujeres}")