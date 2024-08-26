nombre=input("Ingrese su nombre y apellido:")
ColorBalota=input("Digite el color de la balota (rojo, verde, otro):")
valorCompra=int(input("Digite el valor de la compra:"))


if ColorBalota == "rojo"  :
    descuento = 0.15 * valorCompra
    

elif ColorBalota == "verde" :
    descuento = 0.20 * valorCompra
    
else : 
    descuento = 0

valorFinal= valorCompra - descuento
print(f"Valor de la compra: ${valorCompra}")
print(f"Color de la balota: {ColorBalota}")
print(f"Descuento aplicado: ${descuento}")
print(f"Valor a pagar: ${valorFinal}")