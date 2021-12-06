porcentaje_1 = 20
porcentaje_2 = 25
porcentaje_3 = 40;
porcentaje_4 = 50;
numero_trajes = int(input("Ingresar la cantidad de trajes a comprar: "))
costo_traje = int(input("Ingresar el costo del traje: "))

if ( numero_trajes == 1):
    subtotal = costo_traje * numero_trajes
    descuento = (subtotal * porcentaje_1)/100

else:
    if (numero_trajes == 2):
        subtotal = costo_traje * numero_trajes
        descuento = (subtotal * porcentaje_2) / 100

    else:
        if (numero_trajes == 3):
            subtotal = costo_traje * numero_trajes
            descuento = (subtotal * porcentaje_3) / 100

        else:
            if (numero_trajes > 3):
                subtotal = costo_traje * numero_trajes
                descuento = (subtotal * porcentaje_4) / 100

total = subtotal - descuento
print("Subtotal: ", subtotal)
print("Descuento aplicado: ", descuento)
print("El total a pagar por la compra del/los trajes es: ", total)