mensaje="hola,estoy aprendiendo python"
nombre="sofia"
formacion="ADSO"
edad=17
estatura=1.63
peso=65
#forma de imprimir 1
print(mensaje,"Mi nombre es:",nombre, "soy de la formacion:",formacion,"tengo:",edad,"años","mido:",estatura,"peso:",peso,"kg")
#forma de imprimir 2
print(f"{mensaje} Mi nombre es:{nombre},soy de la formacion: {formacion},tengo: {edad} años,mido:{estatura},y peso: {peso} kg")


l=10
c=15
suma=l+c
resta = l-c
multiplicacion = l*c
division_cociente= l//c
division_residuo=l%c
#forma de imprimir 1
print("El resultado de la suma es:",suma,"el resultado de la resta es:",resta,"el resutado de la multiṕlicacion es:",multiplicacion,"el resultado de la division_cociente es:",division_cociente,"el resultado de la division_residuo es:",division_residuo)
#forma de imprimir 2
print(f"El resultado de la suma es:{suma},el resultado de la resta es: {resta},el resutado de la multiṕlicacion es: {multiplicacion},el resultado de la division_cociente es:{division_cociente},y el resultado de la division_residuo es:{division_residuo}")

"""
ejercicio pidiendo datos por teclado
"""
numero1=int(input("digite un valor:"))
numero2=int(input("digite otro valor:"))
print(f"el resustado de la suma es:{numero1+numero2}")
print(f"el resultado de la resta es:{numero1-numero2}")
print(f"el resultado de la multiplicacion es:{numero1*numero2}")
print(f"el resulultado de la division de cociente es:{numero1//numero2}")
print(f"el resultado de la division de residuo es:{numero1%numero2}")