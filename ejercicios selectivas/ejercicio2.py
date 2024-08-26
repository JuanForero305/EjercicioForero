numeroZapatilla=int(input("digite la cantidad de zapatillas:"))
valorcompra=int(input("digite el valor total de la compra:"))
if numeroZapatilla >=3 :
    descuento1= valorcompra * (20/100)
    valorfinal= valorcompra - descuento1
    print(f"el valor de la compra con el descuento 20% es {valorfinal}")
elif numeroZapatilla < 3 :
     descuento2= valorcompra * (10/100)
     valorfinal= valorcompra - descuento2
     print(f"el valor de la compra con el decuento 10% es {valorfinal}")
else :
    print=(f"no ingreso correctamente los datos")